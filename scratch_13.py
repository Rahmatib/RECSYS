import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network

# # Read the CSV file into a DataFrame
# data = {
#     'title': ['Probabilistic matrix factorization', 'Learning to rank: from pairwise approach to listwise approach',
#               'Factorization meets the neighborhood: a multifaceted collaborative filtering model',
#               'Personalized recommendation in social tagging systems using hierarchical clustering',
#               'Matrix factorization techniques for recommender systems',
#               'Collaborative filtering with temporal dynamics',
#               'Scalable collaborative filtering approaches for large recommender systems',
#               'The YouTube video recommendation system', 'Factorization machines'],
#     'authors': ['Mnih, Andriy and Salakhutdinov, Russ R', 'Cao, Zhe and Qin, Tao and Liu, Tie-Yan and Tsai, Ming-Feng and Li, Hang',
#                 'Koren, Yehuda', 'Shepitsen, Andriy and Gemmell, Jonathan and Mobasher, Bamshad and Burke, Robin',
#                 'Koren, Yehuda and Bell, Robert and Volinsky, Chris', 'Koren, Yehuda',
#                 'TakÃ¡cs, GÃ¡bor and PilÃ¡szy, IstvÃ¡n and NÃ©meth, BottyÃ¡n and Tikk, Domonkos',
#                 'Davidson, James and Liebald, Benjamin and Liu, Junning and Nandy, Palash and Van Vleet, Taylor and Gargi, Ullas and Gupta, Sujoy and He, Yu and Lambert, Mike and Livingston, Blake and others',
#                 'Rendle, Steffen'],
#     'number_of_authors': [2, 5, 1, 4, 3, 1, 4, 10, 1],
#     'Categories': [
#         '/technology & computing/artificial intelligence, /technology & computing/computing',
#         '/technology & computing/artificial intelligence, /technology & computing/computing',
#         '/technology & computing/artificial intelligence, /technology & computing/computing, /technology & computing/computing/information and network security, /technology & computing/computing/computer software and applications',
#         '/technology & computing/computing/information and network security, /technology & computing/computing/computer software and applications, /technology & computing/computing/internet/social networking, /technology & computing/artificial intelligence, /technology & computing/computing/computer software and applications/browsers, /technology & computing/computing/internet/web hosting, /technology & computing/computing/internet/it and internet support, /education/online education, /video gaming/mobile games',
#         '/technology & computing/artificial intelligence',
#         '/technology & computing/artificial intelligence, /technology & computing/computing/internet/email, /technology & computing/computing/information and network security, /technology & computing/computing/computer software and applications',
#         '/technology & computing/artificial intelligence, /business and finance/business/business i.t., /technology & computing/computing/information and network security',
#         '/technology & computing/computing/computer software and applications/browsers, /television, /technology & computing/computing/internet/social networking, /television/music tv, /technology & computing/computing/internet/it and internet support, /technology & computing/computing/information and network security, /technology & computing/computing/internet/web hosting, /video gaming/mobile games',
#         '/technology & computing/artificial intelligence, /technology & computing/computing, /technology & computing/computing/computer software and applications/operating systems'
#     ]
# }
# # Read the CSV file into a DataFrame
# file_path1 = 'c:\\Users\\rahma\\OneDrive\\Desktop\\lit review paper\\2005-2010.csv'
# file_path2 = 'c:\\Users\\rahma\\Downloads\\2010-2015.csv'
# file_path3 = 'c:\\Users\\rahma\\Downloads\\2015-2020.csv'
# file_path4 = 'c:\\Users\\rahma\\Downloads\\2020-2023.csv'
# file_path5 = 'c:\\Users\\rahma\\Downloads\\2005-2023.csv'
# df= pd.read_csv(r"C:\Users\rahma\OneDrive\Desktop\lit review paper\2007-2024\2007-2010.csv")
# df = pd.read_csv(r"C:\Users\rahma\OneDrive\Desktop\lit review paper\2007-2024\2010-2015.csv")
# df = pd.read_csv(r"C:\Users\rahma\OneDrive\Desktop\lit review paper\2007-2024\2015-2020.csv")
# df = pd.read_csv(r"C:\Users\rahma\OneDrive\Desktop\lit review paper\2007-2024\2020-2024.csv")
df = pd.read_csv(r"C:\Users\rahma\OneDrive\Desktop\lit review paper\2007-2024\2020-2024.csv")

# df = pd.read_csv(file_path4, encoding='latin1')
# df = pd.DataFrame(data)


import pandas as pd
import networkx as nx
from pyvis.network import Network

# # Read the CSV file into a DataFrame
# file_path1 = 'c:\\Users\\SocialComputing-1\\Downloads\\2005-2010.csv'
# file_path2 = 'c:\\Users\\SocialComputing-1\\Downloads\\2010-2015.csv'
# file_path3 = 'c:\\Users\\SocialComputing-1\\Downloads\\2015-2020.csv'
# file_path4 = 'c:\\Users\\SocialComputing-1\\Downloads\\2020-2023.csv'
# df = pd.read_csv(file_path4, encoding='latin1')

# Create a graph
B = nx.Graph()

# Add nodes for papers and categories
for idx, paper in df.iterrows():
    paper_number = idx + 1
    B.add_node(paper_number, bipartite=0, label=str(paper_number) + ': ' + str(paper['title']))

    # Paper node categories
    categories = str(paper['Categories']).split(", ")
    for category in categories:
        # # Extract the content after the last slash
        # last_part = category.split("/")[-1].strip()
        # B.add_node(last_part, bipartite=1, label=last_part)
        # # Category node
        # B.add_edge(paper_number, last_part)  # Edge connecting paper to categories
        # Directly use the category name as it is
        B.add_node(category, bipartite=1, label=category)
        # Category node
        B.add_edge(paper_number, category)  # Edge connecting paper to categories

# Get the category nodes
category_nodes = {node for node, data in B.nodes(data=True) if data['bipartite'] == 1}

# Calculate degree centrality for categories
category_degree_centrality = nx.degree_centrality(B)
category_betweenness_centrality = nx.betweenness_centrality(B)
# Calculate PageRank
pagerank = nx.pagerank(B)


# Print degree centrality for categories
print("\nCategory Degree Centrality:")
for node, centrality in sorted(category_degree_centrality.items(), key=lambda x: x[1]):
    if node in category_nodes:
        print(f"Category {node}: Degree Centrality = {centrality}")

print("\nCategory betweenness Centrality:")
for node, centrality in sorted(category_betweenness_centrality.items(), key=lambda x: x[1]):
    if node in category_nodes:
        print(f"Category {node}: Betweenness Centrality = {centrality}")

# Print PageRank for categories
print("\nCategory PageRank:")
for node, rank in sorted(pagerank.items(), key=lambda x: x[1]):
    if node in category_nodes:
        print(f"Category {node}: PageRank = {rank}")

# Draw the graph with Kamada-Kawai layout
pos = nx.kamada_kawai_layout(B)

# Adjust the font size and family
node_font_size = 8
font_family = 'Arial'

# # Specify node colors

#
# # Draw the graph with title
# nt = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
# nt.from_nx(B)
# Draw the graph with title
# Create a PyVis network graph
nt = Network(height='600px', width='100%', bgcolor='#ffffff', font_color='black')  # Set background to white, font to black

# Manually add nodes with specific colors
for node, data in B.nodes(data=True):
    if data['bipartite'] == 0:
        nt.add_node(node, label=data['label'], color='darkblue', size=10)  # Paper nodes - dark blue
    else:
        nt.add_node(node, label=data['label'], color='lightblue', size=10)  # Category nodes - light blue

# Manually add edges with black color
for edge in B.edges:
    nt.add_edge(edge[0], edge[1], color='black')  # Edges - black
nt.show_buttons(filter_=['physics'])
nt.show("bipartite_graph.html")



# # Extract categories from DataFrame
# all_categories = df['Categories'].str.split(', ').explode()
#
#
# def generate_wordcloud(frequencies):
#     # Create a WordCloud instance
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frequencies)
#
#     # Display the word cloud using matplotlib
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     plt.show()
#     return wordcloud


















# # Create a graph
# B = nx.Graph()
#
# # Add nodes for papers and categories
# for idx, paper in df.iterrows():
#     paper_number = idx + 1
#     B.add_node(paper_number, bipartite=0, label=str(paper_number) + ': ' + paper['title'])  # Paper node
#     categories = paper['Categories'].split(", ")
#     for category in categories:
#         # Extract the content after the last slash
#         last_part = category.split("/")[-1].strip()
#         B.add_node(last_part, bipartite=1, label=last_part)  # Category node
#         B.add_edge(paper_number, last_part)  # Edge connecting paper to categories
# # Get the category nodes
# category_nodes = {node for node, data in B.nodes(data=True) if data['bipartite'] == 1}
#
# # Calculate degree centrality for categories
# category_degree_centrality = nx.degree_centrality(B)
# category_betweenness_centrality = nx.betweenness_centrality(B)
#
#
# # Print degree centrality for categories
# print("\nCategory Degree Centrality:")
# for node, centrality in sorted(category_degree_centrality.items(), key=lambda x: x[1]):
#     if node in category_nodes:
#         print(f"Category {node}: Degree Centrality = {centrality}")
#
# print("\nCategory betweenness Centrality:")
# for node, centrality in sorted(category_betweenness_centrality.items(), key=lambda x: x[1]):
#     if node in category_nodes:
#         print(f"Category {node}: Betweenness Centrality = {centrality}")
# # # Calculate degree centrality for papers and categories separately
# # paper_degree_centrality = nx.degree_centrality(B)
# # category_degree_centrality = nx.degree_centrality(B)
# #
# # # Print degree centrality for papers
# # print("Paper Degree Centrality:")
# # for node, centrality in sorted(paper_degree_centrality.items(), key=lambda x: x[1]):
# #     print(f"Paper {node}: Degree Centrality = {centrality}")
# #
# # # Print degree centrality for categories
# # print("\nCategory Degree Centrality:")
# # for node, centrality in sorted(category_degree_centrality.items(), key=lambda x: x[1]):
# #     print(f"Category {node}: Degree Centrality = {centrality}")
#
# # Draw the graph with Kamada-Kawai layout
# pos = nx.kamada_kawai_layout(B)
#
# # Adjust the font size and family
# node_font_size = 8
# font_family = 'Arial'
#
# # Specify node colors
# # paper_node_colors = ['pink' if node in paper_degree_centrality else 'lightblue' for node in B.nodes]
# category_node_colors = ['red' if node in category_degree_centrality else 'lightgreen' for node in B.nodes]
#
# # Draw the graph with title
# nt = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
# nt.from_nx(B)
# nt.show_buttons(filter_=['physics'])
# nt.show("bipartite_graph.html")
# Author: TristanCB
# Description: Wikipedia graph generator
# roget graph built by scraping wikipedia pages for their first 20 links.
# Reference for visualization: 
# Weeks, Margaret R, et. al. https://doi.org/10.1023/A:1015457400897

# Building a network graph from scraped data: 
# https://python-graph-gallery.com/321-custom-networkx-graph-appearance/

import networkx as nx
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import heapq
import os
import time
import pickle
from operator import itemgetter
from collections import defaultdict
import numpy
from scipy.cluster import hierarchy
from scipy.spatial import distance

# Defining the domain to scrape and the starting url
domain = "https://en.wikipedia.org"
startpage = "/wiki/Airfoil"
# We will use this list to append to. Ideally I would implement a heapq.
urls = []
# To pass to request as kwarg
proxies = {'http': "socks5://127.0.0.1:9150"}
# Count at which we decide to stop
SCRAPECOUNT = 10

# Initialize graph network
G = nx.Graph()
plt.figure(figsize=(20,14)) # Large size makes it look better

def get_links(base_wiki_page):
    '''
    Small function which returns first 20 links of a wikipedia page.
    It also adds them to the nx.Graph() object
    '''
    url = domain + base_wiki_page # Construct url to send request
    req = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(req.text, 'lxml')
    # Find all the internal wikipedia links.
    links = soup.find_all('a')

    # We will only consider the first 20 links in the HTML
    first_twenty_links = links[0:20]

    for link in first_twenty_links:
        textlink = link.get('href')
        if textlink is None:
            continue
        
        # flagged urls will be disregarded
        flagged = False
        for i in ['https://', '/w/', '//', '#', ':', '.PNG', '.svg', ]:
            if i in textlink:
                flagged = True

        if flagged == False:
            # Add an edge to the graph
            G.add_edge(f"{base_wiki_page[6:]}", f"{textlink[6:]}")
            # Construct a list for deeper iterations.
            urls.append(textlink)

# Initially we populate the list
get_links(startpage)

# Web crawling
scrape_counter = 0 # A counter to check how many pages have been scraped
while scrape_counter < SCRAPECOUNT:
    # Delay crawl to not overload wikipedia servers
    next_url = urls.pop(0)
    print(f"Waittime prior to scraping: {next_url}")
    scrape_counter += 1
    get_links(next_url)
    time.sleep(0.1)

def save_object(obj, filename):
    '''
    https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence
    '''
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

save_object(G, 'G.pkl')

# with open('G.pkl', 'rb') as input:
#     G = pickle.load(input)

###
# The remainder of this file was taken from: 
# https://networkx.org/documentation/stable/auto_examples/algorithms/plot_blockmodel.html#sphx-glr-auto-examples-algorithms-plot-blockmodel-py

def create_hc(G):
    """Creates hierarchical cluster of graph G from distance matrix"""
    path_length = nx.all_pairs_shortest_path_length(G)
    distances = numpy.zeros((len(G), len(G)))
    for u, p in path_length:
        for v, d in p.items():
            distances[u][v] = d
    # Create hierarchical cluster
    Y = distance.squareform(distances)
    Z = hierarchy.complete(Y)  # Creates HC using farthest point linkage
    # This partition selection is arbitrary, for illustrive purposes
    membership = list(hierarchy.fcluster(Z, t=1.15))
    # Create collection of lists for blockmodel
    partition = defaultdict(list)
    for n, p in zip(list(range(len(G))), membership):
        partition[p].append(n)
    return list(partition.values())

# Extract largest connected component into graph H
H = G.subgraph(next(nx.connected_components(G)))
# Makes life easier to have consecutively labeled integer nodes
H = nx.convert_node_labels_to_integers(H)
# Create parititions with hierarchical clustering
partitions = create_hc(H)
# Build blockmodel graph
BM = nx.quotient_graph(H, partitions, relabel=True)

# Draw original graph
pos = nx.spring_layout(H, iterations=100)
plt.subplot(211)
nx.draw(H, pos, with_labels=False, node_size=10)

# Draw block model with weighted edges and nodes sized by number of internal nodes
node_size = [BM.nodes[x]["nnodes"] * 10 for x in BM.nodes()]
edge_width = [(0.1 * d["weight"]) for (u, v, d) in BM.edges(data=True)]
# Set positions to mean of positions of internal nodes from original graph
posBM = {}
for n in BM:
    xy = numpy.array([pos[u] for u in BM.nodes[n]["graph"]])
    posBM[n] = xy.mean(axis=0)
plt.subplot(212)
nx.draw(BM, posBM, node_size=node_size, width=edge_width, with_labels=False)
plt.axis("off")
plt.show()
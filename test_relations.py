from functions import *
import networkx as nx
import matplotlib.pyplot as plt

def run():
    #set = [1, 2, 3, 4, 5]
    #set = ['a', 'b', 'c', 'd']
    set = [1,2,3,4,5]
    #relation =((1,1), (2,2), (3,3),(4,4),(10,10), (20,20),(1,2) )
    #relation =(('a','a'),('a','d'),('d','d'),('d','a'),('b','b'),('b','c'),('c','c'),('c','b'))
    relation = [(1,3), (2,4), (3,5) ,(3,1), (4,2), (5,3), (1,1), (2,2), (3,3), (4,4), (5,5)]
    print(print_reflexive(relation,set))
    print(print_symmetric(relation))
    print(print_transitive(relation))
    print(print_equivalence_relation(set,relation))
    print(print_parcial_order_relation(set, relation))



G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)


G.add_edge(1,1)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(3,5)
G.add_edge(3,1)
G.add_edge(4,2)
G.add_edge(5,3)
G.add_edge(1,1)
G.add_edge(2,2)
G.add_edge(3,3)
G.add_edge(4,4)
G.add_edge(5,5)

print(G.nodes())
print(G.edges())

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows = True)

plt.show()


if __name__ == '__main__':
    run()

    
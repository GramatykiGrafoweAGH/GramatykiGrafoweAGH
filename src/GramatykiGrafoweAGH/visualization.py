from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import networkx as nx

from GramatykiGrafoweAGH import Node, Graph

node_colors = {
    0: {
        'E': '#fe0000',
        'e': '#fe0000',
    },
    1: {
        'E': '#4e81bd',
        'I': '#c0504d',
        'i': '#c0504d',
    },
    2: {
        'E': '#93d051',
        'I': '#f79645',
        'i': '#f79645',
    },
    3: {
        'E': '#feff00',
        'I': '#d9d9d9',
        'i': '#d9d9d9',
    },
}


def get_node_color(node: Node) -> str:
    return node_colors.get(min(node.level, 3), {}).get(node.label, 'violet')


def get_node_colors(G: nx.Graph) -> List[str]:
    return [get_node_color(node) for node in G.nodes]


def get_node_labels(G: nx.Graph) -> Dict[int, str]:
    return {
        node: node.label
        for node in G.nodes
    }


def calculate_layout(G: nx.Graph) -> Dict[int, Tuple[float, float]]:
    return {
        node: (node.x, node.y - node.level * 1.5)
        for node in G.nodes
    }


def draw_graph(G: Graph, *, level: Optional[int] = None) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    ax.set(xlabel='$x$', ylabel='$y$')

    G = G._G
    if level is not None:
        G = G.subgraph([node for node in G.nodes if node.level == level])

    pos = calculate_layout(G)
    node_color = get_node_colors(G)
    labels = get_node_labels(G)
    nx.draw(G, ax=ax, pos=pos, node_color=node_color, labels=labels)

    return fig


def show_graph(G: Graph, **kwargs):
    draw_graph(G, **kwargs)
    plt.show()

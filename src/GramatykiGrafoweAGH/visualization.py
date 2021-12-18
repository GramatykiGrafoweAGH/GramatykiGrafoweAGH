from math import dist
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import networkx as nx

from GramatykiGrafoweAGH import Node, Graph, IProduction

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


def get_node_position(node: Node) -> Tuple[float, float]:
    return node.x, node.y - node.level * 1.5


def calculate_layout(G: nx.Graph) -> Dict[int, Tuple[float, float]]:
    return {
        node: get_node_position(node)
        for node in G.nodes
    }


def draw_graph(G: Graph, *, ax: Optional[plt.Axes] = None, level: Optional[int] = None) -> plt.Figure:
    if ax is None:
        fig, ax = plt.subplots()
        fig.tight_layout()
    else:
        fig = None

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


class InteractiveVisualizer:
    def __init__(self, G: Graph, productions: List[IProduction]):
        self.G = G
        self.productions = productions
        self.fig, self.ax = plt.subplots()
        self.fig.tight_layout()
        self.fig.canvas.mpl_connect('button_press_event', self._handle_click)
        self._reset_limits()

    def _reset_limits(self) -> None:
        x, y = 0.5, -0.5
        dx = dy = 3
        self.ax.set(xlim=(x - dx, x + dx), ylim=(y - dy, y + dy))

    def _handle_click(self, event) -> None:
        if not event.dblclick or not self.G.nodes:
            return

        event_xy = event.xdata, event.ydata

        def distance(node: Node) -> float:
            return dist(event_xy, get_node_position(node))

        root = min(self.G.nodes, key=distance)

        for production in self.productions:
            lhs = production.match_lhs(self.G, root)
            if lhs is not None:
                production.apply(self.G, lhs)
                print(type(production).__name__)
                self._draw()
                break
        else:
            print('Cannot apply any production for selected node')

    def _draw(self) -> None:
        old_xlim = plt.xlim()
        old_ylim = plt.ylim()
        self.ax.clear()
        draw_graph(self.G, ax=self.ax)
        self.ax.set(xlim=old_xlim, ylim=old_ylim)
        plt.draw()
        plt.suptitle(f'{self.G.count_duplicates()} duplicated nodes')

    def show(self) -> None:
        self._draw()
        plt.show()

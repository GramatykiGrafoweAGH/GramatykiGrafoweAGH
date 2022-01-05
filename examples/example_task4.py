from GramatykiGrafoweAGH import Node
from GramatykiGrafoweAGH.project.task4 import P7
from tests.project.test_task4 import make_P7_left_side_graph

if __name__ == '__main__':
    G = make_P7_left_side_graph()
    E = G.get_first_node_with_label('E')
    E1 = Node(label='E', x=-5, y=0, level=2)
    G.add_node(E1)
    G.add_edge(E, E1)
    G.apply_production(P7)
    G.assert_no_duplicated_nodes()
    G.show()

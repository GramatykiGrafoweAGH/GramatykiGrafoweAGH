from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.project.task4 import P7
from GramatykiGrafoweAGH.project.task5 import P8
from GramatykiGrafoweAGH.project.task6 import P9
from GramatykiGrafoweAGH.visualization import InteractiveVisualizer

if __name__ == '__main__':
    G = make_initial_graph()
    P1(G)
    productions = [P9, P8, P7, P2]  # without P1
    iv = InteractiveVisualizer(G, productions)
    iv.show()

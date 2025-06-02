from graphviz import Digraph


# crea graph dirifgifo
disiplia = Digraph(comment="ejemplo disiplina")


disiplia.node("a", "nodo a")
disiplia.node("b", "nodo b")
disiplia.node("c", "nodo c")
disiplia.node("d", "nodo d")

disiplia.edges(["ab", "ac", "bc", "cd"])
disiplia.edge("c", "a", constrint="false")

disiplia.save("displina.dot")
disiplia.render("disiplina", format="png", view=True)

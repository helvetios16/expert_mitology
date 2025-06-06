import json
import networkx as nx

# Cargar archivo JSON
with open("mitologia.json") as f:
    data = json.load(f)

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar nodos
for node in data["nodes"]:
    G.add_node(node["id"], **node)

# Agregar aristas
for edge in data["edges"]:
    G.add_edge(edge["from"], edge["to"], relation=edge["relation"])

# Mostrar nodos y relaciones
print("📌 Nodos:")
for node, attrs in G.nodes(data=True):
    print(f"  {node} -> {attrs}")

print("\n🔗 Relaciones:")
for u, v, attrs in G.edges(data=True):
    print(f"  {u} --[{attrs['relation']}]--> {v}")

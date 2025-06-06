import json
import networkx as nx
from arta import RulesEngine

# 🚀 1. Cargar grafo

# Cargar archivo JSON
with open("mito.json") as f:
    data = json.load(f)

# Cargar grafo dirigido
G = nx.DiGraph()

# Agregar nodos
for node in data["nodes"]:
    G.add_node(node["id"], **node)

# Agregar aristas
for edge in data["edges"]:
    G.add_edge(edge["from"], edge["to"], relation=edge["relation"])

# 🚀 2. Aplicar reglas del sistema experto
engine = RulesEngine(config_path=".")

user_input = {"land": "oscuro", "values": "sabiduria", "cultura": "europa"}

result = engine.apply_rules(input_data=user_input)
cultura = result["culture"].get("cultura")
arch = result["archetype"].get("archetype")

print(result)

# 🚀 3. Consultar el grafo según la decisión
candidatos = [
    n
    for n, attrs in G.nodes(data=True)
    if attrs.get("cultura") == cultura and attrs.get("type") == "dios"
]
print("Candidatos dioses:", candidatos)

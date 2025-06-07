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

user_input = {
    "land": "oscuro",
    "values": "sabiduria",
    "creature": "dragon",
    "element": "fuego",
    "role": "sabio",
    "conflict": "guerra",
    "god": "solar",
    "culture": "griega",
    "origin": "semilla",
    "ending": "ciclo",
}

result = engine.apply_rules(input_data=user_input)
print(result)
land = result["world"].get("cultura")
values = result["values"].get("values")
creature = result["creature"].get("creature")
element = result["element"].get("element")
role = result["role"].get("role")
conflict = result["conflict"].get("conflict")
god = result["god"].get("god")
culture = result["culture"].get("culture")
origin = result["origin"].get("origin")
ending = result["ending"].get("ending")

# 🚀 3. Consultar el grafo según la decisión
data = [
    n
    for n, attrs in G.nodes(data=True)
    if attrs.get("cultura") == land or attrs.get("conflicto") == conflict
]
print("Data:", data)

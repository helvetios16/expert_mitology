# import json
# import networkx as nx
from arta import RulesEngine
from openai import OpenAI
from secret import API_DEEPSEEK as DEEP

# # 🚀 1. Cargar grafo
#
# # Cargar archivo JSON
# with open("mito.json") as f:
#     data = json.load(f)
#
# # Cargar grafo dirigido
# G = nx.DiGraph()
#
# for node in data["nodes"]:
#     G.add_node(node["id"], **{k: v for k, v in node.items() if k != "id"})
#
# for edge in data["edges"]:
#     G.add_edge(edge["from"], edge["to"], relation=edge["relation"])

# 🚀 2. Aplicar reglas del sistema experto
engine = RulesEngine(config_path=".")

user_input = {
    "cultura": "oscuro",
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

clean_result = {}
for outer_key, inner_dict in result.items():
    clean_result[outer_key] = next(iter(inner_dict.values()))

# print("Resultado de las reglas:", clean_result)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=DEEP,
)

prompt = f"""

Genera una mitología original basada en las siguientes características:

1. Mundo (world): Describe el tipo de mundo donde ocurre la historia.
2. Valor del protagonista (value): Explica cuál es el valor principal que guía al protagonista.
3. Criatura principal (creature): La criatura mítica o símbolo que habita o representa el mundo.
4. Elemento que controla (element): El elemento natural que tiene influencia o poder en el mundo o sobre el protagonista.
5. Rol del protagonista (role): El papel que desempeña el protagonista en la historia.
6. Conflicto global (conflict): El problema o conflicto principal que afecta al mundo.
7. Dios caído (god): El dios o entidad divina caída o ausente que influye en la historia.
8. Cultura (culture): La cultura o civilización que se mezcla o inspira el mundo.
9. Origen del mundo (origin): Cómo comenzó el mundo o mito principal.
10. Final del protagonista (ending): Cómo termina la historia o el destino del protagonista.

Usa todos estos elementos para inventar una historia mitológica que explique el origen, desarrollo y destino del protagonista en este mundo fantástico. La historia debe ser coherente y combinar los detalles dados, creando una narrativa rica y original.
---
**Entrada:**
- Mundo: {clean_result["world"]}  
- Valor: {clean_result["values"]}  
- Criatura: {clean_result["creature"]}  
- Elemento: {clean_result["element"]}  
- Rol: {clean_result["role"]}  
- Conflicto: {clean_result["conflict"]}  
- Dios caído: {clean_result["god"]}  
- Cultura: {clean_result["culture"]}  
- Origen: {clean_result["origin"]}  
- Final: {clean_result["ending"]}  
---
Genera la mitología basada en estos parámetros. Cuentala como una historia épica, rica en detalles y con un tono narrativo que evoque las antiguas leyendas. Asegúrate de que la historia fluya naturalmente y conecte todos los elementos de manera coherente. No crees secciones o subtítulos, simplemente narra la historia de forma continua y envolvente.
"""
# print(prompt)
completion = client.chat.completions.create(
    extra_body={},
    model="deepseek/deepseek-r1:free",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)

print(completion.choices[0].message.content)

# 🚀 3. Consultar el grafo según la decisión
# data = [
#     n
#     for n, attrs in G.nodes(data=True)
#     if attrs.get("cultura") == land or attrs.get("conflicto") == conflict
# ]
# print("Data:", data)

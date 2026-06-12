import urllib.request
import json

# 1. Buscar dados das APIs
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as r:
    usuarios = json.loads(r.read())

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos") as r:
    tarefas = json.loads(r.read())

# 2. Contar tarefas pendentes por usuario
pendentes_por_usuario = {}
for tarefa in tarefas:
    if not tarefa["completed"]:
        uid = tarefa["userId"]
        pendentes_por_usuario[uid] = pendentes_por_usuario.get(uid, 0) + 1

# 3. Descobrir o usuario mais sobrecarregado
uid_max = max(pendentes_por_usuario, key=pendentes_por_usuario.get)
total_max = pendentes_por_usuario[uid_max]

# 4. Buscar o nome por ID
nome = next(u["name"] for u in usuarios if u["id"] == uid_max)

print(f"Usuário mais sobrecarregado: {nome}")
print(f"Tarefas pendentes: {total_max}")

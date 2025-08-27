# •	Función add_note(title, body) en app/notes.py que agrega un dict {id, title, body,
# •	created_at} a data/notes.json.
# •	CLI python -m app.cli add "Titulo" "Contenido".
# •	Branch y PR:

notes = {
    "id":"",
    "title":"",
    "body":"",
    "created_at":""
}


def add_note(title,body):
    with open("data/notes.json", "a") as file:
        file.write(notes)

#list_notes() y find_notes(query).
#CLI: list, search "palabra".
#Branch/PR feature/3-listar-buscar.
# Issue #5 Pruebas (Dev C)
# Pruebas mínimas de add_note y list_notes con pytest.
# Branch/PR feature/5-tests.
#Pequeño bug


def list_notes():
    pass
def find_notes():
    pass

def delete_notes():
    pass

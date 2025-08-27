# team-notes

Instalación

1.Clonar el repositorio:

git clone https://github.com/PabloOscarSilva430/team-notes.git

2. Ir a la carpeta del proyecto

cd team-notes

3. Ejecutar desde Python

python -m app.cli


Comandos CLI

- Agregar nota (add_note)
    python -m app.cli add (title,body)

- Listar notas (list_notes)
    python -m app.cli list

- Buscar notas (find_notes)
    python -m app.cli find

- Borrar todas las notas (delete_notes)
    python -m app.cli delete


# Ejemplo de uso

## Uso
## El uso de esta seccion es modificada por devMonasterio

## uso 
Esta es la seccion que se esta modificando para generar el conflicto

python -m app.cli add "Tarea" "Hacer el trabajo 2"

python -m app.cli list

python -m app.cli find "Tarea"

python -m app.cli delete

# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto!  
Sigue estas reglas para que el trabajo en equipo sea claro y ordenado.  

---

## 📝 Convención de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/).  

### Tipos más comunes
- ✨ **feat:** nueva funcionalidad (`feat: agregar búsqueda de notas`)
- 🐞 **fix:** corrección de bug (`fix: error en list_notes`)
- 📚 **docs:** cambios en docs (README, CONTRIBUTING, etc.)
- 🧪 **test:** agregar o actualizar tests
- 🛠️ **chore:** tareas de mantenimiento (configuración, build, etc.)

---

## 🌿 Ramas y Pull Requests

- Las ramas se crean a partir de `develop`.  
- Convención de nombres:

Ejemplos:



### Al abrir una PR
- 🔗 Referenciar la **issue** relacionada (`Closes #5`).
- ✍️ Describir claramente qué cambia.
- ✅ Asegurarse que los tests pasen.

---

## 🎨 Estilo de Código

- Mantener un estilo uniforme:
- **Python** → `black` o `flake8`.  
- **JS/React** → `prettier` + `eslint`.  
- Indentación: 4 espacios (Python) / 2 espacios (JS).  
- Usar nombres claros y consistentes.

---

## ✅ Tests

Antes de abrir una PR, asegurate de correr los tests en tu entorno local:

```bash
pytest -v


Si hay Makefile o package.json, podés usar:

make test
# o
npm test

📌 Regla: si agregás una función nueva, también agregá al menos un test en tests/.

🔍 Checklist para PR

Marca esta lista antes de abrir tu PR:

 📦 La rama parte de develop.

 📝 El commit sigue la convención.

 🧪 Los tests pasan en local (pytest).

 📚 Se actualizó la documentación si aplica.

 🔗 La PR referencia su issue (Closes #X).

💡 ¡Con esto mantenemos el repo limpio, entendible y fácil de mantener! 🚀
# 📚 Generador Automático de README.md

Este generador usa GitHub Actions y OpenAI para crear descripciones automáticas en los proyectos de la organización CampusCodeUNED.

## 🚀 ¿Cómo funciona?

1. Cada vez que se haga push en la carpeta `readme-generator`, se ejecutará automáticamente.
2. Busca las carpetas de proyectos dentro del repositorio.
3. Genera un `README.md` usando inteligencia artificial.

## 🔐 API KEY

Agrega tu clave de OpenAI como secreto:
- Ve a **Settings > Secrets > Actions**
- Crea un nuevo secreto llamado `OPENAI_API_KEY`

## 🧠 Modelo usado

Usa el modelo `gpt-4` para generar los archivos de documentación.

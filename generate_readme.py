import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

for folder in os.listdir('.'):
    if os.path.isdir(folder) and folder != "readme-generator" and not folder.startswith('.'):
        prompt = f"Genera un README.md descriptivo y profesional para un proyecto con esta carpeta: {folder}. Está en una organización educativa llamada CampusCodeUNED."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un generador de documentación para repositorios de GitHub educativos."},
                {"role": "user", "content": prompt}
            ]
        )

        readme_path = os.path.join(folder, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(response.choices[0].message.content)

        print(f"README.md generado para {folder}")

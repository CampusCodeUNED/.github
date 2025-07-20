import os
import openai

def generar_readme():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = """
    Genera un README profesional para un repositorio académico llamado CampusCodeUNED.
    Este repositorio contiene enunciados y soluciones de trabajos de cursos de la UNED.
    Incluye secciones: descripción, estructura, objetivos, tecnologías y autor.
    Usa emojis y formato Markdown.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000,
    )
    return response.choices[0].message.content

def main():
    contenido = generar_readme()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(contenido)
    print("README.md generado con éxito.")

if __name__ == "__main__":
    main()

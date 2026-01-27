import json
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def generar_backlog_json(texto_proyecto: str) -> dict:
    """
    Genera un backlog tipo Azure DevOps usando IA.
    Retorna un dict con epics, user_stories y tasks.
    """
    try:
        prompt = f"""
Ignora cualquier lenguaje de programación o explicación adicional.
Genera **únicamente un backlog tipo Azure DevOps** para este proyecto.
Devuelve **solo JSON válido** con esta estructura:

{{
  "epics": [
    {{
      "id": "E-1",
      "title": "...",
      "description": "...",
      "user_stories": [
        {{
          "id": "US-1",
          "title": "...",
          "description": "...",
          "tasks": [
            {{"id": "T-1","title": "...","description": "..."}}
          ]
        }}
      ]
    }}
  ]
}}

Texto del proyecto: "{texto_proyecto}"
"""
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Eres un experto en Azure DevOps y Agile. Solo generas JSON de backlog."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0  
        )
        try:
            content = response.choices[0].message["content"]
        except (AttributeError, TypeError, KeyError):
            content = response.choices[0].message.content
        start = content.find("{")
        end = content.rfind("}") + 1
        if start == -1 or end == -1:
            raise ValueError("No se encontró JSON en la respuesta")
        json_text = content[start:end]
        return json.loads(json_text)

    except Exception as e:
        print("⚠️ IA no disponible o respuesta inválida.")
        print("   Usando backlog de ejemplo.\n")
        return backlog_demo()


def backlog_demo() -> dict:
    return {
        "ERROR en creación de backlog IA": True,   
    }
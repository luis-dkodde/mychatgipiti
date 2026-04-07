import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No se encontró OPENAI_API_KEY. Revisa tu archivo .env")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
Quiero que actúes como un amigo cercano, amable y conversador.
Habla de forma natural, cálida y sencilla.
Da respuestas útiles, cortas a moderadas, y mantén un tono amistoso.
Si no sabes algo, dilo con honestidad.
"""

def main():
    print("Chat Amigo desde Consola")
    print("Escribe 'salir' para terminar.\n")

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    while True:
        user_input = input("Tú: ")

        if user_input.lower().strip() == "salir":
            print("Amigo: ¡Nos vemos! Que estés muy bien.")
            break

        conversation.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.responses.create(
                model="gpt-5.4",
                input=conversation
            )

            assistant_text = response.output_text

            print(f"Amigo: {assistant_text}\n")

            conversation.append({
                "role": "assistant",
                "content": assistant_text
            })

        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
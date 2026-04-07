import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable OPENAI_API_KEY en el archivo .env")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
Actúa como un amigo cercano, amable, conversador y respetuoso.
Responde de manera natural, cálida y sencilla.
Mantén un tono humano y agradable.
Responde en el mismo idioma del usuario.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "No recibí ningún mensaje."}), 400

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )

        return jsonify({"reply": response.output_text})

    except Exception as e:
        return jsonify({"reply": f"Ocurrió un error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
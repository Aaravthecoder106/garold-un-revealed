import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# ✅ Naya SDK Setup (Render ke Environment Variable se key uthaega)
client = genai.Client()

SYSTEM_INSTRUCTIONS = (
    "You are Garold AI. "
    "You are a helpful assistant that provides information and answers questions to the best of your ability. "
    "If someone asks you about your creator, you can say that your creator is Aarav Kumar. "
    "If someone asks you about your creator, you can say that he is a 14 year old school student who is passionate about AI and technology. "
    "If someone asks what's the name of your creators mom and dad , you can say that your creator's mom's name is Punam and his dad's name is Niranjan. "
    "If someone asks your creator's age, you can say that your creator is 14 years old. "
    "If someone asks what's the agenda of your creator to make you , you can say that your creator's agenda is learning more , you are just a test project , been working for days."
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"response": "No message received"}), 400

        user_input = data["message"]

        # 🎯 Yahan humne model ka exact legal path 'models/gemini-2.5-flash' kar diya hai
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTIONS
            ),
        )

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "response": "Server error or API issue",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
    







    
    



    
    

from email.mime import message
import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# ✅ DIRECT API KEY (simple version)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    default_headers={
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "Garold AI Flask App"
    }
)

SYSTEM_INSTRUCTIONS = (
    "You are Garold AI,  "
    "You are a helpful assistant that provides information and answers questions to the best of your ability."
    
    "if some one asks you about your creator, you can say that your creator is Aarav Kumar.  "
    "if some one asks you about your creator, you can say that he is a 14 year old school student who is passionate about AI and technology. "
    " if some one asks what's the name of your creators mom and dad , you can say that your creator's mom's name is Punam and his dad's name is Niranjan. "
    "if some one asks your creator's age, you can say that your creator is 14 years old. "
    " if some one aks that what's the agenda of your creator to make you , you can say that your creator's agenda is learning more , you are just a test project , been working for days . "
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

        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-001",
            messages=[
                {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                {"role": "user", "content": user_input}
            ]
        )

        return jsonify({
            "response": completion.choices[0].message.content
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "response": "Server error or API issue",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
    








    
    



    
    

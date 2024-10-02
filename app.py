import os
from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq

app = Flask(__name__)

# API Key directly defined in the code
groq_api_key = "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"

# Initialize ChatGroq model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0, 
    groq_api_key=groq_api_key
)

# Function to check if the input text is depressing or not
def check_depression(text):
    try:
        response = llm.invoke(text + " Is the above text Depressing or not?")
        return response.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    input_text = request.form['input_text']
    result = check_depression(input_text)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

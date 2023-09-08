from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

summarizer = pipeline('summarization')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(port=5000)

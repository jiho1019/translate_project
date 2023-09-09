from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import googletrans

app = Flask(__name__)

CORS(app)

translator = googletrans.Translator()

@app.route('/')
def index(methods=['GET', 'POST']):
    return "hello"

@app.route('/main')
def main(methods=['GET', 'POST']):
    return "main"
    
@app.route('/trans_ko', methods=['GET', 'POST'])
def trans__ko():
    text = request.form['text']
    dest = request.form['dest']
    lang = request.form['lang']
    
    res = translator.translate(text,dest=dest)
    return jsonify({'text': f"{res.text}", 'lang': lang})

@app.route('/trans_en', methods=['GET', 'POST'])
def trans__en():
    
    text = request.form['text']
    dest = request.form['dest']
    lang = request.form['lang']
    res = translator.translate(text,dest=dest)
    return jsonify({'text': f"{res.text}", 'lang': lang})

@app.route('/trans_ja', methods=['GET', 'POST'])
def trans__ja():
    
    text = request.form['text']
    dest = request.form['dest']
    lang = request.form['lang']
    res = translator.translate(text,dest=dest)
    return jsonify({'text': f"{res.text}", 'lang': lang})
    
if __name__ == '__main__':
    app.run(debug=True)

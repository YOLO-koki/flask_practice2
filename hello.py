from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)

bullets = [
    '箇条書き１',
    '箇条書き2',
    '箇条書き3',
    '箇条書き4',
    '箇条書き5',
    '箇条書き6',
    '箇条書き7',
]

@app.route('/<city>')
def hello(city):
    
    return render_template('hello.html', name_bullets=bullets, name_city=city)
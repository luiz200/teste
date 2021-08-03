from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_index():
    g1 = requests.get('https://g1.globo.com/')
    index1json = g1.json()
    index1s = {
        'feed-post-body-title gui-color-primary gui-color-hover ' : index1json[0]['feed-post-body-title gui-color-primary gui-color-hover '],
        'feed-post-body-resumo': index1json[0]['feed-post-body-resumo']
    }
    ge = requests.get('https://ge.globo.com/')
    index2json = ge.json()
    index2s = {
        'feed-post-link gui-color-primary gui-color-hover' : index2json[0]['feed-post-link gui-color-primary gui-color-hover'],
        'feed-post-body-resumo' : index2json[0]['feed-post-body-resumo']
    }
    return render_template('index.html', index1s=index1s, index2s=index2s)
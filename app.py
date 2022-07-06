from flask import Flask, jsonify

import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>API is online, you can check the documentation:</h1>'


@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('data_apicsv.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

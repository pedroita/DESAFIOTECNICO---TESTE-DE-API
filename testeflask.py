from flask import Flask, jsonify

import pandas as pd

app = Flask(__name__)



@app.route("/todosdados")
def todas_operadoras():
   

    try:
        df = pd.read_csv("operadoras.csv", encoding="latin1", sep=';', on_bad_lines='skip')

    except pd.errors.ParserError as e:
        return jsonify({"error": f"Erro de análise: {e}"})

    
    result_dict = df.to_dict(orient='records')
    
    return jsonify(result_dict)

@app.route("/registroans/<termo>")
def buscar_registrosans(termo):

    try:
         df = pd.read_csv("operadoras.csv", encoding="latin1", sep=';', on_bad_lines='skip')
    except pd.errors.ParserError as e:
        return jsonify({"error": f"Erro de análise: {e}"}), 500

    resultados_encontrados = df[df['Registro_ANS'].astype(str).str.contains(termo, case=False)]
    if resultados_encontrados.empty:
        return jsonify({"message": "Dado não encontrado"}), 404
    resultados_dict = resultados_encontrados.to_dict(orient='records')
    
    return jsonify({"resultados": resultados_dict})

@app.route("/buscarporcnpj/<termo>")
def buscar_cnpj(termo):

    try:
        df = pd.read_csv("operadoras.csv", encoding="latin1", sep=';', on_bad_lines='skip')
    except pd.errors.ParserError as e:
        return jsonify({"error": f"Erro de análise: {e}"}), 500

    resultados_encontrados = df[df['CNPJ'].astype(str).str.contains(termo, case=False)]
    if resultados_encontrados.empty:
        return jsonify({"message": "Dado não encontrado"}), 404
    resultados_dict = resultados_encontrados.to_dict(orient='records')

    return jsonify({"resultados": resultados_dict})


@app.route("/nomefantasia/<termo>")
def buscar_nomefantasia(termo):

    try:
        df = pd.read_csv("operadoras.csv", encoding="latin1", sep=';', on_bad_lines='skip')

    except pd.errors.ParserError as e:
        return jsonify({"error": f"Erro de análise: {e}"}), 500

    resultados_encontrados = df[df['Nome_Fantasia'].astype(str).str.contains(termo, case=False)]
    if resultados_encontrados.empty:
        return jsonify({"message": "Dado não encontrado"}), 404
    resultados_dict = resultados_encontrados.to_dict(orient='records')

    return jsonify({"resultados": resultados_dict})


if __name__ == "__main__":  
    app.run(debug=True)

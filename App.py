from flask import Flask, jsonify
from control.NotaController import NotaController

app = Flask("API Nota")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint GET: /notas/media/<float:nota1>/<float:nota2>
@app.route('/notas/media/<float:nota1>/<float:nota2>', methods=['GET'])
def get_media_notas(nota1, nota2):
    try:
        notaController = NotaController()
        notaController.nota_converter.nota1 = nota1
        notaController.nota_converter.nota2 = nota2

        media = notaController.calcular_media()

        jsonResposta = {
            "nota1": nota1,
            "nota2": nota2,
            "media": media
        }
        return jsonify(jsonResposta), 200
    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

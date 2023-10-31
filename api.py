from flask import Flask, request, jsonify

app = Flask(__name__)

cidades = [
    {
        'id': 1,
        'nome': 'Houston',
        'prefeito': 'Sylvester Turner (D)',
    },
    {
        'id': 2,
        'nome': 'Chicago',
        'prefeito': 'Brandon Johnson',
    },
    {
        'id': 3,
        'nome': 'Los angeles',
        'prefeito': 'Karen Bass',
    },

]

@app.route('/cidades', methods=['GET'])
def obter_cidades():
   return jsonify(cidades)


@app.route('/cidades/<int:id>',methods=['GET'])
def obter_cidades_por_id(id):
   for cidades in cidades:
     if cidades.get('id')  == id:
        return jsonify(cidades)
     
     @app.route('/cidades/<int:id>', methods=['PUT'])
     def editar_cidades_por_id(id):
       cidades_alterada = request.get_json()
       for indice, cidades in enumerate(cidades):
          if cidades.get('id') == id:
             cidades[indice].update(cidades_alterada)
             return jsonify(cidades[indice])
          
@app.route('/cidades',methods=['POST'])          
def incluie_nova_cidade():
   nova_cidade = request.get_json()
   cidades.append(nova_cidade)

   return jsonify(cidades)

@app.route('/cidades/<int:id>', methods=['DELETE'])
def excluir_cidades(id):
   for indice, cidade in enumerate(cidades):
      if cidade.get('id') == id:
         del cidades[indice]

         return jsonify(cidades)

app.run(port=7000,host='localhost',debug=True)
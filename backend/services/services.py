import os
from domain.retirada import Retirada
from domain.estoque import Estoque
from domain.produto import Produto
from domain.entrada import Entrada
from flask_cors import CORS
from flask import Flask, jsonify, request
from domain.doador import Doador
from domain.doacao import Doacao


def main():
    app = Flask(__name__)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['DEBUG'] = True

    @app.route("/", methods=['GET'])
    def index():
        return "Rota de Teste de API"

    # Rotas para produtos---------------------------------------

    @app.route('/api/v1/produto/listar', methods=['GET'])
    def listarProdutos():
        result = Produto()
        return result.listarProdutos()

    @app.route('/api/v1/produto/cadastro', methods=['POST'])
    def cadastroProduto():
        dados = request.get_json()
        id = 0
        nome = dados['nomeproduto']
        cad = Produto(id, nome)
        cad.cadastroProduto()
        return "cadastrado com sucesso"

    # Rotas para doador ------------------------------------------

    @app.route('/api/v1/doador/listar', methods=['GET'])
    def listarDoador():
        result = Doador()
        return result.listarDoador()

    @app.route('/api/v1/doador/cadastro', methods=['POST'])
    def cadastroDoador():
        dados = request.get_json()
        produto = dados['idproduto']
        doador = dados['iddoador']
        qtde = dados['quantidade']
        datadoacao = dados['datadoacao']
        cad = Doacao(produto, doador, qtde, datadoacao)
        cad.cadastroDoacao()
        return "teste"

    # Rotas para doacao ------------------------------------------

    @app.route('/api/v1/doacao/listar', methods=['GET'])
    def listarDoacao():
        result = Doacao()
        return result.listarDoacao()

    @app.route('/api/v1/doacao/cadastro', methods=['POST'])
    def cadastroDoacao():
        dados = request.get_json()
        idproduto = dados['idproduto']
        iddoador = dados['iddoador']
        quantidade = dados['quantidade']
        cad = Doacao(idproduto, iddoador, quantidade)
        cad.cadastroDoacao()
        return jsonify(rs={"resultado": "Cadastro realizados com sucesso"})

    @app.route('/api/v1/doacao/totaldoadoinicio', methods=['GET'])
    def totalDoacaoInicio():
        result = Doacao()
        return result.totalDoacaoInicio()

    @app.route('/api/v1/doacao/totaldoado24', methods=['GET'])
    def totalDoacao24():
        result = Doacao()
        return result.totalDoacao24()
# Rotas para Entrada ------------------------------------------

    @app.route('/api/v1/entrada/listar', methods=['GET'])
    def listarEntrada():
        result = Entrada()
        return result.listarEntrada()

    @app.route('/api/v1/entrada/cadastro', methods=['POST'])
    def cadastroEntrada():
        dados = request.get_json()
        idproduto = dados['idproduto']
        datavalidade = dados['datavalidade']
        quantidade = dados['quantidade']
        cad = Entrada(idproduto, datavalidade)
        rs = cad.cadastroEntrada()
        print("codigo entrada -> %d", rs)
        est = Estoque(rs, quantidade)
        est.cadastroEstoque()
        return jsonify(rs={"resultado": "Cadastro realizado"})

    # Rotas para Estoque ------------------------------------------

    @app.route('/api/v1/estoque/listar', methods=['GET'])
    def listarEstoque():
        result = Estoque()
        return result.listarEstoque()

    @app.route('/api/v1/estoque/listarprodutoestoque', methods=['GET'])
    def listarProdutoEstoque():
        result = Estoque()
        return result.listarProdutoEstoque()

    @app.route('/api/v1/estoque/cadastro', methods=['POST'])
    def cadastroEstoque():
        dados = request.get_json()
        identrada = dados['identrada']
        quantidade = dados['quantidade']
        cad = Estoque(identrada, quantidade)
        cad.cadastroEstoque()
        return jsonify(rs={"resultado": "Cadastro realizados com sucesso"})

    # Rotas para Retirada ------------------------------------------

    @app.route('/api/v1/retirada/listar', methods=['GET'])
    def listarRetirada():
        result = Retirada()
        return result.listarRetirada()

    @app.route('/api/v1/retirada/cadastro', methods=['POST'])
    def cadastroRetirada():
        dados = request.get_json()
        idproduto = dados['idproduto']
        quantidade = dados['quantidade']
        cad = Retirada(idproduto, quantidade)
        cad.cadastroRetirada()
        return jsonify(rs={"resultado": "Cadastro realizados com sucesso"})

    @app.route('/api/v1/retirada/totaldoadoinicio', methods=['GET'])
    def totalRetiradaInicio():
        result = Retirada()
        return result.totalRetiradaInicio()

    @app.route('/api/v1/retirada/totaldoado24', methods=['GET'])
    def totalRetirada24():
        result = Retirada()
        return result.totalRetirada24()

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)

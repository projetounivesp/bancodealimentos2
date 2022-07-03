from flask import jsonify
import json
import traceback

import pymysql


class Produto:
    def __init__(self, idproduto=None, nomeproduto=None):
        self.idproduto = idproduto
        self.nomeproduto = nomeproduto

        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='bancoalimentos',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroProduto(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `produto`(`nomeproduto`)VALUES(%s)"
                cur.execute(sql, (self.nomeproduto))
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarProdutos(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM produto")
                result = cur.fetchall()
                return jsonify(result)

        except:
            print("Erro ao tentar cadastrar os dados")
        finally:
            self.conn.close()

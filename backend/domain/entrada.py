from flask.json import jsonify
import traceback

import pymysql


class Entrada:
    def __init__(self, idproduto=None, datavalidade=None):
        self.idproduto = idproduto
        self.datavalidade = datavalidade

        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='bancoalimentos',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroEntrada(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `entrada` (`idproduto`, `datavalidade`)VALUES(%s, %s)"
                cur.execute(sql, (self.idproduto, self.datavalidade))
                self.conn.commit()
                entrada_id = cur.lastrowid
                return entrada_id
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarEntrada(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM entrada")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar listar doacoes")
        finally:
            self.conn.close()

from flask.json import jsonify
import traceback

import pymysql


class Doador:
    def __init__(self, iddoador=None, bloco_apartamento=None):
        self.iddoador = iddoador
        self.bloco_apartamento = bloco_apartamento

        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='bancoalimentos',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroDoador(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `doador`(`bloco_apartamento`)VALUES(%s)"
                cur.execute(sql, (self.bloco_apartamento))
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarDoador(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM doador")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar listar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

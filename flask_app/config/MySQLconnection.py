import pymysql

class MySQLconnection:
    def __init__(self,db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
    def query_db(self,query, data=None):
        cursor = self.connection.cursor()
        try:
            resultado = cursor.execute(query, data)

            # Si estamos consultando información
            if query.strip().lower().startswith("select"):
                resultado = cursor.fetchall()

            # Si estamos modificando información
            else:
                self.connection.commit()
            return resultado
        except Exception as error:
            print("Error MySQL:", error)
            return False

        finally:
            cursor.close()
            self.connection.close()


def connectToMySQL(db):
    return MySQLconnection(db)
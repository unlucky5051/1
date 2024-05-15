from dist.Config.config import connection

class Model:
    def get(self,table):
        with connection().cursor() as cursor:
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()
    def getOne(self,table,field):
        with connection().cursor() as cur:
            query = (f"SELECT * FROM {table} WHERE id = {field}")
            cur.execute(query)
            return cur.fetchall()
        connection().close()

from MySQLconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM usuarios;"
        
        resultados_query=connectToMySQL('usuarios_crud').query_db(query)

        lista_usuarios=[]

        for elemento in resultados_query:
            lista_usuarios.append(cls(elemento))

        return lista_usuarios

    
    @classmethod
    def save(cls, datos):

        query="INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"

        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {
            "id":id
        }
        resultado = connectToMySQL("usuarios_crud").query_db(query,datos)
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
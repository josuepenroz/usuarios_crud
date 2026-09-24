from flask import Flask, render_template,redirect,url_for
from usuario import Usuario
from flask import request
app =  Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/usuarios")
def Usuarios():
    usuarios = Usuario.get_all()

    
    
    return render_template("index.html", usuarios=usuarios)


@app.route("/usuarios/nuevo", methods=["GET","POST"])
def nuevo_usuario():
    
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "apellido": request.form["apellido"],
            "email": request.form["email"],
        }
        resultado = Usuario.save(datos)
        print("Resultado gura",resultado)
       
        return redirect(url_for("Usuarios"))
    return render_template("nuevo.html")

@app.route("/usuarios/<int:usuario_id>")
def ver_usuario(usuario_id):
    usuario = Usuario.get_one(usuario_id)
    return render_template("ver.html", usuario=usuario)
@app.route("/usuarios/editar/<int:usuario_id>",methods=["GET","POST"] )
def editar(editar_id):
    if request.method =="GET":
        usuario = Usuario.get_one(usuario_id)
        
        return render_template(
            "editar.html",
            usuario=usuario
        )


if __name__ == "__main__":
    app.run(debug=True) 
from flask import Flask, render_template
from usuario import Usuario
app =  Flask(__name__)


@app.route("/usuarios")
def Usuarios():
    usuarios = Usuario.get_all()
    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    correo = request.form["correo"].strip().lower()
    
    
    
    return render_template("index.html", usuarios=usuarios)


@app.route("/usuarios/nombre/<nuevo>")

@app.route(
    "/gestion/libros/<int:libro_id>/eliminar",
    methods=["POST"]
)

def borrar(usuario_id):

    resultado = Libro.eliminar(
        libro_id
    )

    if resultado is False:

        flash(
            "No se pudo eliminar el libro."
        )

    elif resultado == 0:

        flash(
            "El libro no existe."
        )

    else:

        flash(
            "Libro eliminado correctamente."
        )

    return redirect(
        url_for("gestion_libros")
    )


if __name__ == "__main__":
    app.run(debug=True)
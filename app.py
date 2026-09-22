from flask import Flask, render_template

app =  Flask(NAME)


@app.route("/Usuarios")
def Usuarios():
    return render_template("index.html")

@app.route("/Usuarios/nombre/<nuevo>")

def crear():
    return render_template("index.html")

@app.route("/Usuarios")
def Usuarios():
    return render_template("index.html")

@app.route("/Usuarios")
def Usuarios():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
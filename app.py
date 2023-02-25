from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def products_page():
    return render_template("index.html")

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)
from flask import Flask, request, Response, render_template


app = Flask(__name__)

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/info", methods=['GET'])
def info():
    return render_template("info.html")

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route("/upload", methods=['GET'])
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

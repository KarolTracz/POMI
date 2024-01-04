from flask import Flask, render_template, request

app = Flask(__name__)

l = []

@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Hello world!</h1>"

@app.route("/summoner", methods=["POST"])
def summoner():
    name = request.form.get("name")
    server = request.form.get("server")
    l.append(name)
    l.append(server)
    print(l)
    return render_template("summoner.html")

if __name__ == '__main__':
    app.run(port=80)

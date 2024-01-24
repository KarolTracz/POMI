from flask import Flask, render_template, request, redirect, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from logic import main
from extensions import db
from models import SignIn

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# app.config['SQLALCHEMY_BINDS'] = {
#     'app': 'sqlite:///app.db',
#     'MatchHistory': 'sqlite:///MatchHistory.db'
# }
app.config["JWT_SECRET_KEY"] = "asjdaskjdajsjdksajjdksajkdas"
jwt = JWTManager(app)
db.init_app(app)
with app.app_context():
    db.create_all()



# strona glowna
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        dbname = SignIn.query.filter_by(name=name, password=password).first()
        if dbname:
            if dbname.name == name and dbname.password == password:
                access_token = create_access_token(identity=dbname.name)
                return redirect('/search')
        else:
            return render_template("index.html")
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        summoner = request.form['summoner']
        server = request.form['server']
        match_history_records = main(summoner, server)
        for record in match_history_records:
            db.session.add(record)
        db.session.commit()

        return render_template("summonerName.html", summoner=summoner)
    return render_template("search.html")


@app.route('/summonerName')
def summonerName():
    return render_template("summonerName.html")


# rejestracja
@app.route('/register', methods=['GET', 'POST'])
def register():
    # db.create_all()
    if request.method == 'POST':
        signin = SignIn(name=request.form['username'], email=request.form['email'], password=request.form['password'])
        db.session.add(signin)
        db.session.commit()

    signins = SignIn.query.all()
    return render_template("register.html", signins=signins)



if __name__ == "__main__":
    app.run()

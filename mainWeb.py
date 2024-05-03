from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO

DATABASE = "/tmp/shop.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5b58cdc7451ba0e17f71d6a79ca9f613ae13a6f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)


@app.route('/about', methods=['GET', "POST"])
def about():
    if request.method == 'POST':
        file = request.files['file']

        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()

        return f'Uploaded: {file.filename}'
    return render_template('about.html')


@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), as_attachment=True)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title


@app.route("/")
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template("index.html", data=items)


@app.route("/reg", methods=["POST", "GET"])
def reg_hand():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        dan = Account(login=login, password=password)
        try:
            db.session.add(dan)
            db.session.commit()
            return redirect("/")
        except:
            return "ошибка"
    else:
        return render_template("log_reg.html")


@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        price = request.form["price"]
        item = Item(title=title, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect("/")
        except:
            return "Ошибка"
    else:
        return render_template("create.html")


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)

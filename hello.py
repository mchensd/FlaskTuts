from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

grades = {"Chem": "A", "Math":"A", "WH": "B"}

class NameForm(Form):
    name = StringField("What is your name?", validators = [Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow(), deadline_time=datetime(2016,12,26))

@app.route('/user/<name>')
def user(name):
    
    return render_template('user.html', name=name, grades=grades)

@app.route('/hellouser/<user>')
def hello_user(user):
    return render_template('hellouser.html', name=user)

@app.route('/redirme')
def redirme():
    return redirect("youtube.com")

@app.route('/cookieresp')
def cookieresp():
    response = make_response("<h1>This has a cookie!</h1>")
    response.set_cookie('answer', '42')
    return response

@app.route('/fancyuser')
def fancyuser():
    return render_template("fancyuser.html", name="michael")

@app.route('/base')
def base():
    return render_template("base.html")
@app.errorhandler(404)
def page_404(e):
    return render_template("404.html"), 404
if __name__ == '__main__':
    manager.run()

    

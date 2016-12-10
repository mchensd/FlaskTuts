from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
class nameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    pw = PasswordField("Enter your password", validators=[Required()])
    submit = SubmitField("Submit")

@app.route("/", methods=['GET', 'POST'])
def index():
    # We will store name/pw in the session dict
    #name=None
    #pw=None
    form = nameForm()

    if form.validate_on_submit():  # if validators are met
        old_name = session.get('name')
        old_pw = session.get('pw')

        if old_name is not None and old_pw is not None:
            if old_name != form.name.data:
                flash("It looks like you have changed your name!")
            if old_pw != form.name.data:
                flash("Successfully changed password!")
        session['name'] = form.name.data
        session['pw'] = form.pw.data
        return redirect(url_for('index'))  # A get request so refresh will work as expected
        # We use session to store name/pw
        #name=form.name.data
        #pw = form.pw.data
        #form.name.data=''
        #form.pw.data=''

    return render_template("index.html", name=session.get('name'),form=form, pw=session.get('pw'), session=session)


if __name__ == "__main__":
    manager.run()
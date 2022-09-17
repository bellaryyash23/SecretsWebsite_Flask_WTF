from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField("E-mail", validators=[Email(message="Invalid email address"),
                                              DataRequired(message="This field is required.")])
    password = PasswordField("Password", validators=[Length(min=8, message="Password must be least 8 characters long"),
                                                     DataRequired(message="This field is required.")])
    submit = SubmitField("Login")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "Some secret string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

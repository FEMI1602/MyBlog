from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app= Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='195105ee931397613b0e58683278bcd1'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username
post=[
    {
        'author':'Amish Tripathi',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'2018 April 10'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'2018 April 13'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',post=post)


@app.route("/about")
def about():
    return render_template('about.html',title='About Page title')

@app.route("/register",methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesssful. Please check username and password','danger')
    return render_template('login.html',title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
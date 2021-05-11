from flask import Flask, render_template, url_for
app= Flask(__name__,template_folder='template')

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


if __name__=='__main__':
    app.run(debug=True)
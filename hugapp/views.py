from flask import render_template
from hugapp import app

@app.route('/')
@app.route('/index')
def index():
    postNum, body = 1, "" # lol this is a bad way to do this??????
    posts = [ # fake array of posts
        {
            postNum: 1,
            body: "I am less alone because of this fake site"
        },
        {
            postNum: 2,
            body: "I need a new kitty"
        },
        {
            postNum: 3,
            body: "Third thing"
        }
    ]
    return render_template('index.html',
                            title='Hughughome',
                            posts=posts)

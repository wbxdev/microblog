from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Edgar'}
    posts = [
        {
            'author':{'username': 'Dwight'},
            'body': "It was bigger than a snake"
        },
        {
            'author': {'username': 'Michael Scott'},
            'body': "That's what she said"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
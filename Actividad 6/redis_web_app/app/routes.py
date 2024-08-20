from flask import render_template, request, redirect, url_for
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def configure_routes(app):

    @app.route('/')
    def index():
        # Suponiendo que queremos mostrar algunos datos de Redis
        data = r.get('some_key')
        return render_template('index.html', data=data)

    @app.route('/add', methods=['POST'])
    def add_data():
        data = request.form['data']
        r.set('some_key', data)
        return redirect(url_for('index'))
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
from flask.cli import FlaskGroup

app = Flask(__name__)
app.config['DATABASE'] = 'flashcards.db'
app.config['SELECT_KEY'] = 'VVF'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    flashcards = query_db('SELECT * FROM flashcards;')
    return render_template('AddVocabPage.html', flashcards=flashcards)

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    frontside = request.form['frontside']
    backside = request.form['backside']
    link = request.form['link']

    db = get_db()
    db.execute('INSERT INTO flashcards (frontside, backside, link) VALUES (?,?,?);')
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    @app.cli.command('init-db')
    def init_db_command():
        """Initialize the database."""
        init_db()
        print('Initialized the database.')

    FlaskGroup(app).run()

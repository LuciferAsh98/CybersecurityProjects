from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'demo.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return '''
    <form method="GET" action="/search">
        Search for user: <input type="text" name="username">
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search')
def search():
    username = request.args.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}")
    cur = get_db().execute(query)
    results = cur.fetchall()
    cur.close()
    return f"Results: {results}"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, session
from flask_cors import CORS
from db import engine, user_table, init_db
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/api/authenticate', methods=['GET'])
def authenticate():
    if 'username' in session:
        return {
            'status': 'success',
            'data': {
                'username': session['username']
            }
        }
    return {
        'status': 'fail'
    }

@app.route('/api/login', methods=['POST'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']

    stmt = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
    with engine.connect() as conn:
        result = conn.execute(stmt).all()
        if len(result) == 0:
            return {
                'status': 'fail',
                'data': 'Wrong information'
            }
        elif len(result) > 1:
            return {
                'status': 'fail',
                'data': {
                    'username': 'Multiple user exist'
                }
            }
        session['username'] = username
    return {
        'status': 'success'
    }

@app.route('/api/join', methods=['POST'])
def join():
    username = request.get_json()['username']
    password = request.get_json()['password']
    
    stmt = insert(user_table).values(username=username, password=password)
    try:
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
    except IntegrityError:
        return {
            'status': 'fail',
            'data': {
                'username': 'Duplicated username'
            }
        }
    return {
        'status': 'success'
    }

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
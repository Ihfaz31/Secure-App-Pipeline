from flask import Flask, request
import sqlite3

app = Flask(__name__)

# This part creates a tiny database in the computer's memory
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.execute('CREATE TABLE users (id INTEGER, username TEXT, password TEXT)')
    conn.execute('INSERT INTO users VALUES (1, "admin", "p@ssword123")')
    return conn

db_conn = init_db()

@app.route('/search')
def search():
    user_id = request.args.get('id')
    
    # --- THE SECURE FIX ---
    # We use a '?' as a placeholder. The data is passed as a separate tuple.
    query = "SELECT username FROM users WHERE id = ?"
    
    # The database engine now treats user_id strictly as data, not code.
    cursor = db_conn.execute(query, (user_id,))
    
    result = cursor.fetchone()
    return f"User found: {result[0]}" if result else "Not found"
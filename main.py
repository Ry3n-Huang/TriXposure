# app.py
from flask import Flask, render_template, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route('/')
def home():
    # initialize a user session or ID if you want
    session.setdefault('user_id', datetime.utcnow().timestamp())
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    # record when the user clicked “Start”
    ts = datetime.utcnow().isoformat()
    # e.g. write to a file or DB: (session['user_id'], 'start', ts)
    print(f"USER {session['user_id']} STARTED LEARNING AT {ts}")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

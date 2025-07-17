from flask import Flask, render_template, jsonify
import secrets
import string

app = Flask(__name__)

def generate_password(length=16):
    allowed_chars = string.ascii_letters + string.digits + "!@#$%^&*-_=+"
    password = ''.join(secrets.choice(allowed_chars) for _ in range(length))
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-password')
def generate():
    return jsonify({'password': generate_password()})

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect
import oracledb

app = Flask(__name__)

# Oracle XE connection
conn = oracledb.connect(
    user="your_username",
    password="your_password",
    dsn="localhost/XE"
)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Insert into Oracle database
    cursor.execute("""
        INSERT INTO portfolio_contacts (name, email, message) 
        VALUES (:1, :2, :3)
    """, (name, email, message))
    conn.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

import oracledb

# Enable thick mode
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_22")  # 👈 path to your Instant Client folder

from flask import Flask, request, render_template_string
import oracledb

# Initialize thick mode
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_22")

app = Flask(__name__)

# Database connection
conn = oracledb.connect(
    user="hr",
    password="your_password_here",   # 🔑 replace this
    dsn="localhost/XE"
)

@app.route('/')
def form():
    return render_template_string('''
        <h2>Portfolio Contact Form</h2>
        <form method="POST" action="/submit">
            Name: <input type="text" name="name" required><br><br>
            Email: <input type="email" name="email" required><br><br>
            Message: <textarea name="message" required></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO portfolio_data (name, email, message)
        VALUES (:1, :2, :3)
    """, (name, email, message))
    conn.commit()
    cur.close()

    return f"<h3>Thanks {name}, your data has been saved!</h3>"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pavankumar@123",
        database="second"
    )

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee2")
    employees = cursor.fetchall()
    conn.close()
    return render_template("index.html", employees=employees)

# ADD EMPLOYEE
@app.route('/add', methods=['POST'])
def add_employee():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employee2
    (Department, Name, Designation, Email, Address,
     Married_status, DOB, DOJ, id_proof_type,
     id_proof, Gender, Phone, Country, Salary)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        request.form['Department'],
        request.form['Name'],
        request.form['Designation'],
        request.form['Email'],
        request.form['Address'],
        request.form['Married_status'],
        request.form['DOB'],
        request.form['DOJ'],
        request.form['id_proof_type'],
        request.form['id_proof'],
        request.form['Gender'],
        request.form['Phone'],
        request.form['Country'],
        request.form['Salary']
    )

    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# UPDATE EMPLOYEE
@app.route('/update', methods=['POST'])
def update_employee():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE employee2 SET
        Department=%s,
        Name=%s,
        Designation=%s,
        Email=%s,
        Address=%s,
        Married_status=%s,
        DOB=%s,
        DOJ=%s,
        id_proof_type=%s,
        Gender=%s,
        Phone=%s,
        Country=%s,
        Salary=%s
    WHERE id_proof=%s
    """

    values = (
        request.form['Department'],
        request.form['Name'],
        request.form['Designation'],
        request.form['Email'],
        request.form['Address'],
        request.form['Married_status'],
        request.form['DOB'],
        request.form['DOJ'],
        request.form['id_proof_type'],
        request.form['Gender'],
        request.form['Phone'],
        request.form['Country'],
        request.form['Salary'],
        request.form['id_proof']
    )

    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# DELETE EMPLOYEE
@app.route('/delete/<id_proof>')
def delete_employee(id_proof):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee2 WHERE id_proof=%s", (id_proof,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
import sqlite3

def create_table():
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()

    CURSOR.execute('''
              CREATE TABLE IF NOT EXISTS Employees (
                   id TEXT PRIMARY KEY, 
                   name TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT)''')
    CONN.commit()
    CONN.close()

def fetch_employees():
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('SELECT * FROM Employees')
    employees = CURSOR.fetchall()
    CONN.close()
    return employees

def insert_employees(id, name, role, gender, status):
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('INSERT INTO Employees (id, name, role, gender,status) VALUES (?,?,?,?,?)',
                   (id, name, role, gender, status))
    CONN.commit()
    CONN.close()

def delete_employee(id):
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('DELETE FROM Employees WHERE id = ?', (id,))
    CONN.commit()
    CONN.close()

def update_employee(new_name, new_role, new_gender, new_status, id):
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('UPDATE Employees SET name = ?, role = ?, gender = ?,status = ? WHERE id = ?',
                  (new_name, new_role, new_gender, new_status, id) )
    
    CONN.commit()
    CONN.close()

def id_exists(id):
    CONN = sqlite3.connect('Employees.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('SELECT COUNT(*) FROM Employees WHERE id = ?',(id,))
    result = CURSOR.fetchone()
    CONN.close()
    return result[0]>0
create_table()




                   
                   

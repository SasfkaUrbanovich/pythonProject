import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect('string.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS String (col_1 TEXT)''')

    conn = sqlite3.connect('numeric.db')
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS Numeric (col_1 INTEGER)''')

    array = ['Word', 2, 'hello']

    for elem in array:
        if isinstance(elem, str):
            cur.execute('''INSERT INTO String(col_1) VALUES(?)''', elem)
            con.commit()
            curr.execute('''INSERT INTO Numeric(col_1) VALUES(?)''', len(elem))
            conn.commit()
        elif isinstance(elem, int):
            if elem / 2 == 0:
                curr.execute('''INSERT INTO Numeric(col_1) VALUES(?)''', elem)
                conn.commit()
            else:
                cur.execute('''INSERT INTO String(col_1) VALUE ('Нечётное')''')
                con.commit()
import sqlite3

def init_db(cursor):
    cursor.executescript('''

    DROP TABLE if exists category;
	DROP TABLE if exists users;

    CREATE TABLE "category" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT
    );
    CREATE TABLE users (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT,
        "type_id" INTEGER,
        "registration_date" TEXT,
        FOREIGN KEY ("type_id") REFERENCES "category"("id")
    );

    INSERT INTO "category" ('name') VALUES
    ('student'),
    ('parent'),
    ('teacher');

    INSERT INTO "users" ('name', 'type_id', 'registration_date') VALUES
    ('Kristina',1,'2020-11-20'),
    ('Alex',1,'2009-09-22'),
    ('Kirill',3,'2000-08-06'),
    ('Marina',2,'2020-08-01');

    ''')



def task1(cursor):
    cursor.execute('SELECT name FROM users ORDER BY registration_date DESC limit 1')
    mas = cursor.fetchall()
    return (mas[0][0])





con = sqlite3.connect('4.db')
cursor = con.cursor()
print(task1(cursor))
con.commit()
con.close()
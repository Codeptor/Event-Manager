import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('college_event_management.db')  # Use a persistent SQLite database file
        print(f'successful connection with sqlite version {sqlite3.version}')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    cur = conn.cursor()

    # users schema
    cur.execute('''CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL);''')

    # events schema
    cur.execute('''CREATE TABLE events (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    location TEXT,
                    start_time DATETIME NOT NULL,
                    end_time DATETIME NOT NULL);''')

    # event_categories schema
    cur.execute('''CREATE TABLE event_categories (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL);''')

    # event_registrations schema
    cur.execute('''CREATE TABLE event_registrations (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    event_id INTEGER NOT NULL,
                    registration_time DATETIME NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (event_id) REFERENCES events (id));''')

    # event_volunteers schema
    cur.execute('''CREATE TABLE event_volunteers (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    event_id INTEGER NOT NULL,
                    volunteer_time DATETIME NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (event_id) REFERENCES events (id));''')

    # sponsors schema
    cur.execute('''CREATE TABLE sponsors (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    contact_email TEXT);''')

    # event_sponsors schema
    cur.execute('''CREATE TABLE event_sponsors (
                    id INTEGER PRIMARY KEY,
                    event_id INTEGER NOT NULL,
                    sponsor_id INTEGER NOT NULL,
                    FOREIGN KEY (event_id) REFERENCES events (id),
                    FOREIGN KEY (sponsor_id) REFERENCES sponsors (id));''')

    conn.commit()

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
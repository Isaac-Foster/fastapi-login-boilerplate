from sqlite3 import connect

db = connect("main.db", check_same_thread=False)

cur = db.cursor()
commit = (lambda: db.commit())

cur.execute("PRAGMA journal_mode=WAL")

cur.executescript(
    """
-- table users --
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,  
    passwd TEXT NOT NULL,  
    name TEXT NOT NULL,  
    email TEXT NOT NULL,
    admin INTEGER DEFAULT 0
);
    """
)


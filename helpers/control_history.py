import sqlite3
import datetime

file_path = "history_ia_sqlite.db"
name_table = "history"


def check_exist(func):
    def wrapper(*arg):
        conn = sqlite3.connect(file_path)
        cur = conn.cursor()
        check = cur.execute("SELECT name FROM sqlite_master")
        data_check = check.fetchone()

        if not data_check:
            cur.execute(f"CREATE TABLE {name_table}(id INTEGER PRIMARY KEY AUTOINCREMENT, created_at, question, data)")
        else:
            if not name_table in data_check:
                cur.execute(
                    f"CREATE TABLE {name_table}(id INTEGER PRIMARY KEY AUTOINCREMENT, created_at, question, data)"
                )

        return func(conn, cur, *arg)

    return wrapper


@check_exist
def write_in_backup(conn: sqlite3.Connection, cur: sqlite3.Cursor, text: str, question: str):
    created_at = datetime.datetime.now().strftime("%d %B %Y - %H:%M%p")
    cur.execute(
        f"INSERT INTO {name_table}(created_at, question, data) VALUES (?,?,?)",
        (created_at, question, text),
    )
    conn.commit()
    conn.close()


@check_exist
def get_all_data(conn: sqlite3.Connection, cur: sqlite3.Cursor):
    result = cur.execute(f"SELECT * FROM {name_table} ORDER BY id DESC")
    result_data = result.fetchall()
    conn.close()
    return result_data


@check_exist
def remove_by_id(conn: sqlite3.Connection, cur: sqlite3.Cursor, id: int):
    cur.execute(f"DELETE FROM {name_table} WHERE id=?", id)
    conn.close()


@check_exist
def remove_all(conn: sqlite3.Connection, cur: sqlite3.Cursor):
    cur.execute(f"DELETE FROM {name_table} WHERE 1")
    conn.commit()
    conn.close()

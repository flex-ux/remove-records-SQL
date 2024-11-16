
import sqlite3

def connect_to_db(db_name):
    """
    Establish a connection to the SQLite database.
    :param db_name: Name of the SQLite database file.
    :return: Connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        print("Connected to database successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def delete_records(conn, table_name, condition):
    """
    Delete records from a specified table based on a condition.
    :param conn: Connection object to the database.
    :param table_name: Name of the table to delete records from.
    :param condition: SQL WHERE clause condition (e.g., "id = 1").
    """
    try:
        cursor = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition};"
        cursor.execute(query)
        conn.commit()
        print(f"Records matching condition '{condition}' deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting records: {e}")

def fetch_records(conn, table_name):
    """
    Fetch and display all records from a specified table.
    :param conn: Connection object to the database.
    :param table_name: Name of the table to fetch records from.
    """
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Current records in the table:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

def close_connection(conn):
    """
    Close the connection to the SQLite database.
    :param conn: Connection object to the database.
    """
    try:
        if conn:
            conn.close()
            print("Connection closed.")
    except sqlite3.Error as e:
        print(f"Error closing connection: {e}")

if __name__ == "__main__":
    # Database and table details
    database_name = "example.db"
    table_name = "users"
    condition_to_delete = "id = 2"  # Example condition: delete where id is 2

    # Workflow
    conn = connect_to_db(database_name)
    if conn:
        print("\nBefore deletion:")
        fetch_records(conn, table_name)
        
        delete_records(conn, table_name, condition_to_delete)
        
        print("\nAfter deletion:")
        fetch_records(conn, table_name)
        
        close_connection(conn)

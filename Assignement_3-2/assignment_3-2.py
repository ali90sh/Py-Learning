import mysql.connector

# MySQL connection configs
DB_HOST = '127.0.0.1'
DB_USER = 'test_user' 
DB_PASSWORD = 'StrongPass123!'
DB_NAME = 'accounts'
TBL_NAME = 'users'
config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'host': DB_HOST,
  'database': DB_NAME,
  'raise_on_warnings': True
}

def is_valid_email(email):
    # example: local@domain.tld
    
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local:
        return False
    # Just alphabet or digits are acceptable
    for ch in local:
        if not (ch.isalpha() or ch.isdigit()):
            if ch == '.':
                continue
            return False

    if domain.count('.') != 1:
        return False
    domain_part, tld = domain.split('.')
    if not domain_part or not tld:
        return False
    if not (domain_part.isalpha() or domain_part.isdigit()):
        return False
    if not tld.isalpha():
        return False
    return True

def is_valid_password(pw):
    # Password must contain just combination of letters and digits 
    has_letter = False
    has_digit = False
    for ch in pw:
        if not ch.isalpha():
            if not ch.isdigit():
                return False
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True
    return has_letter and has_digit

def prompt_email():
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            return email
        print("Invalid email format. Example: example@domain.com")

def prompt_password():
    while True:
        pw = input("Enter your password: ").strip()
        if is_valid_password(pw):
            return pw
        print("Password must contain letters and digits.")

def check_database_existance(connection):
    mycursor = connection.cursor(buffered = True)
    mycursor.execute("SHOW DATABASES")
    
    for db in mycursor:
        if db[0] == DB_NAME:
            return True
    return False

def check_table_exist(connection):
    mycursor = connection.cursor(buffered = True)
    mycursor.execute("SHOW TABLES")
    
    for tbl in mycursor:
        if tbl[0] == TBL_NAME:
            return True
    
    return False

def init_mysql():
    # Choosing db and connect to it
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    # Creating database if not exist
    if not check_database_existance(conn):
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.database = DB_NAME
    # Creating table if not exist
    if not check_table_exist(conn):
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TBL_NAME} (
                username VARCHAR(255) PRIMARY KEY,
                password VARCHAR(255) NOT NULL
            )
        """)
    conn.commit()
    return conn

def main():
    
    conn = init_mysql()
    cursor = conn.cursor()

    email = prompt_email()
    pw = prompt_password()

    # Insert new record
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (email, pw)
    )
    conn.commit()
    conn.close()
    print("User has been saved to the database.")

if __name__ == "__main__":
    while True:
        main()
        choice = input("Please write 'exit' and press Enter to exit the program or press any key to add new data: ")
        if choice.lower() == "exit":
            print("GoodBye")
            break

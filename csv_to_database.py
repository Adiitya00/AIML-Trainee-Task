import sqlite3
import csv

# read data from CSV file
def read_csv_file(csv_file):
    user_list = []
    
    file = open(csv_file, 'r')
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        if len(row) >= 2:
            name = row[0].strip()
            email = row[1].strip()
            
            if name and email:
                user_data = {
                    'name': name,
                    'email': email
                }
                user_list.append(user_data)
    
    file.close()
    return user_list

# create database and table
def create_database():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


# insert users into database
def insert_users_to_database(users):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    for user in users:
        name = user['name']
        email = user['email']
        
        insert_query = "INSERT INTO users (name, email) VALUES (?, ?)"
        cursor.execute(insert_query, (name, email))
    
    connection.commit()
    connection.close()


# display all users from database
def display_users():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    select_query = "SELECT id, name, email FROM users"
    cursor.execute(select_query)
    all_users = cursor.fetchall()
    
    if len(all_users) == 0:
        print("No users found in database")
        connection.close()
        return
    
    print("\nUsers in Database:")
    print("-" * 70)
    print("ID".ljust(5) + "Name".ljust(30) + "Email")
    print("-" * 70)
    
    for user in all_users:
        user_id = user[0]
        name = user[1]
        email = user[2]
        print(str(user_id).ljust(5) + name.ljust(30) + email)
    
    print("-" * 70)
    print("Total users: " + str(len(all_users)))
    print()
    
    connection.close()


def main():
    csv_file = "users.csv"
    print("Reading data from CSV file")
    users = read_csv_file(csv_file)
    print("Found " + str(len(users)) + " users in CSV file")
    
    print("Creating database...")
    create_database()
    
    print("Inserting users into database")
    insert_users_to_database(users)
    print("Users inserted successfully")
    
    print("Displaying users:")
    display_users()


if __name__ == "__main__":
    main()


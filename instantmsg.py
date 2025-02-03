import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password", # enter your password
    database="service"
)

def create_table():
    try:
        mycursor = db.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS message (msg_id VARCHAR(10),\
                         rname VARCHAR(30), sname VARCHAR(30), \
                         rmail VARCHAR(50), smail VARCHAR(50),\
                         msg VARCHAR(450))")
        print("Table created")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_msg():
    mycursor = db.cursor()
    msg_id = input("Enter Message ID: ")
    rname = input("Enter Receiver Name: ")
    sname = input("Enter Sender Name: ")
    rmail = input("Enter Receiver Email: ")
    smail = input("Enter Sender Email: ")
    msg = input("Enter Message: ")
    sql = "INSERT INTO message (msg_id, rname, sname, rmail, smail, msg) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (msg_id, rname, sname, rmail, smail, msg)
    mycursor.execute(sql, val)
    db.commit()
    print(mycursor.rowcount, "Record inserted.")

def search_msg():
    mycursor = db.cursor()
    print("Select the search criteria: ")
    print("1. Message ID:")
    print("2. Name of Sender:")
    print("3. Name of Receiver:")
    print("4. All Details")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s = input("Enter Message ID: ")
        mycursor.execute("SELECT * FROM message WHERE msg_id = %s", (s,))
    elif choice == 2:
        sn = input("Enter Sender Name: ")
        mycursor.execute("SELECT * FROM message WHERE sname = %s", (sn,))
    elif choice == 3:
        rn = input("Enter Receiver Name: ")
        mycursor.execute("SELECT * FROM message WHERE rname = %s", (rn,))
    elif choice == 4:
        mycursor.execute("SELECT * FROM message")
    else:
        print("Invalid choice")
        return

    myresult = mycursor.fetchall()
    if not myresult:
        print("No record found")
    else:
        for x in myresult:
            print(x)

def delete_msg():
    mycursor = db.cursor()
    ms = input("Enter the message ID to be deleted: ")
    sql = "DELETE FROM message WHERE msg_id = %s"
    mycursor.execute(sql, (ms,))
    db.commit()
    print(mycursor.rowcount, "record(s) deleted")

def Main_Menu():
    while True:
        print("Enter 1: To add new message")
        print("Enter 2: To search message")
        print("Enter 3: To delete message")
        print("Enter 0: To exit")
        try:
            userInput = int(input("Please Select an above option: "))
            if userInput == 1:
                add_msg()
            elif userInput == 2:
                search_msg()
            elif userInput == 3:
                delete_msg()
            elif userInput == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid Input")

if __name__ == "__main__":
    create_table()
    Main_Menu()

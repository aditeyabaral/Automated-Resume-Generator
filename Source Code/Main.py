import Dependencies
import ResumeGenerator
import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;'
                      'MARS_Connection = YES;')

def activity(memberID):
    while(1):
        print("\nWhat would you like to do today?\n\n1. View Details\n2. Edit Details\n3. Generate Resume\n4. Log Out\n")
        choice = int(input("Enter choice: "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Try again.\n")
        else:
            print()
            if choice == 1:
                Dependencies.displayDetails(memberID)
            elif choice == 2:
                Dependencies.editDetails(memberID)
                pass
            elif choice == 3:
                values = Dependencies.clientInfo(memberID)
                resume_values = Dependencies.structureDetails(values)
                ResumeGenerator.create_resume(resume_values)
            else:
                return

def run():
    while(1):
        print("1. Register\n2. Log In\n3. Exit")
        choice = int(input("Enter choice: "))
        if choice not in [1, 2, 3]:
            print("Invalid choice! Try again.\n")
        else:
            print()
            if choice == 1:
                memberID = Dependencies.registerAccount()
                print("Successfully registered!\n")
                activity(memberID)
            elif choice == 2:
                memberID = input("Enter member ID: ")
                password = input("Enter password: ")
                print()
                cur = connection.cursor()
                check_login = cur.execute("SELECT NAME FROM MEMBER WHERE MEMBER_ID = ? AND PASSWORD = ?", (memberID, password)).fetchall()
                cur.close()
                if not check_login:
                    print("Error! Member does not exist!\n")
                else:
                    print("You have logged in!")
                    activity(memberID)
            else:
                break
                

if __name__ == "__main__":
    run()
    connection.close()
import json
import re
import time
users = {
    'admin': {
        'password': 'Password@1','group':'admin'
        }
}
b={
    'To Kill a Mockingbird':{
        'Name': 'To Kill a Mockingbird','Author':'Harper Lee','Copies': '2','Id': 'BK1'
        },
    'Pride and Prejudice':{
        'Name': 'Pride and Prejudice', 'Author': 'Jane Austen','Copies': '2','Id':'BK2'
        },
    'The Jungle book':{
        'Name':'The Jungle book','Author':'Rudyard Kipling','Copies':'2','Id':'BK3'
        }
}
s={
    'Saswati':{
        'Name':'Saswati','SIC':'180310427','Phone no.':9437989565,'Mail id':'saswati@gmail.com'
        }
}

book=json.dumps(b)
student=json.dumps(s)

class Admin:
    def add_books(self):
        while True:
            name = input('Enter the name of the new book: ')
            if not len(name) > 0:
                print('Name cannot be blank')
                continue
            else:
                break
        while True:
            auth = input('Enter the author of the book: ')
            if not len(auth) > 0:
                print('Author cannot be blank')
                continue
            else:
                break
        while True:
            copies = input('Enter the no of copies of the book: ')
            if not len(copies) > 0:
                print('No of copies cannot be blank')
                continue
            else:
                break
        while True:
            Id = input('Enter the book id: ')
            if not len(Id) > 0:
                print('Id cannot be blank')
                continue
            else:
                break        
        b[name] = {}
        b[name]['Name'] = name
        b[name]['Author'] = auth
        b[name]['Copies'] = copies
        b[name]['Id'] = Id
        print('The book has been added')     
    def delete_books(self):
        name=input('Enter the name of the book you want to delete: ')
        del b[name]
    def add_students(self):
        while True:
            name = input('Enter the name of the new student: ')
            if not len(name) > 0:
                print('Name cannot be blank')
                continue
            else:
                break
        while True:
            sic = input('Enter the SIC of the student: ')
            if (int(sic) > 0) and (int(sic) < 9):
                continue
            else:
                break
        while True:
            phone=input('Enter phone no: ')
            def isValid(phone):
                pattern=re.compile('(0/91)?[6-9][0-9]{9}')
                return pattern.match(phone)
            if isValid(phone):
                break
            else:
                print('Invalid phone no.,enter again!')
                continue
        while True:
            email=input('Enter email address of the student: ')
            regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            def check(email):
                if re.search(regex,email):
                    return True
                else:
                    return False
            if check(email) == True:
                break
            else:
                print('Invalid email address,enter again!')
                continue            
        s[name] = {}
        s[name]['Name'] = name
        s[name]['SIC'] = sic
        s[name]['Phone no.'] = phone
        s[name]['Mail id'] = email
        print('The student has been added')
    def delete_students(self):
        name=input('Enter the name of the student you want to delete: ')
        del s[name]
    def display_books(self):        
        print(b)     
    def display_students(self):
        print(s)
           
class Librarian(Admin):
    info=[]
    n=0
    def issue_book(self):
        name=input('Enter your name: ')
        if name in s:
            books=input('Enter the name of the book you want to issue: ')
            if books in b:
                c=int(b[books]['Copies'])
                if c != 0:
                    c-=1
                    b[books]['Copies']=int(c)
                    if [name,books] not in Librarian.info:
                        info=self.info.append([name,books])
                        if name == Librarian.info[0][0]:
                            Librarian.n+=1
                        if Librarian.n<=2:
                            print('Book is successfully issued')
                        else:
                            print('Cannot issue more than 2 books, first return then issue again!')
                    else:
                        print('Cannot issue same book more than once')
                else:
                    print('Book not available')
            else:
                print('Book not available')   
        else:
            print('You have not registered in the library, first get yourself registered')
    def return_book(self):
        name=input('Enter your name: ')
        if name in s:
            books=input('Enter the name of the book you want to return: ')
            if books in b:
                c=int(b[books]['Copies'])
                c+=1
                b[books]['Copies']=int(c)
                print('Book is successfully returned')
                info=self.info.remove([name,books])
            else:
                print('Wrong details of the book.Try again')
        else:
            print('You are in the list, first add yourself')
    def data(self):
        print('The list of students having books are: ')
        print('Name:Book')
        for i in range(len(Librarian.info)):
            print(Librarian.info[i][0],':',Librarian.info[i][1])



def main():
    admin=Admin()
    librarian=Librarian()    
    def loginauth(username, password):
        if username in users:
            if password == users[username]['password']:
                print('Login successful')
                return True
        return False
    def login():
        while True:
            username = input('Username: ')
            if not len(username) > 0:
                print('Username cannot be blank')
            else:
                break
        while True:
            password = input('Password: ')
            if not len(password) > 0:
                print('Password cannot be blank')
            else:
                break
        if loginauth(username, password):
            return session(username)
        else:
            print('Invalid username or password')
    def register():
        while True:
            username = input('New username: ')
            if not len(username) > 0:
                print('Username cannot be blank')
                continue
            else:
                break
        
        while True:
            flag = 0
            password = input('New password: ')
            while True:
                if len(password) not in range(6,13):
                    flag = -1
                    break
                elif not re.search('[a-z]',password):
                    flag = -1
                    break
                elif not re.search('[A-Z]',password):
                    flag = -1
                    break
                elif not re.search('[0-9]',password):
                    flag=-1
                    break
                elif not re.search('[!_@$%&]',password):
                    flag=-1
                    break
                elif re.search('\s',password):
                    flag=-1
                    break
                else:
                    flag=0
                    break
            if flag == -1:
                print('Invalid password.The password must contain atleast 1 uppercase letter, 1 lowercase letter, 1 special character, 1 number')
                continue
            else:
                break           
            
        print('Creating account...')
        users[username] = {}
        users[username]['password'] = password
        users[username]['group']='user'
        time.sleep(1)
        print('Account has been created')
    def session(username):
        print('Welcome to your account ' + username)
        while True:
            print('1.Modify books')
            print('2.Modify students')
            print('3.View available books')
            print('4.View registered students')
            print('5.Exit')
            choice=int(input('Enter your choice: '))
            if choice == 1:
                while True:
                    print('1.Add books')
                    print('2.Delete books')
                    print('3.Exit')
                    choice=int(input('Enter your choice: '))
                    if choice == 1:
                        admin.add_books()
                    elif choice == 2:
                        admin.delete_books()
                    elif choice == 3:
                        break
                    else:
                        print('Not a valid option')
            elif choice == 2:
                while True:
                    print('1.Add students')
                    print('2.Delete students')
                    print('3.Exit')
                    choice=int(input('Enter your choice: '))
                    if choice == 1:
                        admin.add_students()
                    elif choice == 2:
                        admin.delete_students()
                    elif choice == 3:
                        break
                    else:
                        print('Not a valid option')
            elif choice == 3:
                admin.display_books()
            elif choice == 4:
                admin.display_students()
            elif choice == 5:
                return
                                
    def adm():
        print('Welcome to the Library. Please register or login.')
        print('Options: register | login | exit')
        option = input("> ")
        if option == "login":
            login()
        elif option == "register":
            register()
        elif option == "exit":
            exit()
        else:
            print(option + " is not an option")
    while True:
        print('==========WELCOME TO THE LIBRARY==========')
        print('Do you want to continue as: ')
        print('1.Admin')
        print('2.Librarian')
        print('3.Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            adm()                      
        elif choice == 2:
            while True:
                print('1.View available books')
                print('2.Issue book')
                print('3.Return book')
                print('4.List of students which took a specific books')
                print('5.Exit')
                choice=int(input('Enter your choice: '))
                if choice == 1:
                    admin.display_books()
                elif choice == 2:
                    librarian.issue_book()
                elif choice == 3:
                    librarian.return_book()
                elif choice == 4:
                    librarian.data()
                elif choice == 5:
                    break
                else:
                    print('Not a valid option')
        elif choice == 3:
            exit()
        else:
            print('Not a valid option')
            continue
main()
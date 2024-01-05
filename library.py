class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        print(f"We have following books in {self.name} library : ")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            self.booklist.remove(book)
            print("Lender book database has been updated you can take the book now ")
        else:
            print(f"The book is already been used by f{self.lenddict[book]}")

    def addbook(self,book):

        for b in self.booklist:
            if(book == b):
                print("This book is already present in the library")
                return
        self.booklist.append(book)
        print("The book is been added to the library ")

    
    def returnbook(self,book):
        
        

        if book in self.lenddict.keys():
            self.lenddict.pop(book)
            self.booklist.append(book)
        else:
            print("This book does not belong to this library")
            


    

ayush = library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Ayush_Lib")


while True:
    print(f"Welcome to {ayush.name} LIBRARY please select the following options from below")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    print("5. Exit ")
    try:
        user_choice = int(input("Enter the choice : "))
        if(user_choice==1):
            ayush.displaybook()
        elif(user_choice==2):
            user = input("Enter the name of the user : ")
            book1 = input("Enter the book name : ")
            ayush.lendbook(user,book1)
        elif(user_choice==3):
            book2 = input("Enter the book that you want to add : ")
            
            ayush.addbook(book2)
        elif(user_choice==4):
            book = input("Enter the book you want to return :")
            ayush.returnbook(book)
        elif(user_choice==5):
            print("Thank for using this library........ ")
            exit()
    except ValueError:
        print(f"Please type an integer value and not a string literal")
        
        
    





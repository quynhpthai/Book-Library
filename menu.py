import sys
import book_dao
import mysql.connector

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    # More options to be added
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    # To be added
    1:'All books',
    2:'Search by Title',
    3:'Search by ISBN',
    4: 'Search by publisher ',
    5: 'Search by price range from min to max',
    6:'Seach by published year',
    7:'Search by title and publisher'
}

def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))
    print("---End of Search Results---")

def search_by_title(title):
    results = book_dao.findByTitle(title)
    print("Search by Title:")
     # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))


    print("---End of Search Results---")

def search_by_isbn(ISBN):
    results = book_dao.findByISBN(ISBN)
    print("Search by ISBN:")
    # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))


    print("---End of Search Results---")

def search_by_publisher(publisher):
    results=book_dao.findbyPublisher(publisher)
    print("Search by Publisher:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))
    print("---End of Search Results---")
def search_by_price(min,max):
    results=book_dao.findByPrice(min,max)
    print("Search by price:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))
    print("---End of Search Results---")
def search_by_year(year):
    results=book_dao.findByYear(year)
    print("Search by year:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))
    print("---End of Search Results---")
def search_by_tile_publisher(title,publisher):
    results=book_dao.findByTitleAndPublisher(title,publisher)
    print("Search by year:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1],"|",item[2],"|",item[3],"|", item[4],"|",item[5]))
    print("---End of Search Results---")
def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()
def print_query():
    print()
    print("Please make a selection")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()



def option1():  # add a publisher
    print()
    print("-------Add Publisher-------")
    print("Type NULL for no entry.")
    name=""
    while len(name)==0:
        name = input("Enter Name: ")
        if len(name)>25:
            name=""
            print("Error: name length must be smaller than 25")
    phone = ""
    while phone == "":
        phone = input("Enter Phone Number: ")
        if len(phone) != 10:
            phone = ""
            print("Error: Phone number length must be 10!")
        try:
            int(phone)
        except ValueError:
            phone = ""
            print("Error: Phone number must consist of integers!")
    city = ""
    while len(city) == 0:
        city = input("Enter City: ")
        if len(city) > 20:
            city = ""
            print("Error: City name too long (max 20 characters)!")
    result = book_dao.addPublisher(name, phone, city)
    print(result)
def option2():#ADD book
    print()
    print("-------Add Book-------")
    print("Type NULL for no entry.")
    ISBN = ""
    while len(ISBN) == 0:
        ISBN = input("Enter ISBN Number: ")
        if len(ISBN) > 10:
            ISBN = ""
            print("Error: ISBN length must be smaller than 10!")
    title=""
    while len(title)==0:
        title = input("Enter Title: ")
        if len(title) > 50:
            title = ""
            print("Error: title length must be smaller than 50!")
    year=""
    while len(year)==0:
        year=input("Enter published year: ")
        if len(year)!=4:
            year=""
            print("Error: year must have at 4 digits")
        try:
            int(year)
        except ValueError:
            year = ""
            print("Error: year number must consist of integers!")
    published_by=""
    while(len(published_by)==0):
        published_by=input("Enter publisher: ")
        if len(published_by>25):
            published_by=""
            print("Error: publisher name must be smaller than 25")
       
    previousEdition=""
    while(len(previousEdition)==0):
        previousEdition=input("Enter previous Edition: ")
        if len(previousEdition)>10:
            previousEdition=""
            print("Error: previous edition must be smaller than 10")
       
    price=""
    while price=="":
        price=input("Enter price: ")
        try:
            float(price)
        except ValueError:
            price = ""
            print("Error: price  must consist of number only !")
    result = book_dao.addBook( ISBN, title, year, published_by, previousEdition, price)
    print(result)


def option3():
        ISBN=""
        while len(ISBN)==0:
            ISBN = input("Enter ISBN Number of the book you want to edit: ")
            if len(ISBN) > 10:
                ISBN = ""
                print("Error: ISBN length must be smaller than 10!")
        book_dao.editBook(ISBN)
        
def option4():
        ISBN=""
        while len(ISBN)==0:
            ISBN = input("Enter ISBN Number of the book you want to delete: ")
            if len(ISBN) > 10:
                ISBN = ""
                print("Error: ISBN length must be smaller than 10!")
        book_dao.deleteBook(ISBN)
    

def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    # print_search_menu

    # user selection of options and actions

    print_query()    
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except:
        print('Wrong input. Please enter a number ...')
    if option == 1:
        print("Search Option 1: all books were chosen.")
        search_all_books()
    elif option == 2:
        print("Search Option 2, specified name of book:")
        try: 
            title= input('Enter book name:')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_title(title)
    elif option==3:
        print("Search option 3, please specified ISBN")
        try: 
            isbn= input('Enter book ISBN:')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_isbn(isbn)
    elif option ==4:
        print("Search option 4, please specified publisher")
        try: 
            publisher= input('Enter book publisher:')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_publisher(publisher)
    elif option == 5:
        print("Search option 5, please specified price range")
        try: 
            min= input('Enter book price min:')
            max=input('Enter book price max: ')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_price(min,max)
    elif option==6:
        print("Search option 6, please specified published year")
        try: 
            year=input('Year published: ')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_year(year)
    elif option ==7:
        print("Search option 7, please specified title and publisher")
        try: 
            title= input('Enter book title :')
            publisher=input('Enter book publisher: ')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_tile_publisher(title,publisher)
    else:
        print("Invalid option, please type an option from 1 to 7")
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option ==3:
            option3()
        # More options to be added
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            book_dao.close()
            exit()
            
        else:
            print('Invalid option. Please enter a number between 1 and 6.')












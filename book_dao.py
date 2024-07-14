import mysql.connector
from mysql_connector import connection
#Find all the book
def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    
#find by title attribute
def findByTitle(title):
    # returns all tuples in Book with specified title attribute
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where Book.title='" + title + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def findByISBN(ISBN):
    #return all tuples in Book with specified ISBN
    cursor = connection.cursor()
    query = "select *  from bookmanager.Book where Book.ISBN='" + ISBN + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def findbyPublisher(publisher):
    #return all tuples with specified publisher
    cursor = connection.cursor()
    query = "select *  from bookmanager.Book where Book.published_by='" + publisher + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def findByPrice(min,max):
    cursor = connection.cursor()
    query = "select *  from bookmanager.Book where Book.price>='" + min + "' and Book.price<'"+max+"'"
    cursor.execute(query)
    results = cursor.fetchall()
    #cursor.close()
    return results
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where Book.year='"+year+"'"
    cursor.execute(query)
    results = cursor.fetchall()
    #cursor.close()
    return results
def findByTitleAndPublisher(title,publisher):
    cursor = connection.cursor()
    query = "select *  from bookmanager.Book where Book.title='"+title+"' and Book.published_by='"+publisher+"'"
    cursor.execute(query)
    results = cursor.fetchall()
    #cursor.close()
    return results
def addPublisher(name, phone, city):
    # inserts a tuple into Publisher
    cursor = connection.cursor()
    query = "insert into Publisher values('" + name + "', '" + phone + "', '" + city + "')"
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
       # cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists!"
    #cursor.close()
    return "Publisher <" + name + "> added successfully"
#add book queries
def addBook(ISBN, title, year, published_by, previous_edition, price):
    cursor = connection.cursor()
    if(previous_edition=="NULL"):#if their is no previous edition
         query = "insert into Book values('" + ISBN + "', '" + title + "', '" + year+"','"+published_by+"',"+previous_edition+",'"+price + "')"
    else:
        query = "insert into Book values('" + ISBN + "', '" + title + "', '" + year+"','"+published_by+"','"+previous_edition+"','"+price + "')"
    
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        return "Duplicate entry: book <" + title + "> already exists!"
    #cursor.close()
    return "Book <" + title + "> added successfully"
def editBook(isbn):
        cursor = connection.cursor()

        # Check if the book with the provided ISBN exists
        query="SELECT * FROM bookmanager.Book WHERE ISBN = '" + isbn + "'"
        cursor.execute(query)
        existing_book = cursor.fetchone()

        if existing_book is None:
            print("Book not found.")
        else:
            # Get new values for the book
            new_title=""
            while(len(new_title)==0):
                new_title = input("Enter new title: ")
                if len(new_title) > 50:
                    new_title = ""
                    print("Error: title length must be smaller than 50!")
            new_year=""
            while(len(new_year)==0):
                new_year = input("Enter the new year: ")
                if len(new_year)!=4:
                    new_year=""
                    print("Error: year must have at 4 digits")
                try:
                    int(new_year)
                except ValueError:
                    new_year = ""
                    print("Error: year number must consist of integers!")
            new_published_by=""
            while(len(new_published_by)==0):
                new_published_by = input("Enter the new publisher: ")
                if len(new_published_by)>25:
                    new_published_by=""
                    print("Error: publisher name must be smaller than 25")
            new_previous_edition=""
            while(len(new_previous_edition)==0):
                new_previous_edition = input("Enter the new previous edition: ")
                if len(new_previous_edition)>10:
                    new_previous_edition=""
                    print("Error: previous edition must be smaller than 10")
            new_price=""
            while new_price=="":
                new_price=input("Enter price: ")
            try:
                float(new_price)
            except ValueError:
                new_price = ""
                print("Error: price  must consist of number only !")
                new_price = input("Enter the new price: ")

            # Execute the SQL UPDATE statement
            if(new_previous_edition=="NULL"): #IF THere is no previous edition
                
                sql_update = " UPDATE bookmanager.Book SET title ='"+new_title+"',year='"+new_year+"',published_by='"+new_published_by+"',previous_edition=NULL"+",price='"+new_price+"' where ISBN='"+isbn+"'"
            else:
                sql_update = " UPDATE bookmanager.Book SET title ='"+new_title+"',year='"+new_year+"',published_by='"+new_published_by+"',previous_edition='"+new_previous_edition+"',price='"+new_price+"' where ISBN='"+isbn+"'"
            try:
                cursor.execute(sql_update)

            # Commit the changes to the database
                connection.commit()
                print("Book information updated successfully.")

            except mysql.connector.errors.IntegrityError:
                print("Error editting book")

            # Close the database connection
            #cursor.close()

def deleteBook(isbn):
        cursor = connection.cursor()

        # Check if the book with the provided ISBN exists
        query="SELECT * FROM bookmanager.Book WHERE ISBN = '" + isbn + "'"
        cursor.execute(query)
        existing_book = cursor.fetchone()

        if existing_book is None:
            print("Book not found.")
        #write delete
        else:
            delete="DELETE FROM bookmanager.Book WHERE ISBN = '"+isbn+"'"
            cursor.execute(delete)
            connection.commit()
            print("Book information deleted successfully.")
# close the connection
def close():
    connection.close()
    
import sqlite3
import requests

# get data from API
def fetch_books_from_api():
    api_url = "https://openlibrary.org/search.json?q=python&limit=10"
    response = requests.get(api_url)
    json_data = response.json()
    book_list = []
    docs = json_data.get('docs', [])
    for book_data in docs:
        book_title = book_data.get('title', 'Unknown Title')
        author_list = book_data.get('author_name', [])
        if author_list:
            book_author = author_list[0]
        else:
            book_author = 'Unknown Author'
        
        year = book_data.get('first_publish_year')
        if year is None:
            publish_years = book_data.get('publish_year', [])
            if publish_years:
                year = publish_years[0]
        
        if year:
            book_info = {
                'title': book_title,
                'author': book_author,
                'publication_year': year
            }
            book_list.append(book_info)
    
    return book_list


#save data to database
def store_books_in_database(books):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER
    )
    """
    cursor.execute(create_table_query)
    
    for book in books:
        title = book['title']
        author = book['author']
        year = book['publication_year']
        
        insert_query = "INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (title, author, year))
    
    connection.commit()
    connection.close()


# show data from database
def display_books():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_query = "SELECT title, author, publication_year FROM books"
    cursor.execute(select_query)
    all_books = cursor.fetchall()
    
    if len(all_books) == 0:
        print("No books found in database")
        connection.close()
        return
    
    print("\nBooks in Database:")
    print("-" * 70)
    print("Title".ljust(35) + "Author".ljust(25) + "Year")
    print("-" * 70)

    for book in all_books:
        title = book[0]
        author = book[1]
        year = book[2]
        print(title.ljust(35) + author.ljust(25) + str(year))
    
    print("-" * 70)
    print("Total books: " + str(len(all_books)))
    print()
    
    connection.close()


def main():
    print("Getting books from API...")
    books = fetch_books_from_api()
    print("Got " + str(len(books)) + " books")
    
    print("Saving to database...")
    store_books_in_database(books)
    print("Saved successfully!")
    
    print("Displaying books:")
    display_books()


if __name__ == "__main__":
    main()


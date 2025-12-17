""" Create our database from scratch"""

import pandas as pd

from transitionzero.goodreads.models import database

def create_db():
    database.Base.metadata.create_all(database.engine)
    return True

def fill_db(books):
    
    db = next(iter(database.get_db()))

    db_authors = [database.Author(name=author) for author in books.author.unique()]
    db_books = [
        database.Book(
            title=book['title'],
            year=book['year'],
            genre=book['genre'],
            author_name=book['author'],
            times_read=1
        )
        for _, book in books.iterrows()
    ]
    
    db.add_all(db_authors)
    db.add_all(db_books)
    db.commit()

    return True


if __name__=="__main__":
    books = pd.read_csv('./bin/tz_reads.csv')
    create_db()
    fill_db(books)
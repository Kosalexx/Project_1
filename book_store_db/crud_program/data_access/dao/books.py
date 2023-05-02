from __future__ import annotations
from .base import BaseDAO
from data_access.factories import BooksFactory
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.dto import BooksDTO


class BooksDAO(BaseDAO):
    def get_all_data(self) -> list[BooksDTO]:
        data = self._db_gateway.cursor.execute(
            'SELECT * FROM books ORDER BY name;'
        )
        result_list: list[tuple] = data.fetchall()
        final_list: list[BooksDTO] = []
        for row in result_list:
            list_data = list(row)
            book_id = row[0]
            genres = self._db_gateway.cursor.execute(
                'SELECT genres.name FROM genres '
                'JOIN books_genres ON genres.genre_id = books_genres.genre_id '
                'WHERE book_id = ?;', (book_id, )
            )
            genres_list = genres.fetchall()
            res_genres_list: list[tuple] = []
            for genre in genres_list:
                res_genres_list.append(*genre)
            list_data.append(res_genres_list)
            authors = self._db_gateway.cursor.execute(
                'SELECT authors.first_name, authors.last_name FROM authors '
                'JOIN books_authors ON authors.author_id = '
                'books_authors.author_id WHERE book_id = ?;', (book_id, )
            )
            authors_list = authors.fetchall()
            res_authors_list = []
            for author in authors_list:
                result_name = ''
                for names in author:
                    result_name += str(names)
                    result_name += " "
                res_authors_list.append(result_name)
            list_data.append(res_authors_list)
            data_dto = BooksFactory(list_data=list_data).generate_dto()
            final_list.append(data_dto)
        return final_list

    def check_in_data(self, value: int) -> bool:
        data = self._db_gateway.cursor.execute(
            'SELECT name FROM books WHERE book_id = ?', (value, )
        )
        result_list = data.fetchall()
        if result_list == []:
            return False
        else:
            return True

    def delete_data(self, value: int) -> None:
        self._db_gateway.cursor.execute('PRAGMA foreign_keys = ON;')
        self._db_gateway.cursor.execute(
            'DELETE FROM books WHERE book_id = ?;', (value, ))
        self._db_gateway.connection.commit()

    def update_value(self, integer_id: int, new_value: str) -> None:
        self._db_gateway.cursor.execute(
            'UPDATE books SET name = ? WHERE book_id = ?;',
            (new_value, integer_id))
        self._db_gateway.connection.commit()

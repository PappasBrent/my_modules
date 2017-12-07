#!/usr/bin/python3
'''
A module providing a wrapper class for providing
a simple way to create and manage a database
'''
import sqlite3


class Database:
    '''
    A wrapper class for SQLite databases; provides
    a simple way to create and manage a database
    '''

    def __init__(self, filename):
        self._filename = filename
        self._db = sqlite3.connect(self._filename)
        self._db.row_factory = sqlite3.Row
        self._db.commit()

    def open_table(self, table_name, overwrite=True, **headers):
        '''
        Opens a database table; will overwrite a pre-existing
        table with the same name if overwrite is set to True
        '''

        if overwrite:
            self._db.execute("DROP TABLE IF EXISTS {}".format(table_name))

        args = ''
        i = 0
        for record, valtype in headers.items():
            i += 1
            args += record + ' '
            args += valtype
            if i < len(headers):
                args += ', '

        self._db.execute(
            "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, args))


def main():
    '''
    Executes script
    '''
    my_db = Database('test.sqlite3')
    my_db.open_table('People', name='TEXT', age='INT')


if __name__ == "__main__":
    main()

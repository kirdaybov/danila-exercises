class Book:
    def __init__(self, header, author, publisher):
        self.__header = header
        self.__author = author
        self.__publisher = publisher

    def set_header(self, header):
        self.__header = header

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher
  
    def get_header(self):
        return self.__header

    def get_author(self):
        return self.__author
        
    def get_publisher(self):
        return self.__publisher

    def __str__(self):
        return f"Заголовок: {self.__header}\n" + \
                f'Автор:{self.__author}\n' + \
                f'Издатель:{self.__publisher}'


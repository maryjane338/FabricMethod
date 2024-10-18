from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def save(self):
        pass


class PDFDocument(Document):
    def __init__(self, number_of_pictures):
        self.pictures = number_of_pictures

    def save(self):
        try:
            print(f'Файл формата "PDF" с числом картинок {int(self.pictures)} успешно сохранён!')
        except ValueError:
            print('Вам нужно ввести ЧИСЛО. Файл не сохранён. Попробуйте ещё раз.')


class WordDocument(Document):
    def __init__(self, number_of_strings, which_words):
        self.strings = number_of_strings
        self.words = which_words

    def save(self):
        if self.words == '':
            print('В вашем документе должен находиться хотя бы 1 символ. Файл не сохранён. Попробуйте ещё раз')
        else:
            try:
                print(f'Файл формата "Word", состоящий из {int(self.strings)} строк и слов: {self.words}', end=' ')
                print('успешно сохранён!')
            except ValueError:
                print('В поле "Введите количество строк" нужно ввести ЧИСЛО. Файл не сохранён. Попробуйте ещё раз.')


class ExcelDocument(Document):
    def __init__(self, number_of_columns, number_of_rows):
        self.columns = number_of_columns
        self.rows = number_of_rows

    def save(self):
        try:
            print(f'Файл формата "Excel", состоящий из таблицы, в которой {int(self.columns)}', end=' ')
            print(f'столбца и {int(self.rows)} строки успешно сохранён!')
        except ValueError:
            print('Количество столбцов и строк должно являться ЧИСЛОМ. Файл не сохранён. Попробуйте ещё раз.')


class DocumentFactory:
    def __init__(self, document):
        self.type_of_document = document

    def make_document(self):
        if self.type_of_document == 'PDF':
            return PDFDocument(input('Введите количество картинок: '))
        elif self.type_of_document == 'Word':
            return WordDocument(input('Введите количество строк: '), input('Введите слова: '))
        elif self.type_of_document == 'Excel':
            return ExcelDocument(input('Введите число колонок: '), input('Введите число строк: '))
        else:
            print('Такого типа документов не существует. Попробуйте ещё раз.')


presentation = DocumentFactory('PDF').make_document()
presentation.save()

text = DocumentFactory('Word').make_document()
text.save()

table = DocumentFactory('Excel').make_document()
table.save()

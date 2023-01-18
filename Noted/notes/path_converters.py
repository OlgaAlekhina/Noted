from datetime import datetime, date


# для перевода строки, передаваемой в урле, в формат даты
class DateConverter:
    regex = '[0-9]{2}-[0-9]{2}-[0-9]{4}'

    def to_python(self, value: str):
        return datetime.strptime(value, '%d-%m-%Y').date()

    def to_url(self, value: date):
        return value.strftime('%d-%m-%Y')
from django import template

register = template.Library()

# фильтр, который убирает путь в названии файла, присоединенного к заметке
@register.filter(name='file_name')
def change_filename(text):

	return text.replace("documents/", "")
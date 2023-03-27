from django import template

register = template.Library()

@register.filter(name='file_name')
def change_filename(text):

	return text.replace("documents/", "")
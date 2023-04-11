from django.template import Library

register = Library()

def img_path(value): # Only one argument.
    """Converts a full path from and image to the simple image file path"""
    return 'images/' + str(value).split('/')[-1]

def index(list, index): # Only one argument.
    """Converts a full path from and image to the simple image file path"""
    return list[index]

register.filter('img_path', img_path)
register.filter('index', index)
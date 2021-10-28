from django import template
from ..models import Contact

register = template.Library()

@register.simple_tag
def contact():
    contact = Contact.objects.last()
    return contact

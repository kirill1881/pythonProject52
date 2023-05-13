from django.db.models import QuerySet

from .models import Order
from .models import Person
from .models import ItemModel
class OrderToShow:
    def __init__(self, item_id, user_id):
        person = Person.objects.filter(id = user_id)[0]
        print(type(person))
        item = ItemModel.objects.filter(id = item_id)[0]
        name = person.name
        lastname = person.surname
        number = person.number
        adress = person.citizenship
        item_name = item.product_name


# from django.db import models

# Create your models here.

from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

# Create your models here.


class City(StructuredNode):
    code = StringProperty(required=True)
    name = StringProperty(default="city")

class Person(StructuredNode):

    name = StringProperty()
    age = IntegerProperty(default=0)

    # Relations :
    city = RelationshipTo(City, 'LIVES_IN')
    friends = RelationshipTo('Person','FRIEND')



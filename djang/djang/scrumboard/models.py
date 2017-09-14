from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

#Created two classes inherit from model.Models
#models.Models allows data saved into database
@python_2_unicode_compatible
class List(models.Model):
    name =  models.CharField(max_length=50)

    def _str__(self):
        return "List: {}".format(self.name)

@python_2_unicode_compatible
class Card(models.Model):
    title = models.CharField(max_length =100)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name = "cards")# relation between card and list, each card is in a list, argument to model, related name in list class we have cards prop cotians all cards in list n blank true or null true so all have property
    story_points = models.IntegerField(null =True, blank= True)
    business_value = models.IntegerField(null = True, blank= True)

    def __str__(self):
        return "Card:{}".format(self.title)

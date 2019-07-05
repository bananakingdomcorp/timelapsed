# This file is for the placement of Django Signals. These are used as the engine to run our relationships. 

#NOTE: Consider Circular Dependencies. 

from ..models import Card, Subclass_Relationships


from django.db.models.signals import pre_save
from django.dispatch import receiver

#Move

@receiver(pre_save, sender = Card)
def move_signal(sender, instance, *args, update_fields, **kwargs):
  print('SIGNAL FOUND')

  print(sender)
  print(instance)
  print(update_fields)

  #If we find this move what we will do is find the child action and do it as well. 


#Delete

@receiver(pre_save, sender = Card)
def delete_signal(sender, instance, *args, **kwargs):
  print('DELETE FOUND')

  print(sender)
  print(instance)


#Subclass

@receiver(pre_save, sender = Subclass_Relationships)
def move_signal(sender, instance, *args, update_fields, **kwargs):
  print('SUBCLASS FOUND')

  print(sender)
  print(instance)
  print(update_fields)


#Tag

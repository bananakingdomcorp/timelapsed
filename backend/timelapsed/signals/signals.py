# Directions:

#Locmemcache ase will be used as a caching service. When we make changes in our signals we will write that data into locmemcache. 
#When we are ready to return a response we will build a response from our lomemcache and return it. This allows us to return 
#any and all changes to cards in one response. 


from ..models import Card, Subclass_Relationships, Card_Relationship_Move_Action, Topic, Card_Relationship_Parent_Action, Card_Relationship_Child_Action
from ..services import peform_child_action
from django.core.cache.backends import locmem

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

  if 'Topic' in update_fields:
    relationships =  Card_Relationship_Move_Action.objects.filter(Card_ID = instance, Topic_ID = Topic.objects.get(id = update_fields['Topic']) )

    for i in relationships:
      print(i)

      parent_actions =Card_Relationship_Parent_Action.objects.filter(Move_ID = i)
      for j in parent_actions:
        try:
             child_action = Card_Relationship_Child_Action(Parent_Action = j)
             peform_child_action(child_action)
        except Card_Relationship_Child_Action.DoesNotExist:
            continue       


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

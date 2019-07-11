# Directions:

#Locmemcache ase will be used as a caching service. When we make changes in our signals we will write that data into locmemcache. 
#When we are ready to return a response we will build a response from our lomemcache and return it. This allows us to return 
#any and all changes to cards in one response. 


from ..models import Card, Subclass_Relationships, Card_Relationship_Move_Action, Topic, Card_Relationship_Parent_Action, Card_Relationship_Child_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action
# from ..services import peform_child_action
import  timelapsed.services as services
from django.core.cache.backends import locmem
from django.core.signals import request_finished

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

#Move

def perform_card_relationship_lookup(relationship):
  for i in relationship:
    parent_actions =Card_Relationship_Parent_Action.objects.filter(Move_ID = i)
    for j in parent_actions:
      try:
        child_action = Card_Relationship_Child_Action(Parent_Action = j)
        services.peform_child_action(child_action)
      except Card_Relationship_Child_Action.DoesNotExist:
          continue   



@receiver(pre_save, sender = Card)
def move_signal(sender, instance, *args, **kwargs):


  if instance.id != None:

    instance_in_DB = Card.objects.get(id = instance.id)

    if instance_in_DB.Topic != instance.Topic:

      perform_card_relationship_lookup( Card_Relationship_Move_Action.objects.filter(Card_ID = instance, Topic_ID = instance.Topic ))



#Delete

@receiver(pre_delete, sender = Card)
def delete_signal(sender, instance, **kwargs):

  perform_card_relationship_lookup(Card_Relationship_Delete_Action.objects.filter(Card_ID = instance))


#Subclass

@receiver(pre_save, sender = Subclass_Relationships)
def subclass_signal(sender, instance, **kwargs):


  perform_card_relationship_lookup( Card_Relationship_Subclass_Action.objects.filter(Subclass_ID = instance.Subclass, Card_ID = instance.Child_ID))


#Tag

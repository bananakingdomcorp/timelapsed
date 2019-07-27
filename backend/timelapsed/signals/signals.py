# Directions:

#Locmemcache will be used as a caching service. When we make changes in our signals we will write that data into locmemcache. 
#When we are ready to return a response we will build a response from our locmemcache and return it. This allows us to return 
#any and all changes to cards in one response. 

#In production, we may want to switch to memcached. 

#Need to think a lot about thread safety and especially locks in this function. 


from ..models import Card, Subclass_Relationships, Card_Relationship_Move_Action, Topic, Card_Relationship_Parent_Action, Card_Relationship_Child_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action, Card_Relationship_In_Same_Action
import  timelapsed.services as services
from django.core.signals import request_finished

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from ..batching.responses import card_response_builder
from searchapp import search




def peform_card_action(card_action):

  #card_response_builder found in batching/responses. 

  if card_action.Move_ID is not None:

    move_action = card_action.Move_ID
    move_action_card = move_action.Card_ID
    move_action_card.Topic = move_action.Topic_ID
    move_action_card.save()

    card_response_builder.edit(move_action_card)

    return


  if card_action.Delete_ID is not None:

    delete_action = card_action.Delete_ID
    delete_action_card = delete_action.Card_ID
    
    card_response_builder.delete(delete_action_card.id)

    delete_action_card.delete()

    return

  if card_action.Subclass_ID is not None:

    subclass_action = card_action.Subclass_ID
    subclass_action_card = subclass_action.Card_ID
    new_relationship = Subclass_Relationships.objects.create(Email = subclass_action.Email, Subclass = subclass_action.Subclass_ID, Child_ID = subclass_action_card)
    

    card_response_builder.subclass(new_relationship)

    return 

  # if child_action.Tag_ID is not None:

    # Fill in later once tags are finished. 


    # return


def peform_card_same_action(instance, relationship):
  become_same = None

  #If parent

  if instance.id == relationship.Card_ID.id:
    become_same = relationship.Child_ID
    become_same.Topic = instance.Topic


  else:

    become_same = relationship.Card_ID
    become_same.Topic = instance.Topic
  

  parent = Card_Relationship_Parent_Action.objects.get(Same_ID = relationship)
  parent.delete()
  relationship.delete()

  become_same.save() 

  card_response_builder.edit(become_same)





def perform_card_relationship_lookup(relationship):
  for i in relationship:
    parent_actions =Card_Relationship_Parent_Action.objects.filter(Move_ID = i)    
    for j in parent_actions:
      try:
        child_actions = Card_Relationship_Child_Action.objects.filter(Parent_Action = j)
        #Class that performs this action found in services. 
        for k in child_actions:
          peform_card_action(k)
          k.delete()
      finally:
        j.delete()
        #This deletion should also cascade to delete the card action model as well. 
      


@receiver(pre_save, sender = Card)
def card_save_signal(sender, instance, *args, **kwargs):

  #If Move
  if instance.id != None:

    instance_in_DB = Card.objects.get(id = instance.id)

    if instance_in_DB.Topic != instance.Topic:
      # Perform checks for moves
      perform_card_relationship_lookup( Card_Relationship_Move_Action.objects.filter(Card_ID = instance, Topic_ID = instance.Topic ))
      # Perform checks for same as parent


    try:
      #Try to find card relationships where you are are card_ID.
      find_same =  Card_Relationship_In_Same_Action.objects.get(Card_ID = instance)
    
    except Card_Relationship_In_Same_Action.DoesNotExist:
      try:
        #If can't find as card_ID, try as Child_ID. 
        find_same_child =  Card_Relationship_In_Same_Action.objects.get(Child_ID = instance)     
  
      except Card_Relationship_In_Same_Action.DoesNotExist:      
        pass
      
      else:
        peform_card_same_action(instance, find_same_child)
    
    else:
      peform_card_same_action(instance, find_same)

      
    card_response_builder.edit(instance)

    #perform ES call. 

    #NOTE: I am aware this is a non-optimal configuration, a better solution using the ES bulk api needs to be built. This will work for now. 

    change = search.ElasticSearchCard.get(id = instance.pk)   
    change.update(Name = instance.Name, Description = instance.Description, Topic = instance.Topic.Name )

  else:

    return



#Delete

@receiver(pre_delete, sender = Card)
def delete_signal(sender, instance, **kwargs):

  #NON-OPTIMAL CONFIGURATION, BUILD ES BATCHING SERVICE 

  remove = search.ElasticSearchCard.get(id = instance.pk)
  remove.delete()



  perform_card_relationship_lookup(Card_Relationship_Delete_Action.objects.filter(Card_ID = instance))


#Subclass

@receiver(pre_save, sender = Subclass_Relationships)
def subclass_signal(sender, instance, **kwargs):


  perform_card_relationship_lookup( Card_Relationship_Subclass_Action.objects.filter(Subclass_ID = instance.Subclass, Card_ID = instance.Child_ID))


#Tag

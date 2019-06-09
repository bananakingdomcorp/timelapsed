# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

from datetime import datetime
from django.shortcuts import get_object_or_404

class CardListSerializer(serializers.ListField):
#Just a generic serializer for any lists of card ID's 

  child = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())




class UsersSerializer(serializers.ModelSerializer):
  Email = serializers.EmailField()

  class Meta:
    model = Users
    fields = ('Email',)

  def create(self, validated_data):
    return super().create(validated_data)



class CreateCardTimesSerializer(serializers.ModelSerializer):
  Begin_Date = serializers.DateField()


  class Meta:
    model = Date_Range
    fields = ('Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time', )

class EditCardTimesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Date_Range
    fields = ('Begin_Time', 'End_Time', 'Num_Weeks', 'Weeks_Skipped')


class DeleteCardTimesSerializer(serializers.ListField):
  child = serializers.CharField()


class UpdateCardTimesSerializer(serializers.Serializer):
  Edit = serializers.DictField(child = EditCardTimesSerializer(),)
  Add = serializers.ListField(child = CreateCardTimesSerializer(),)
  Delete = DeleteCardTimesSerializer()


  class Meta:
    model = Date_Range
    # fields = ('Delete',)
    exclude = ('Add', 'Edit')

class CreateCardDataSerializer(serializers.ModelSerializer):
  Topic = serializers.PrimaryKeyRelatedField(queryset = Topic.objects.all())
  Position = serializers.IntegerField(required = False,)

  class Meta: 
    model = Card
    fields = ('Name', 'Description', 'Topic', 'Position' )

class UpdateCardSerializer(serializers.ModelSerializer):
  Data = CreateCardDataSerializer()
  Times = UpdateCardTimesSerializer(required = False,)

  
  def update(self, validated_data, pk, user):

    info = validated_data['Data']
    times = validated_data['Times']
    temp = Card.objects.values('Topic', 'Position').filter(id = pk).first()

    #If topic is the same. 
    if temp['Topic'] == info['Topic'] :
      #If Position has changed. 
      if info['Position'] != -1:
        #Find the position of the card to switch with. 
        pos = Card.objects.values('Position').filter(id = info['Position']).first()
        Card.objects.filter(id = info['Position']).update(Position = temp['Position'])
        
        Card.objects.filter(id = pk).update(Position = pos['Position'])
    else :
      #The topic has changed. 
      pos =  Card.objects.values('Position').filter(Topic = info['Topic']).order_by('-Position').first()
      #If there are no cards in the topic. 
      if pos == None:
        pos = 0
      else :
        pos = pos['Position']

      Card.objects.filter(id = pk).update(Description = info['Description'], Name = info['Name'], Position = pos +1, Topic = info['Topic'])
    
    Card.objects.filter(id = pk).update(Description = info['Description'], Name = info['Name'])     

    #Handle Deletions:

    for key in times['Delete']:
      Date_Range.objects.filter(id = key).delete()

    #Handle Edits:

    for key in times['Edit']:
      Date_Range.objects.filter(id = key).update(Begin_Time = times['Edit'][key]['Begin_Time'], End_Time = times['Edit'][key]['End_Time'], Num_Weeks =  times['Edit'][key]['Num_Weeks'], Weeks_Skipped = times['Edit'][key]['Weeks_Skipped']  )


    #Handle Additions:

    for key in times['Add']:
      ids = []
      a = Date_Range.objects.create(Day = key['Day'], Begin_Date = key['Begin_Date'], Num_Weeks = key['Num_Weeks'], Weeks_Skipped = key['Weeks_Skipped'], Begin_Time = key['Begin_Time'], End_Time = key['End_Time'], Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = pk) )
      ids.append(a.id)
      
    Return_Times =[j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = pk)).order_by('Begin_Date') ]


    return Return_Times

  class Meta:
    model = Card
    fields = ('Data', 'Times')


class CreateCardSerializer(serializers.ModelSerializer):

  Data = CreateCardDataSerializer()
  Times = serializers.ListField(child=CreateCardTimesSerializer(), required = False)

  def create(self, validated_data, user):
    info = validated_data['Data']
    

    pos =  Card.objects.values('Position').filter(Topic = info['Topic']).order_by('-Position').first()
    if pos == None:
      pos = 0
    else :
      pos = pos['Position']
    n =  Card.objects.create(Name = info['Name'], Description = info['Description'], Position = pos +1 , Email = Users.objects.get(Email = user), Topic = Topic.objects.get(id = info['Topic']))
    res = {}

    if validated_data.get('Times'):
      for times in validated_data['Times']:
        ids = []
        a = Date_Range.objects.create(Day = times['Day'], Begin_Date = times['Begin_Date'], Num_Weeks = times['Num_Weeks'], Weeks_Skipped = times['Weeks_Skipped'], Begin_Time = times['Begin_Time'], End_Time = times['End_Time'], Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = n.id) )
        ids.append(a.id)
        res['Data'] = {'ids': ids}
      res['Data']['id']= n.id      
    else :
      res['Data'] = {'id': n.id}
    return (res)

  class Meta:
    model = Card
    fields = ('Data', 'Times')

class DeleteCardSerializer(serializers.ModelSerializer):
  def destroy(self, pk):
    #Delete any times associated with said card. 

    Date_Range.objects.filter(Card_ID = Card.objects.get(id = pk)).delete()

    Card.objects.get(id = pk).delete()
    return 'Deleted'
  
  class Meta: 
    model = Card
    fields = ('id',)


class AddTopicSerializer(serializers.ModelSerializer):
  Name = serializers.CharField()


  def create(self, validated_data, user):
    # first, find the proper position. We can just add from the previous highest position.
    pos = Topic.objects.values('Position').filter(Email = user).order_by('-Position').first()
    next_position = None
    if pos == None:
      next_position = 1
    else:
      next_position = pos['Position'] + 1
    n = Topic.objects.create(Name = validated_data['Name'], Position = next_position, Email = Users.objects.get(Email = user))
    return({'Data': {'id': n.id, 'Name': validated_data['Name'], 'Cards': [] }})

  class Meta:
    model = Topic
    fields =  ('Name', )



class DeleteTopicSerializer(serializers.ModelSerializer):
  Empty = serializers.ReadOnlyField(required = False)

  def delete(self, validated_data):
    #Set this so that it deletes all of the cards inside of the topic first. 
    get_object_or_404(Topic, id = validated_data).delete()
    # temp = Topic.objects.get(id = validated_data).delete()
    return

  class Meta: 
    model = Topic
    fields = ('Empty',)

    

class EditTopicSerializer(serializers.ModelSerializer):
  switchPosition= serializers.IntegerField(required = False)
  Name = serializers.CharField(required = False)

  def validate(self, data):
    if not 'switchPosition' in data and not 'Name' in data:
        raise serializers.ValidationError("They are both required.")
    return data
  
  def update(self, validated_data, pk):

    record = get_object_or_404(Topic, id = pk)
    
    #If we are only changing the name

    def nameChange():
      record.Name = validated_data['Name']
      record.save()

    def positionChange():
      otherRecord = get_object_or_404(Topic, id = validated_data['switchPosition'])
      otherRecord.Position, record.Position = record.Position, otherRecord.Position
      record.save()
      otherRecord.save()


    if('Name' in validated_data and not 'switchPosition' in validated_data):
      
      nameChange()
      return ({'Data': {'Name': record.Name}})

    #If we are only changing position
    if(not 'Name' in validated_data and 'switchPosition' in validated_data):
      positionChange()
      
      return ({'Data': {'Position': record.Position}})

    #If we are changing both
    if('Name' in validated_data and 'switchPosition' in validated_data):
      nameChange()
      positionChange()

      return ({'Data': {'Name': record.Name, 'Position': record.Position}})

  class Meta:
    model = Topic
    fields = ('Name', 'switchPosition' )
    extra_kwargs = {'switchPosition': {'write_only': True}}


class GetSubclassSerializer(serializers.ModelSerializer):

  def get(self, validated_data):

    res = [i for i in Subclass_Relationships.objects.values('Child_ID',).filter(Subclass = Subclass.objects.get(id = validated_data['id'])) ]

# Returns all of the Card ID's in a certain subclass. 

    return res


  class Meta:
    model = Subclass
    fields = ('id')


class CreateSubclassSerializer(serializers.ModelSerializer):

  Head = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())
  Cards = serializers.ListField(child = CardListSerializer()) 


  def create(self, validated_data, user):

    sub = Subclass.objects.create(Head = validated_data['Head'],  Email = Users.objects.get(Email = user))

    for i in validated_data['Cards']:
      Subclass_Relationships.objects.create(Subclass = sub.id, Email = Users.objects.get(Email = user), Child_ID = i)

    return


  class Meta:
    model = Subclass
    fields = ('Head', 'Cards')


class EditSubclassSerializer(serializers.ModelSerializer):

  Add = serializers.ListField(child = CardListSerializer()) 
  Remove = serializers.ListField(child = CardListSerializer()) 

  # Only edits from the perspective of the parent. There is both addition and removal. 

  def update(self, validated_data, pk, user):
    # PK is the ID of the subclass.     

    #First add...

    for i in validated_data['Add']:
      Subclass_Relationships.objects.create(Email = Users.objects.get(Email = user), Subclass = Subclass.objects.get(id = pk), Child_ID = i)

    #Then Delete

    for j in validated_data['Remove']:
      Subclass_Relationships.objects.filter(Subclass = Subclass.objects.get(id = pk), Child_ID = i ).delete()

    return 

  class Meta:
    model = Subclass
    fields = ('Add', 'Remove')


class DeleteSubclassSerializer(serializers.ModelSerializer):
  Empty = serializers.ReadOnlyField(required = False)

  def destroy(self, pk):

    #Destroys the subclass. 

    Subclass.objects.filter(id = pk).delete()

    return

  class Meta:
    model = Subclass
    fields = ('Empty')


class GetSubclassRelationshipSerializer(serializers.ModelSerializer):
  Card = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())

  # Gets both subclasses that start with this card as well as subclasses this card is a part of. 

  

  class Meta:
    model = Subclass_Relationships
    fields = ('Card')




class CreateSubclassRelationshipSerializer(serializers.ModelSerializer):

  Subclass = serializers.PrimaryKeyRelatedField(queryset = Subclass.objects.all())
  Child_ID = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())


  def create(self, validated_data, user):

    Subclass_Relationships.objects.create(Email = Users.objects.get(Email = user), Subclass = validated_data['Subclass'], Child_ID = validated_data['Child_ID'])

    return

  class Meta:
    model = Subclass_Relationships
    fields = ('Subclass', 'Child_ID')


class RemoveSubclassRelationshipSerializer(serializers.ModelSerializer):
  Empty = serializers.Field(required = False)

  def destroy(self, pk):
    
    Subclass_Relationships.objects.get(id = pk).delete()

    return


  class Meta:
    model = Subclass_Relationships
    fields  = ('Empty')


class TopicRelationshipsSerializer(serializers.ModelSerializer):

  

  class Meta:
    model = Topic_Relationships
    fields = ('Type', 'Parent_ID', 'Child_ID')

class CardRelationshipsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Card_Relationships
    fields = ('Type', 'Parent_ID', 'Child_ID')
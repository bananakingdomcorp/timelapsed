# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Date_Range, Card, Subclass, Topic_Relationships,  Subclass_Relationships

from datetime import datetime
from django.shortcuts import get_object_or_404
from searchapp import search


class CardListSerializer(serializers.ListField):
#Just a generic serializer for any lists of card ID's 

  child = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())


#### Users Serializers


class UsersSerializer(serializers.ModelSerializer):
  Email = serializers.EmailField()

  class Meta:
    model = Users
    fields = ('Email',)

  def create(self, validated_data):
    return super().create(validated_data)


#### Topic Serializers

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
        raise serializers.ValidationError("One is required!.")
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



#### Card Serializers


class CreateCardDataSerializer(serializers.ModelSerializer):
  Topic = serializers.PrimaryKeyRelatedField(queryset = Topic.objects.all())

  class Meta: 
    model = Card
    fields = ('Name', 'Description', 'Topic', )

class CreateCardTimesSerializer(serializers.ModelSerializer):

  Day = serializers.CharField()
  Begin_Date = serializers.DateTimeField()
  Num_Weeks = serializers.IntegerField(required = False, default = 0 )
  Weeks_Skipped = serializers.IntegerField(required = False, default = 0)
  Begin_Time = serializers.TimeField()
  End_Time = serializers.TimeField()

  def validate(self, data):
    if not 'Day' in data or not 'Begin_Date' in data or not 'Begin_Time' in data or not 'End_Time' in data:
      raise serializers.ValidationError('Invalid request')
    valid_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if data['Day'] not in valid_days:
      raise serializers.ValidationError('Must Enter a valid day')
    return data

  class Meta:
    model = Date_Range
    fields = ('Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time', )



class CreateCardSerializer(serializers.ModelSerializer):

  Data = CreateCardDataSerializer()
  Times = serializers.ListField(child=CreateCardTimesSerializer(), required = False, allow_empty = False)

  def create(self, validated_data, user):
    info = validated_data['Data']


    pos =  Card.objects.values('Position').filter(Topic = info['Topic']).order_by('-Position').first()
    if pos == None:
      pos = 0
    else :
      pos = pos['Position']
    n =  Card.objects.create(Name = info['Name'], Description = info['Description'], Position = pos +1 , Email = Users.objects.get(Email = user), Topic = Topic.objects.get(id = info['Topic']))
    res = {'Data': {'Name': n.Name, 'Description': n.Description}}

##Right now creating elasticsearch card before we create our times. We'll see how that works. 

    esCard =  search.ElasticSearchCard(Name = n.Name, Description = n.Description, Topic = Topic.objects.get(id = info['Topic']).Name)
    esCard.meta.id = n.id
    esCard.save()


    if validated_data.get('Times'):
      for times in validated_data['Times']:
        ids = []
        a = Date_Range.objects.create(Day = times['Day'], Begin_Date = times['Begin_Date'], Num_Weeks = times['Num_Weeks'], Weeks_Skipped = times['Weeks_Skipped'], Begin_Time = times['Begin_Time'], End_Time = times['End_Time'], Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = n.id) )
        ids.append(a.id)
        res['Data'] = {'ids': ids}

    res['Data']['id'] = n.id
    return (res)

  class Meta:
    model = Card
    fields = ('Data', 'Times')


class EditCardTimesSerializer(serializers.ModelSerializer):
  Num_Weeks = serializers.IntegerField()
  Weeks_Skipped = serializers.IntegerField()
  Begin_Time = serializers.TimeField()
  End_Time = serializers.TimeField()  
  id = serializers.PrimaryKeyRelatedField(queryset = Date_Range.objects.all(),)

  def validate(self, data):
    if not 'Num_Weeks' in data or not 'Weeks_Skipped' in data or not 'Begin_Time' in data or not 'End_Time' in data or not 'id' in data:
      raise serializers.ValidationError('Invalid request')
    return data  

  class Meta:
    model = Date_Range
    fields = ('Begin_Time', 'End_Time', 'Num_Weeks', 'Weeks_Skipped', 'id')


class DeleteCardTimesSerializer(serializers.ListField):
  child = serializers.PrimaryKeyRelatedField(queryset = Date_Range.objects.all(), )


class UpdateCardTimesSerializer(serializers.Serializer):
  Edit = serializers.DictField(child = EditCardTimesSerializer(),)
  Add = serializers.ListField(child = CreateCardTimesSerializer(),)
  Delete = DeleteCardTimesSerializer()


  class Meta:
    model = Date_Range
    # fields = ('Delete',)
    exclude = ('Add', 'Edit')


class UpdateCardDataSerializer(serializers.ModelSerializer):
  Switch_Topic = serializers.PrimaryKeyRelatedField(queryset = Topic.objects.all(), required = False)
  Switch_Position = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all(), required = False)
  Description = serializers.CharField(required = False,)
  Name = serializers.CharField(required = False,)

  def validate(self, data):
    if not 'Name' in data and not 'Description' in data and not 'Switch_Topic' in data and not 'Switch_Position' in data:
        raise serializers.ValidationError("Data cannot be empty.")
    return data

  class Meta: 
    model = Card
    fields = ('Name', 'Description', 'Switch_Topic', 'Switch_Position' )


class UpdateCardSerializer(serializers.ModelSerializer):
  Data = UpdateCardDataSerializer(required = False)
  Times = UpdateCardTimesSerializer(required = False,)

  def validate(self, data):
    if not 'Data' in data and not 'Times' in data:
        raise serializers.ValidationError("Either Data or Times are required.")
    return data
  
  def update(self, validated_data, pk, user):
    
    temp =  get_object_or_404(Card, id = pk)
    res = {}

    if 'Data' in validated_data:
      
      #If there is a topic change. 

      if 'Switch_Topic' in validated_data['Data']:

        pos =  Card.objects.values('Position').filter(Topic = validated_data['Data']['Switch_Topic']).order_by('-Position').first()
        #If there are no cards in the topic. 
        if pos == None:
          pos = 0
        else :
          pos = pos['Position'] +1        
        Topic_Switch = Topic.objects.get(id = validated_data['Data']['Switch_Topic'])
        temp.Topic = Topic_Switch
        temp.Position = pos

      #If there is a position change. 
      
      if 'Switch_Position' in validated_data['Data']:

        switch = Card.objects.get(id = validated_data['Data']['Switch_Position'])
        switch.Position, temp.Position = temp.Position, switch.Position
        switch.save()

        pass

      if 'Name' in validated_data['Data']:
        
        temp.Name = validated_data['Data']['Name']
      
      if 'Description' in validated_data['Data']:

        temp.Description = validated_data['Data']['Description']



      temp.save()

    res['Data'] = {'Name' : temp.Name, 'Description' : temp.Description}

    change = search.ElasticSearchCard.get(id = pk)   
    change.update(Name = temp.Name, Description = temp.Description, Topic = temp.Topic.Name )


    if 'Times' in validated_data:


    #Handle Deletions:

      for key in validated_data['Times']['Delete']:
        Date_Range.objects.filter(id = key).delete()

      #Handle Edits:

      for key in validated_data['Times']['Edit']:

          
        Date_Range.objects.filter(id = validated_data['Times']['Edit'][key]['id']).update(Begin_Time = validated_data['Times']['Edit'][key]['Begin_Time'], End_Time = validated_data['Times']['Edit'][key]['End_Time'], Num_Weeks =  validated_data['Times']['Edit'][key]['Num_Weeks'], Weeks_Skipped = validated_data['Times']['Edit'][key]['Weeks_Skipped'])


      #Handle Additions:

      for key in validated_data['Times']['Add']:
        ids = []
        a = Date_Range.objects.create(Day = key['Day'], Begin_Date = key['Begin_Date'], Num_Weeks = key['Num_Weeks'], Weeks_Skipped = key['Weeks_Skipped'], Begin_Time = key['Begin_Time'], End_Time = key['End_Time'], Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = pk) )
        ids.append(a.id)
        
      Return_Times =[j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = pk)).order_by('Begin_Date') ]
      res['Data']['Return_Times']= Return_Times
    
    return res

  class Meta:
    model = Card
    fields = ('Data', 'Times')



class DeleteCardSerializer(serializers.ModelSerializer):
  def destroy(self, pk):
    #Deletes any times associated with said card via cascade. 

    temp = get_object_or_404(Card, id = pk)
    temp.delete()

    remove = search.ElasticSearchCard.get(id = pk)
    remove.delete()

    return 'Deleted'
  
  class Meta: 
    model = Card
    fields = ('id',)



class GetSubclassSerializer(serializers.Serializer):

  def get(self, pk):
    
    sub = get_object_or_404(Subclass, id =  pk)

    res = [i['Child_ID'] for i in Subclass_Relationships.objects.values('Child_ID',).filter(Subclass = sub) ]

# Returns all of the Card ID's in a certain subclass. 

    return res


class CreateSubclassSerializer(serializers.ModelSerializer):

  Head = serializers.PrimaryKeyRelatedField(queryset = Card.objects.all())
  Cards = CardListSerializer(required = False)


  def create(self, validated_data, user):

    sub = Subclass.objects.create(Head = Card.objects.get(id = validated_data['Head']),  Email = Users.objects.get(Email = user))

    res = {'Data': {'id' : sub.id} }

    if 'Cards' in validated_data:
      temp = []
      for i in validated_data['Cards']:
        created = Subclass_Relationships.objects.create(Subclass = Subclass.objects.get(id = sub.id), Email = Users.objects.get(Email = user), Child_ID = Card.objects.get(id = i))
        temp.append(created.id)
      res['Data']['Children'] = temp

    return res


  class Meta:
    model = Subclass
    fields = ('Head', 'Cards')


class EditSubclassSerializer(serializers.ModelSerializer):

  Add = CardListSerializer(required = False)
  Remove = CardListSerializer(required = False)

  # Only edits from the perspective of the parent. There is both addition and removal. 

  def validate(self, data):
    if not 'Add' in data and not 'Remove' in data:
        raise serializers.ValidationError("One is required!")

    return data  

  def update(self, validated_data, pk, user):
    # PK is the ID of the subclass.     

    sub = get_object_or_404(Subclass, id = pk)

    if 'Remove' in validated_data:
      for j in validated_data['Remove']:
        deleted = Subclass_Relationships.objects.get(Subclass = Subclass.objects.get(id = sub.id), Email = Users.objects.get(Email = user), Child_ID = Card.objects.get(id = j) ).delete()

    if 'Add' in validated_data:
      temp = []
      for i in validated_data['Add']:
        if Card.objects.get(id = i) != sub.Head or Subclass_Relationships.objects.filter(Subclass =  Subclass.objects.get(id = sub.id), Email = Users.objects.get(Email = user),Child_ID = Card.objects.get(id = i)).count() > 0:
          created = Subclass_Relationships.objects.create(Subclass = Subclass.objects.get(id = sub.id), Email = Users.objects.get(Email = user), Child_ID = Card.objects.get(id = i))
          temp.append(created.id)
      return temp
    
    return

  class Meta:
    model = Subclass
    fields = ('Add', 'Remove')


class DeleteSubclassSerializer(serializers.Serializer):

  def destroy(self, pk):

    #Destroys the subclass. 

    to_destroy = get_object_or_404(Subclass, id = pk)

    to_destroy.delete()

    return


# class UpdateCardRelationshipsSerializer(serializers.ModelSerializer):

#   class Meta:
#     model = Card_Relationships
#     fields = ('Type', 'Parent_ID', 'Child_ID')



# class DeleteCardRelationshipsSerializer(serializers.ModelSerializer):

#   class Meta:
#     model = Card_Relationships
#     fields = ('Type', 'Parent_ID', 'Child_ID')




class TopicRelationshipsSerializer(serializers.ModelSerializer):

  

  class Meta:
    model = Topic_Relationships
    fields = ('Type', 'Parent_ID', 'Child_ID')

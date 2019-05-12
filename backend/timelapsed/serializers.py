# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Event, Date_Range, Card

from datetime import datetime


class UsersSerializer(serializers.ModelSerializer):

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
  
  def update(self, instance, validated_data):
    print(instance, validated_data)
    return
  
  class Meta:
    model = Date_Range
    fields = ('Begin_Time', 'End_Time', 'Num_Weeks', 'Weeks_Skipped')


class DeleteCardTimesSerializer(serializers.ListField):
  child = serializers.CharField()


class UpdateCardTimesSerializer(serializers.Serializer):
  Edit = EditCardTimesSerializer()
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
  # Times = serializers.ListField(child=CreateCardTimesSerializer(), required = False)
  Times = UpdateCardTimesSerializer(required = False,)

  
  def update(self, validated_data, pk, user):

    info = validated_data['Data']
    times = validated_data['Times']
    temp = Card.objects.values('Topic', 'Position').filter(id = pk).first()
    res = {}

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

    # for key in times['Delete']:
    #   Date_Range.objects.filter(id = key).delete()

    #Handle Edits:



    #Handle Additions:

    # for key in times['Add']:
    #   ids = []
    #   a = Date_Range.objects.create(Day = key['Day'], Begin_Date = key['Begin_Date'], Num_Weeks = key['Num_Weeks'], Weeks_Skipped = key['Weeks_Skipped'], Begin_Time = key['Begin_Time'], End_Time = key['End_Time'], Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = n.id) )
    #   ids.append(a.id)
    #   res['Added_Times'] = {'ids': ids}
        

    return res

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


class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model: Card
    fields = ('Name', 'Description', 'Position', 'Email', 'Topic')


class AddTopicSerializer(serializers.ModelSerializer):

  def create(self, validated_data, user):
    # first, find the proper position. We can just add from the previous highest position.
    pos = Topic.objects.values('Position').filter(Email = user).order_by('-Position').first()

    n = Topic.objects.create(Name = validated_data['Name'], Position = pos['Position'] + 1, Email = Users.objects.get(Email = user))
    return({'Data': {'id': n.id, 'Name': validated_data['Name'], 'Cards': [] }})

  class Meta:
    model = Topic
    fields =  ('Name', )



class DeleteTopicSerializer(serializers.ModelSerializer):

  def delete(self, validated_data):
    temp = Topic.objects.get(id = validated_data).delete()
    return

  class Meta: 
    model = Topic
    fields = ('id',)

    

class EditTopicSerializer(serializers.ModelSerializer):
  switchPosition= serializers.IntegerField(required = False)
  Name = serializers.CharField(required = False)

  
  def update(self, validated_data, pk):

    record = Topic.objects.get(id = pk)
    #If we are only changing the name

    if('Name' in validated_data and not 'switchPosition' in validated_data):
      record.Name = validated_data['Name']
      record.save()
      return

    #If we are only changing position
    if(not 'Name' in validated_data and 'switchPosition' in validated_data):

      otherRecord = Topic.objects.get(id = validated_data['switchPosition'])
      temp = record.Position
      record.Position = otherRecord.Position
      otherRecord.Position = temp
      record.save()
      otherRecord.save()
      return

    #If we are changing both
    if('Name' in validated_data and 'switchPosition' in validated_data):
      record.Name = validated_data['Name']
      otherRecord = Topic.objects.get(id= validated_data['switchPosition'])
      temp = record.Position
      record.Position = otherRecord.Position
      otherRecord.Position = temp
      record.save()
      otherRecord.save()

      return

  class Meta:
    model = Topic
    fields = ('Name', 'switchPosition' )
    extra_kwargs = {'switchPosition': {'write_only': True}}



class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'User')

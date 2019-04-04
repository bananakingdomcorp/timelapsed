# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Event, Date_Range, Card


class UsersSerializer(serializers.ModelSerializer):

  class Meta:
    model = Users
    fields = ('Email',)

  def create(self, validated_data):
    return super().create(validated_data)

class CreateCardDataSerializer(serializers.Serializer):
  Topic: serializers.IntegerField(source = 'Data_Topic')
  Name: serializers.CharField(source = 'Data_Name')
  Description: serializers.CharField(source = 'Data_Description')




class CreateCardSerializer(serializers.ModelSerializer):

  Data = CreateCardDataSerializer(source = '*')
  


  class Meta:
    model = Card
    fields = ('Data')



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

  #clean this up into services or multiple serializers. 

  
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

class DateRangeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Date_Range
    fields = ('id', 'User', 'Event_ID', 'Card_ID', 'Begin_Date', 'End_Date', 'Begin_Time', 'End_Time', 'Day')
# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Event, Date_Range, Card


class UsersSerializer(serializers.ModelSerializer):

  class Meta:
    model = Users
    fields = ('Email',)

  def create(self, validated_data):
    return super().create(validated_data)


class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ('id','User', 'Topic', 'Name', 'Description', 'Position', 'Expected_Finish')



class AddTopicSerializer(serializers.ModelSerializer):

  def create(self, validated_data, user):
    # first, find the proper position. We can just add from the previous highest position.
    pos = Topic.objects.values('Position').filter(Email = user).order_by('-Position').first()

    n = Topic.objects.create(Name = validated_data['Name'], Position = pos['Position'] + 1, Email = Users.objects.get(Email = user))
    return({n.id: [validated_data['Name'], []]})
    # return ({'Name' : validated_data['Name'], 'id': str(n.id)})

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
  switchPosition= serializers.CharField()


  def update(self, validated_data, pk):


    #If we are only changing the name

    if('Name' in validated_data and not 'switchPosition' in validated_data):
      

      print('NAME CHANGE ONLY')

    #If we are only changing position
    if(not 'Name' in validated_data and 'switchPosition' in validated_data):
      print('POSITON CHANGE ONLY')


    #If we are changing both
    if('Name' in validated_data and 'switchPosition' in validated_data):
      print('BOTH')

  class Meta:
    model = Topic
    fields = ('Name', 'switchPosition' )
    extra_kwargs = {'switchPosition': {'write_only': True}}




class SwitchTopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = ('Name', 'id', 'position')

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'User')

class DateRangeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Date_Range
    fields = ('id', 'User', 'Event_ID', 'Card_ID', 'Date', 'Begin_Time', 'End_Time')
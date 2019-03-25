# Serialize to/from JSON here

from rest_framework import serializers

from .models import Users, Topic, Event, Date_Range, Card


class GetUserTopics(serializers.ModelSerializer):

  class Meta:
    model = Topic

class GetTopcCards(serializers.ModelSerializer) :

  class Meta:
    model = Card

class UsersSerializer(serializers.ModelSerializer):
  #Something here to find all cards/topics, then place into a list. 
  def create(self, validated_data):
    return super().create(validated_data)


  class Meta:
    model = Users
    fields = ('Email',)


class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ('id','User', 'Topic', 'Name', 'Description', 'Position', 'Expected_Finish')

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields =  ('id','User', 'Name', 'Position')

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'User')

class DateRangeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Date_Range
    fields = ('id', 'User', 'Event_ID', 'Card_ID', 'Date', 'Begin_Time', 'End_Time')
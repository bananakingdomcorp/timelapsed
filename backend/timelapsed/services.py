#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card


def get_user_information(data):

  temp = Topic.objects.values().filter(Email = data['Email']).order_by('Position')
  return list(temp)

  
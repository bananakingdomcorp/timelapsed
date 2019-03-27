#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card


def get_user_information(data):
  temp = Topic.objects.all().filter(Email = data.email).order_by(position)
  return list(temp)

  
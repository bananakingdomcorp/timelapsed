# This file is for the placement of Django Signals. These are used as the engine to run our relationships. 

from ..models import Card


from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def test_signals(sender, **kwargs):
  print('SIGNAL FOUND')
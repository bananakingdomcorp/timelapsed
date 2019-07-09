from django.apps import AppConfig


class TimelapsedConfig(AppConfig):
  name = 'timelapsed'
  def ready(self):
      print("at ready")
      import timelapsed.signals.signals
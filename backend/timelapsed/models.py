from django.urls import reverse
from django.db.models import BigAutoField
from django.db.models import DateField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import TextField
from django.db.models import TimeField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class Users(models.Model):

    # Fields
    Email = models.EmailField(primary_key=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_users_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_users_update', args=(self.pk,))


class Topic(models.Model):

    # Fields
    Name = models.TextField(max_length=100)
    Position = models.IntegerField()
    id = models.BigAutoField(primary_key=True)

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="topics", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_topic_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_topic_update', args=(self.pk,))


class Event(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="events", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_event_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_event_update', args=(self.pk,))


class Date_Range(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    Date = models.DateField()
    Begin_Time = models.TimeField()
    End_Time = models.TimeField()

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="dateranges", 
    )
    Event_ID = models.ForeignKey(
        'timelapsed.Event',
        on_delete=models.CASCADE, related_name="dateranges", null=True
    )
    Card_ID = models.ForeignKey(
        'timelapsed.Card',
        on_delete=models.CASCADE, related_name="dateranges", null=True
    )
    def save(self, *args, **kwargs):
      if not self.Event_ID and not self.Card_ID:
        raise Exception("You can't leave both fields as null")
      if self.Event_ID and self.Card_ID:
        raise Exception("You have to have one field as null")
      super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_daterange_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_daterange_update', args=(self.pk,))


class Card(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    Name = models.TextField()
    Description = models.TextField()
    Position = models.IntegerField()
    Expected_Finish = models.DateField()

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="cards", 
    )
    Topic = models.ForeignKey(
        'timelapsed.Topic',
        on_delete=models.CASCADE, related_name="cards", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_card_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_card_update', args=(self.pk,))



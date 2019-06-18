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
from django.utils.timezone import now


class Users(models.Model):

    # Fields
    Email = models.EmailField(primary_key=True)

    def save(self, *args, **kwargs):
        super().full_clean()
        super().save(*args, **kwargs)    

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

    def save(self, *args, **kwargs):
      super().full_clean()
      super().save(*args, **kwargs)    

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_topic_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_topic_update', args=(self.pk,))


class Date_Range(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    Day = models.TextField(max_length=100,)
    Begin_Date = models.DateTimeField()
    Num_Weeks = models.IntegerField(default = 0,)
    Weeks_Skipped = models.IntegerField(default = 0,)
    Begin_Time = models.TimeField()
    End_Time = models.TimeField()

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="dateranges", 
    )
    Card_ID = models.ForeignKey(
        'timelapsed.Card',
        on_delete=models.CASCADE, related_name="dateranges", null=True
    )
    def save(self, *args, **kwargs):
      days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
      if self.Day not in days:
        raise Exception("You are not entering a valid day of the week")

      super().full_clean()
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

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="cards", 
    )
    Topic = models.ForeignKey(
        'timelapsed.Topic',
        on_delete=models.CASCADE, related_name="cards", 
    )

    def save(self, *args, **kwargs):
      super().full_clean()
      super().save(*args, **kwargs)        

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_card_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('timelapsed_card_update', args=(self.pk,))


class Subclass(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="subclass", 
    )

    Head = models.ForeignKey(
      'timelapsed.Card',
      on_delete = models.CASCADE, related_name = 'subclass',
    )

    def save(self, *args, **kwargs):
      super().full_clean()
      super().save(*args, **kwargs)        

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_subclass_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('timelapsed_subclass_update', args=(self.pk,))


class Subclass_Relationships(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="Subclass_Relationship", 
    )

    Subclass = models.ForeignKey(
      'timelapsed.Subclass',
      on_delete=models.CASCADE, related_name = 'Subclass_Relationship'
    )

    Child_ID = models.ForeignKey(
      'timelapsed.Card',
      on_delete=models.CASCADE, related_name="Subclass_Relationship", null=True
    )
    
    def save(self, *args, **kwargs):
     #have exception for self subclassing here. 

      super().full_clean()   
      super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_subclass_relationship_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('timelapsed_subclass_relationship_update', args=(self.pk,))



class Card_Relationships(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    Type = models.TextField()

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="card_relationships", 
    )
    Parent_ID = models.ForeignKey(
      'timelapsed.Card',
      on_delete=models.CASCADE, related_name="card_relationships_parent", null=True
    )
    Child_ID = models.ForeignKey(
      'timelapsed.Card',
      on_delete=models.CASCADE, related_name="card_relationships_child", null=True
    )

    def save(self, *args, **kwargs):
      if self.Parent_ID == self.Child_ID:
        raise Exception("You cannot have a relationship with yourself")   
      super().full_clean()           
      super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_card_relationships_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('timelapsed_card_relationships_update', args=(self.pk,))



class Topic_Relationships(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    # Relationship Fields
    Email = models.ForeignKey(
        'timelapsed.Users',
        on_delete=models.CASCADE, related_name="topic_relationships", 
    )
    Parent_ID = models.ForeignKey(
      'timelapsed.Topic',
      on_delete=models.CASCADE, related_name="topic_relationships_parent", null=True
    )
    Child_ID = models.ForeignKey(
      'timelapsed.Topic',
      on_delete=models.CASCADE, related_name="topic_relationships_child", null=True
    )
    def save(self, *args, **kwargs):
      if self.Parent_ID == self.Child_ID:
        raise Exception("You cannot relate to yourself")   

      super().full_clean()           
      super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('timelapsed_topic_relationships_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('timelapsed_topic_relationships_update', args=(self.pk,))



# Generated by Django 2.2.1 on 2019-05-24 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelapsed', '0008_date_range_begin_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_Relationships',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Type', models.TextField()),
                ('Child_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_relationships_child', to='timelapsed.Card')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_relationships', to='timelapsed.Users')),
                ('Parent_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_relationships_parent', to='timelapsed.Card')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Subclass',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subclass', to='timelapsed.Users')),
                ('Head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subclass', to='timelapsed.Card')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Subclass_Relationships',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Child_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subclass_Relationship', to='timelapsed.Card')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subclass_Relationship', to='timelapsed.Users')),
                ('Subclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subclass_Relationship', to='timelapsed.Subclass')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Topic_Relationships',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Child_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_relationships_child', to='timelapsed.Topic')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_relationships', to='timelapsed.Users')),
                ('Parent_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_relationships_parent', to='timelapsed.Topic')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.RemoveField(
            model_name='date_range',
            name='Event_ID',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
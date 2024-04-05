# Generated by Django 5.0.3 on 2024-04-03 01:11

from django.db import migrations

def populate_role(apps, schemaeditor):
    entries = {
        "developer": "The person on the team who deveelops",
        "product owner": "The person who is responsible for defining what gets uilt",
        "scrum master": "The teams coach"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team)
    ]
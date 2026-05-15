# Models for users, teams, activities, leaderboard, and workouts (MongoDB will be used, so models are for DRF validation)

from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    # Add additional fields as needed
    def __str__(self):
        return self.username

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayField(model_container=User)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

gameChoice=(
        ("","----"),
        ("t","Tourney"),
        ("f","fake News"),
        )
class Instance(models.Model):
    instanceID=models.CharField(max_length=10)
    game=models.CharField(choices=gameChoice,max_length=50)
    def __str__(self):
           return   self.instanceID
class Person(models.Model):
    name=models.CharField(max_length=10)
    instance=models.ForeignKey(Instance)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.name




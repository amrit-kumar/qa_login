import datetime
from django.db import models
from django.utils import timezone




class Question(models.Model):
    question = models.CharField( max_length=100, blank = True, null = True)
    #user = models.ForeignKey(User, blank=True, null=True)
    username=models.CharField(max_length=35,null=True)
    #pub_date = models.DateTimeField('date published',null=)

    def __str__(self):
        return str(self.question)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text= models.CharField( max_length=500, blank= True, null = True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


    def __str__(self):
        return str(self.answer_text)

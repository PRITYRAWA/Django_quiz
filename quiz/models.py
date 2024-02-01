from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

# Create your models here.

class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'),('D', 'D')])

    def __str__(self):
        return self.question_text
    
    


class UserResponse(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s response to {self.question}"
from django.db import models

# MY MODELS
class WorkExp(models.Model):
    Place = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Duties = models.TextField()
    DateFrom = models.DateField()
    DateTo = models.DateField()

    def __str__(self):
        return self.Position


class Education(models.Model):
    Place = models.CharField(max_length=150)
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    DateFrom = models.DateField()
    DateTo = models.DateField()

    def __str__(self):
        return self.Name


class Messages(models.Model):
    UserName = models.CharField(max_length=30)
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self):
        return self.UserName
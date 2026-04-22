from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=10)
    maths = models.FloatField()
    science = models.FloatField()
    english = models.FloatField()
    start = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ({self.age})"



from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    start = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ({self.age})"



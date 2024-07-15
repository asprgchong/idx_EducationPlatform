from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model): 
    # fields of the model 
    course_id = models.IntegerField(null=True)
    course = models.IntegerField(null=True)
    lesson_name = models.CharField(max_length=200, null=True) 
    lesson_num = models.IntegerField(primary_key=True)
    description = models.TextField(null=True) 
    topics = models.TextField(null=True)
    activites = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True) 
    lesson_content = models.URLField(null=True)
    # https://stackoverflow.com/questions/60175280/how-to-display-videos-in-homepage-from-database-in-django video
    def __str__(self):
        return self.lesson_name
    
    def topics_as_list(self):
        return self.topics.split('-')
    
    def activites_as_list(self):
        return self.activites.split(':')
    

class Student(models.Model): 
    # fields of the model 
    userName = models.CharField(max_length=200, null=True,) 
    firstName = models.CharField(max_length=200, null=True,) 
    lastName = models.CharField(max_length=200, null=True,) 
    courseEnrolled = models.CharField(max_length=200, null=True,) 
    cid = models.IntegerField(null=True, db_column="cid") 
    valid = models.BooleanField(default=0)
    # # renames the instances of the model 
    # # with their title name 
    # def __str__(self): 
    #     return self.title 
    def __str__(self):
        return self.userName
    
    def full_name(self):
        return self.firstName + " " + self.lastName
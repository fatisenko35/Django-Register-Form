from django.db import models

# Create your models here.
class Student(models.Model):
    Full_Name = models.CharField(max_length=200)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=50)

    GENDER = (
        
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),

    )

    Gender = models.CharField(max_length=50, choices=GENDER)
    Student_Number = models.IntegerField(unique=True, null=True, blank=True)

    PATH = (
       
        ("Full Stack", "Full Stack"),
        ("AWS-DevOps", "AWS-DevOps"),
        ("Data Science", "Data Science"),
        ("Cyber Security", "Cyber Security"),
    )

    Path = models.CharField(max_length=20, choices=PATH)

    def __str__(self):
        return f"{self.Full_Name} {self.Student_Number}"
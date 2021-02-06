from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
from django.db import models
Gender_choice={
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
}
# for registration of associates
class reg_table(models.Model):
    aid= models.IntegerField()
    fname=models.CharField(max_length=100)
    birthdate=models.DateField(auto_now=False, auto_now_add=False)
    email=models.EmailField()
    nationality=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    gender = models.CharField(choices=Gender_choice,  max_length=100)
    joiningdate=models.DateField(auto_now=False, auto_now_add=False)
    password=models.CharField(max_length=100)
    confirmpass=models.CharField(max_length=100)
    class fetch:
        db_table="test3app_reg_table"

    def __str__(self):
       return "{}-{}".format(self.fname,self.location,self.aid,self.email)

    def isExits(self):
        email=self.email
        if reg_table.object.filter(email):
            return True
        else:
            return False

    def aidExits(self):
        aid = self.aid
        if reg_table.object.filter(aid):
            return True
        else:
            return False
# for login of admin
class log_table(models.Model):
    loginid = models.CharField(max_length=10)
    loginpass = models.CharField(max_length=100)

    class fetch:
        db_table = "test3app_log_table"

# for registration of admin
class AdminTable(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    confirmpass=models.CharField(max_length=100)
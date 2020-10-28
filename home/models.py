from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField() 



 
 
class Reliefcamp(models.Model):
    
    img = models.ImageField(upload_to='pics')
    cityname = models.CharField(max_length=122)
    desc = models.TextField()
    people = models.IntegerField()


class Aboutngo(models.Model):  #made for about us but did not use
    
    img = models.ImageField(upload_to='pics')
    ngoname = models.CharField(max_length=122)
    desc = models.TextField()



class Data1(models.Model):
    
    
    name = models.CharField(max_length=122)
    loc = models.CharField(max_length=122)
    cause = models.CharField(max_length=122)
    death =  models.IntegerField()
    damage = models.CharField(max_length=122)

class Data2(models.Model):
    
    
    name = models.CharField(max_length=122)
    loc = models.CharField(max_length=122)
    cause = models.CharField(max_length=122)
    death =  models.IntegerField()
    damage = models.CharField(max_length=122)

class Data3(models.Model):
    
    
    name = models.CharField(max_length=122)
    loc = models.CharField(max_length=122)
    cause = models.CharField(max_length=122)
    death =  models.IntegerField()
    damage = models.CharField(max_length=122)     


class Data4(models.Model):
    
    
    name = models.CharField(max_length=122)
    loc = models.CharField(max_length=122)
    cause = models.CharField(max_length=122)
    death =  models.IntegerField()
    damage = models.CharField(max_length=122)
        
class Rivers(models.Model):
    
    img = models.ImageField(upload_to='pics')
    Rivername = models.CharField(max_length=122)
    desc = models.TextField()
    year = models.IntegerField()        

class Location(models.Model):
    name = models.CharField(max_length=122)
    desc1 = models.TextField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=122)

    phone = models.CharField(max_length=12)
    exampleFormControlSelect1 = models.CharField(max_length=122)
    exampleFormControlFile1 = models.ImageField(upload_to='pics')
    date = models.DateField()
    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
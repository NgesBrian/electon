from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class User(models.Model):
#     idUser = models.AutoField( primary_key=True)
#     firstName = models.CharField(max_length=200)
#     secondName = models.CharField(max_length=200)
#     userType = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     creationDate = models.DateTimeField('date published') 

class Elections(models.Model):
    idElection = models.AutoField(primary_key=True)
    User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    voterType = models.CharField(max_length=200)
    electorType = models.CharField(max_length= 200)

# class Login(models.Model):
#     idLogin = models.AutoField(primary_key=True)
#     email = models.CharField(max_length= 200)
#     matricule = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     state = models.CharField(max_length= 200)
#     activationLink = models.CharField(max_length = 200)
 #   User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)

class Candidate(models.Model):
    idCandidate = models.AutoField(primary_key=True)
    position = models.CharField(max_length= 200)

class Voting(models.Model):
    idVoting = models.AutoField(primary_key=True)
    User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    Election_idElection = models.CharField(max_length= 200)

#contact us details 
class Contact(models.Model):
    idContact = models.AutoField(primary_key=True)
    topic = models.CharField(max_length= 200)
    body = models.CharField(max_length= 500)
    email = models.CharField(max_length= 80)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def set_email_as_unique():
    """
    Sets the email field as unique=True in auth.User Model
    """
    email_field = dict([(field.name, field) for field in User._meta.fields])["email"]
    setattr(email_field, '_unique', True)

#this is called here so that attribute can be set at the application load time
set_email_as_unique()
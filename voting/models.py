from django.db import models


class User(models.Model):
    idUser = models.AutoField( primary_key=True)
    firstName = models.CharField(max_length=200)
    secondName = models.CharField(max_length=200)
    userType = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    creationDate = models.DateTimeField('date published')

class Elections(models.Model):
    idElection = models.AutoField(primary_key=True)
    User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    voterType = models.CharField(max_length=200)
    electorType = models.CharField(max_length= 200)

class Login(models.Model):
    idLogin = models.AutoField(primary_key=True)
    email = models.CharField(max_length= 200)
    matricule = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    state = models.CharField(max_length= 200)
    activationLink = models.CharField(max_length = 200)
    User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)

class Candidate(models.Model):
    idCandidate = models.AutoField(primary_key=True)
    position = models.CharField(max_length= 200)

class Voting(models.Model):
    idVoting = models.AutoField(primary_key=True)
    User_idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    Election_idElection = models.CharField(max_length= 200)

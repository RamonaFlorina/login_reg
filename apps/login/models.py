from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Model):
    def reg_validations(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2 or not str.isalpha():
            errors["first_name"] = "First name should be no less than 2 charachters and contain only letters"
        if len(postData["last_name"]) < 2 or not str.isalpha():
            errors["last_name"] = "First name should be no less than 2 charachters and contain only letters"
        if not EMAIL_REGEX.match(postData['email']) or len(postData['email']) < 1:
            errors["email"] = "Email cannot be blank and must be valid"



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email =      models.CharField(max_length=255)
    password =   models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

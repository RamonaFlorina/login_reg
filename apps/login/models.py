from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validations(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "First name should be no less than 2 charachters and contain only letters"
        if len(postData["last_name"]) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "Last name should be no less than 2 charachters and contain only letters"
        if not EMAIL_REGEX.match(postData['email']) or len(postData['email']) < 1:
            errors["email"] = "Email cannot be blank and must be valid"
        user = User.objects.filter(email=postData['email'])
        if user:
            errors['User already exists']
        else:
            if len(postData['password']) < 8:
                errors["password"] = "Password should be at least 8 characters"
            if postData['password'] == postData['confirm_password']:
                print('passwords match')
            else:
                errors['Passwords must match']
        if not errors:
            psswrd = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        return errors

    def login_validations(self, postData):
        errors = {} #create dictionary to store errors
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if not User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email doesn't exists"
            return errors
        user_check = User.objects.get(email=postData['email'])
        print (user_check)

        if not bcrypt.checkpw(postData["password"].encode(), user_check.password.encode()):
            errors['password'] = "Password doesn't match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email =      models.CharField(max_length=255)
    password =   models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

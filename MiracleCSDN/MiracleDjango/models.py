from django.db import models


class USER(models.Model):
    USER_email = models.EmailField()
    USER_password = models.CharField(max_length=20)
    USER_country = models.CharField(max_length=20)
    USER_localLastName = models.CharField(max_length=20)
    USER_localFirstName = models.CharField(max_length=20)
    USER_lastName = models.CharField(max_length=20)
    USER_firstName = models.CharField(max_length=20)
    USER_jobTitle = models.CharField(max_length=20)
    USER_workPhone = models.CharField(max_length=20)
    USER_companyName = models.CharField(max_length=20)
    USER_address1 = models.CharField(max_length=40)
    USER_address2 = models.CharField(max_length=40)
    USER_city = models.CharField(max_length=20)
    USER_state = models.CharField(max_length=20)
    USER_postalCode = models.CharField(max_length=20)
    USER_createdTime = models.DateTimeField()


from django.db import models


class web_user(models.Model):
    USER_ID = models.CharField(max_length=20)
    USER_code = models.CharField(max_length=20)
    USER_name = models.CharField(max_length=20)
    USER_corp = models.CharField(max_length=20)
    USER_phone = models.CharField(max_length=20)
    USER_email = models.CharField(max_length=20)
    USER_address = models.CharField(max_length=40)
    USER_createtime = models.DateTimeField(max_length=20)
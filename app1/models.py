from django.db import models


class voter_user_model(models.Model):
    name = models.CharField(max_length=50)
    voter_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name   


class voter_profile_model(models.Model):
    name = models.OneToOneField(voter_user_model, on_delete=models.CASCADE)
    date_birth = models.DateField()
    gender = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    aadhaar_number = models.BigIntegerField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name.name  

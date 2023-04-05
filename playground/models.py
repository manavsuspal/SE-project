from django.db import models
from django.db.models import Value
from django.db.models.functions import Replace
from django.contrib.auth import get_user_model

User = get_user_model()
stateList = [('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('DL', 'Delhi')]

class Event(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    startTime = models.TimeField(default=None)
    date = models.DateField(default=None)
    footfall = models.IntegerField(default=0)
    venue = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices = stateList, default = 'DL')
    image = models.URLField(default=None)
    slug = models.SlugField(max_length = 255, default=None,blank=True, null=True)

class Registrations(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
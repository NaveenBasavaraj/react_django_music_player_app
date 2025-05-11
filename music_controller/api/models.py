from django.db import models
import string
import random


# Create your models here.

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(string.ascii_uppercase, k=length)
        if not Room.objects.filter(code=code).exists():
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code+" "+self.host
    
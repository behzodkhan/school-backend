from django.db import models

# Create your models here.
class Staff(models.Model):
    roles = [
        ("administrator", "Administrator"),
        ("local", "Local Teacher"),
        ("international", "International Teacher"),
        ("mentor", "Mentor"),
        ("technical", "Technical Staff")
    ]
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=roles, default="local")
    desc = models.TextField()
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/staff", blank=True)
    def __str__(self):
        return self.full_name
from django.db import models
from django.conf import settings

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    bio = models.TextField()
    experience = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')
    available_times = models.JSONField()

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Patient"
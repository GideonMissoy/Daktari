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
    

class Appointment(models.Model):
    APPOINTMENT_TYPES = [
        ('Physical', 'Physical'),
        ('Zoom', 'Zoom'),
    ]

    APPOINTMENT_STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPES)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='Scheduled')
    zoom_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.get_full_name} and {self.patient.user.get_full_name} on {self.scheduled_time}"
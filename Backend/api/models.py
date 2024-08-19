from django.db import models
from django.conf import settings
    

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


class MedicalRecord(models.Model):
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE)
    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    notes = models.TextField()
    prescriptions = models.TextField()  # You could also create a separate model if you want to structure this data further
    diagnosis = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.user.get_full_name} by Dr. {self.doctor.user.get_full_name} on {self.date_created}"


class Payment(models.Model):
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ])
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment of {self.amount} by {self.patient.user.get_full_name} for appointment on {self.appointment.scheduled_time}"
    

class Review(models.Model):
    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.patient.user.get_full_name} for {self.doctor.user.get_full_name} - {self.rating} Stars"
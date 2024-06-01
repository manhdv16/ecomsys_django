from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f'Appointment on {self.appointment_date} with doctor {self.doctor_id}'

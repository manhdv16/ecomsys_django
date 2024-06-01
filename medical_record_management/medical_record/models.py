from django.db import models

class MedicalRecord(models.Model):
    patient_id = models.IntegerField()
    record_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    doctor_id = models.IntegerField()

    def __str__(self):
        return f'Record for patient {self.patient_id} on {self.record_date}'

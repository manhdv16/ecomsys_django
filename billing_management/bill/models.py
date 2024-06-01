from djongo import models

class Invoice(models.Model):
    patient_id = models.IntegerField()
    date_issued = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.id} for patient {self.patient_id}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.amount} for invoice {self.invoice.id}"

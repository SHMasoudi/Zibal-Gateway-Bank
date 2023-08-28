from django.db import models

# Create your models here.



class Transactions(models.Model):
    
    STATUS_TRANSACTION = (
        ('s', 'Successful'),
        ('p','Pending'),
        ('c', 'Cancell'))

    
    Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Amount')
    Status = models.CharField(max_length=1, choices=STATUS_TRANSACTION, verbose_name='Status')
    TransCode = models.CharField(max_length=150, unique=True, verbose_name='TransCode')
    InvoiceNo = models.CharField(max_length=150, null=True, verbose_name='TransInvoiceNo')
    paymentStatus = models.CharField(max_length=10,null=True,verbose_name="StatusCode")
    DateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ("Transactions")
        ordering = ['id']
    def __str__(self):
        return f"Status : {self.Status}"
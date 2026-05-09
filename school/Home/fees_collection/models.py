from django.db import models
from student.models import Student   # তোমার student app

class FeesCollection(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    FEES_TYPE_CHOICES = [
        ('tuition', 'Tuition'),
        ('exam', 'Exam'),
        ('admission', 'Admission'),
        ('others', 'Others'),
    ]

    fees_type = models.CharField(max_length=50, choices=FEES_TYPE_CHOICES)

    fees_amount = models.DecimalField(max_digits=10, decimal_places=2)

    paid_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.fees_type}"

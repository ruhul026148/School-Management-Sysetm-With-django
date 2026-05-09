from django.db import models
from django.utils.text import slugify


class Fees(models.Model):
    # ===== Fees Information =====
    fees_id = models.CharField(max_length=100)
    
    FEES_TYPE_CHOICES = [
        ('monthly fees', 'Monthly Fees'),
        ('admission Fees', 'Admission Fees'),
        ('class test', 'Class Test'),
        ('exam fees', 'Exam Fees'),
        ('hostel fees', 'Hostel Fees'),
        ('other', 'Other'),
    ]
    fees_type = models.CharField(max_length=50, choices=FEES_TYPE_CHOICES)

    # 🔥 Gender remove kore Class add kora holo
    student_class = models.CharField(max_length=100)

    fees_amount = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateField()
    end_date = models.DateField()

    # ===== Extra =====
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.fees_id}-{self.student_class}-{self.start_date}")
        super(Fees, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fees_type} - {self.student_class} ({self.fees_amount})"

from django.db import models
from django.utils.text import slugify


class Salary(models.Model):
    # ===== Basic Info =====
    staff_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    # ===== Personal Info =====
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    joining_date = models.DateField()

    # ===== Financial =====
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # ===== Extra =====
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto Slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.staff_id}-{self.name}-{self.joining_date}")
        super(Salary, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.amount}"
from django.db import models
from django.utils.text import slugify


class Expenses(models.Model):
    # ===== Basic Info =====
    expenses_id = models.CharField(max_length=100, unique=True)
    item_name = models.CharField(max_length=255)

    # ===== Item Details =====
    ITEM_QUALITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    item_quality = models.CharField(max_length=20, choices=ITEM_QUALITY_CHOICES)

    # ===== Financial =====
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # ===== Purchase Info =====
    source_of_purchase = models.CharField(max_length=255)

    # ===== Extra =====
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto Slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.expenses_id}-{self.item_name}")
        super(Expenses, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_name} - {self.expense_amount}"

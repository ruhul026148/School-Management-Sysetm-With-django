from django.db import models
from django.utils.text import slugify


class Department(models.Model):
    # ===== Department Details =====
    department_id = models.CharField(max_length=100, unique=True)
    department_name = models.CharField(max_length=150)
    head_of_department = models.CharField(max_length=150)
    department_start_date = models.DateField()
    no_of_students = models.IntegerField()

    # ===== Extra =====
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.department_name}-{self.department_id}")
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.department_name} ({self.department_id})"

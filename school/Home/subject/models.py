from django.db import models
from django.utils.text import slugify


class Subject(models.Model):
    # ===== Subject Information =====
    subject_id = models.CharField(max_length=100, unique=True)
    subject_name = models.CharField(max_length=150)
    student_class = models.CharField(max_length=100)

    # ===== Extra =====
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.subject_name}-{self.subject_id}")
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject_name} ({self.subject_id})"
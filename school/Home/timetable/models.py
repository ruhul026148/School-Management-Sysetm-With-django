from django.db import models
from django.utils.text import slugify


class TimeTable(models.Model):
    # ===== Time Table Info =====
    teacher_id = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    student_class = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # ===== Extra =====
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.teacher_id}-{self.subject}-{self.date}")
        super(TimeTable, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject} - {self.student_class} ({self.date})"
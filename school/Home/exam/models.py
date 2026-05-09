from django.db import models
from django.utils.text import slugify
from subject.models import Subject   # ✅ fixed import


class Exam(models.Model):
    exam_name = models.CharField(max_length=150)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    fees = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_date = models.DateField()

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.exam_name}-{self.subject.subject_id}-{self.event_date}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.exam_name} - {self.subject.subject_name}"
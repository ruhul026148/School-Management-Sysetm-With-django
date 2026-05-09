from django.db import models
from django.utils.text import slugify

class Teacher(models.Model):
    # ===== Basic Details =====
    teacher_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    )
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=15)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=150)
    experience = models.CharField(max_length=100)

    # ===== Login Details =====
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # later hash করা ভালো

    # ===== Address =====
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    # ===== Extra =====
    teacher_image = models.ImageField(upload_to='teacher/images', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # ===== Auto slug =====
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.teacher_id}")
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.teacher_id})"

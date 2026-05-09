from django.db import models
from django.utils.text import slugify

# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email = models.CharField(max_length=100, unique= True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    mother_email = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    student_id = models.CharField(max_length=100, unique= True,null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')],null=True)
    date_of_birth = models.DateField(null=True)
    student_class = models.CharField(max_length=100,null=True)
    religion = models.CharField(max_length=20,null=True)
    joining_date = models.DateField(null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    admission_number = models.CharField(max_length=15,null=True)
    section = models.CharField(max_length=15,null=True)
    student_image= models.ImageField(upload_to='student/images', blank= True,null=True)
    parent = models.OneToOneField(Parent, on_delete= models.CASCADE,null=True)
    slug = models.SlugField(max_length= 255, unique= True, blank= True,null=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
        
from django.db import models

# Create your models here.

class Categoty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Qualification(models.Model):
    q1 = models.CharField(max_length=500 , null = True , blank = True)
    q2 = models.CharField(max_length=500 , null = True , blank = True)
    q3 = models.CharField(max_length=500 , null = True , blank = True)
    q4 = models.CharField(max_length=500 , null = True , blank = True)

def image_upload(instance ,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):
    job_type =[
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Remotly','Remotly')
    ]


    title = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100 , choices=job_type)
    description = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now_add=True )
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=8 ,decimal_places=2)
    experience = models.IntegerField(default=1)
    job_img = models.ImageField(upload_to = image_upload)
    categoty = models.ForeignKey(Categoty,on_delete=models.CASCADE)
    qualification = models.OneToOneField(Qualification , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
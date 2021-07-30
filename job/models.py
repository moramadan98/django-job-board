from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_positive(value):
    if value <=0:
        raise ValidationError(
            _('%(value)s is incorrect number'),
            params={'value': value},
        )



class Categoty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

       
    



def image_upload(instance ,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):
    job_type =[
        ('', 'Job Type'),
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Remotly','Remotly')
    ]


    title = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100 , choices=job_type )
    description = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now_add=True )
    vacancy = models.IntegerField(validators=[validate_positive])
    salary = models.DecimalField(max_digits=8 ,decimal_places=2)
    experience = models.IntegerField(validators=[validate_positive])
    job_img = models.ImageField(upload_to = image_upload)
    categoty = models.ForeignKey(Categoty,on_delete=models.CASCADE,default ='')
    qualification = models.TextField(max_length=1000)

    slug = models.SlugField(blank= True , null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title ,allow_unicode= True)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    


class Apply_job(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    link = models.URLField()
    cv = models.FileField(upload_to= 'apply' )
    coverletter = models.TextField(max_length = 1000)
    job = models.ForeignKey(Job , on_delete= models.CASCADE)  


    def __str__(self):
        return self.name
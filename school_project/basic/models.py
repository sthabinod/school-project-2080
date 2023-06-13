from django.db import models
from school_project.users.models import User

class MoreAbout(models.Model):
    paragraph = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.paragraph


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.phone_number

class Information(models.Model):
    school_name = models.CharField(max_length=100)
    school_logo = models.ImageField(null=True,blank=True)
    sayings= models.CharField(max_length=100)
    sayings_description = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=200)
    about_school = models.TextField()
    more_about = models.ForeignKey(MoreAbout,on_delete=models.CASCADE)
    phone_number = models.ManyToManyField(PhoneNumber)
    our_experience = models.IntegerField()
    about_image = models.ImageField(null=True,blank=True)
    facebook_url = models.URLField(blank=True,null=True)
    instagram_url = models.URLField(blank=True,null=True)
    tiktok_url = models.URLField(blank=True,null=True)
    youtube_url = models.URLField(blank=True,null=True)
    info_video = models.URLField(blank=True,null=True)
    map = models.TextField(null=True,blank=True)
    
    
    class Meta:
        verbose_name = "School Info"
        verbose_name_plural = "School Info"
    
    def __str__(self):
        return self.school_name
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
        
class Team(models.Model):
    name = models.CharField(max_length=100)
    position =  models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return self.name
    
SUBJECT_TYPE =(
    ('half','half'),
    ('full','full')
)
    
class SubjectWeTeach(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    class_duration = models.CharField(max_length=100)
    subject_type = models.CharField(choices=SUBJECT_TYPE,max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name = "Subject We Teach"
        verbose_name_plural = "Subject We Teach"   
        
            
    def __str__(self) -> str:
        return self.name
    



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    position =  models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    feedback = models.TextField()
    
    def __str__(self) -> str:
        return self.name
      
 
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"   
        
class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True)
    venue = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"   
        
class GalleryCategory(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title   
        
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    comments = models.TextField()
    
    def __str__(self) -> str:
        return self.email
from django.shortcuts import render
from django.views import View
from school_project.basic.models import Information,SubjectWeTeach, Feedback,News,Gallery,Team,Events, Contact,GalleryCategory,BOD,AboutSchool, DirectorMessage, PrincipalMessage
from django.contrib import messages
from django.core.mail import send_mail
from config.settings.base import EMAIL_HOST_USER

class HomePage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        subjects = SubjectWeTeach.objects.all()[:4]
        feedbacks = Feedback.objects.all()
        latest_news = News.objects.all()[:4]
        gallery = Gallery.objects.all()[:4]
        bod = BOD.objects.all()
        principal_message = PrincipalMessage.objects.all()[:2]
        director_message = DirectorMessage.objects.all()[:2]
        
        data = {
            'info':info,
            'subjects':subjects,
            'feedbacks':feedbacks,
            'latest_news':latest_news,
            'gallery':gallery,
            'bod':bod,
            'director_message':director_message,
            'principal_message':principal_message
            }
        return render(request, 'pages/home.html',data)
    
class AboutPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        subjects = SubjectWeTeach.objects.all()[:4]
        feedbacks = Feedback.objects.all()
        latest_news = News.objects.all()[:4]
        gallery = Gallery.objects.all()[:4]
        teams = Team.objects.all()
        bod = BOD.objects.all()
        about_school = AboutSchool.objects.all()[:2]
     
        
  
        data = {
            'info':info,
            'subjects':subjects,
            'feedbacks':feedbacks,
            'latest_news':latest_news,
            'gallery':gallery,
            'teams':teams,
            'bod':bod,
            'about_school':about_school
            }
        return render(request, 'pages/about.html',data)
    
    
class SubjectPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        subjects = SubjectWeTeach.objects.all()
        gallery = Gallery.objects.all()[:4]
        data = {
            'info':info,
            'subjects':subjects,
            'gallery':gallery,
            }
        return render(request, 'pages/subject.html',data)
    
class EventPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        events = Events.objects.all()
        gallery = Gallery.objects.all()[:4]
        data = {
            'info':info,
            'events':events,
            'gallery':gallery,
            }
        return render(request, 'pages/events.html',data)
    
class NewsPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        news = News.objects.all()
        gallery = Gallery.objects.all()[:4]
        recent_news = News.objects.all()[:3]
        data = {
            'info':info,
            'news':news,
            'gallery':gallery,
            'recent_news':recent_news
            }
        return render(request, 'pages/news.html',data)
    
class ContactPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        news = News.objects.all()
        gallery = Gallery.objects.all()[:4]
        recent_news = News.objects.all()[:3]
        data = {
            'info':info,
            'news':news,
            'gallery':gallery,
            'recent_news':recent_news
            }
        return render(request, 'pages/contact.html',data)
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        send_mail(subject, message, EMAIL_HOST_USER, [email],fail_silently=False)
        contact = Contact.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone,comments=message,subject=subject)
        messages.success(request,"Thank you for reaching us, we will contact you soon!")
        
        return render(request, 'pages/contact.html')
    
class GalleryPage(View):
    def get(self,request, *args, **kwargs):
        info = Information.objects.get(id=1)
        galleries = Gallery.objects.all()
        gallery = Gallery.objects.all()[:4]
        gallery_categories = GalleryCategory.objects.all()
        data = {
            'info':info,
            'galleries':galleries,
            'gallery':gallery,
            'gallery_categories':gallery_categories
            }
        return render(request, 'pages/gallery.html',data)

class GalleryDetail(View):
    def get(self,request, id, *args, **kwargs):
        info = Information.objects.get(id=1)
        one_gallery = Gallery.objects.get(id=id)
        gallery = Gallery.objects.all()[:4]
        data = {
            'info':info,
            'one_gallery':one_gallery,
            'gallery':gallery,
            }
        return render(request, 'pages/gallery_detail.html',data)
class CatgoryWiseGallery(View):
    def get(self,request, id, *args, **kwargs):
        info = Information.objects.get(id=1)
        galleries = Gallery.objects.filter(category=id)
        print(galleries)
        gallery = Gallery.objects.all()[:4]
        gallery_categories = GalleryCategory.objects.all()
        data = {
            'info':info,
            'galleries':galleries,
            'gallery':gallery,
             'gallery_categories':gallery_categories
            }
        return render(request, 'pages/gallery.html',data)
    
class NewsSingle(View):
    def get(self,request, id, *args, **kwargs):
        info = Information.objects.get(id=1)
        news_single = News.objects.get(id=id)
        print(news_single)
        gallery = Gallery.objects.all()[:4]
        data = {
            'info':info,
            'single_news':news_single,
            'gallery':gallery,
            }
        return render(request, 'pages/single_news.html',data)
    

class PrincipalMessageView(View):
    def get(self, request):
        info = Information.objects.get(id=1)
        gallery = Gallery.objects.all()[:4]
        principal_message = PrincipalMessage.objects.all()
        
        data = {
            'info':info,
            'gallery':gallery,
            'principal_message':principal_message
            }
        return render(request, 'pages/principal_message.html',data)
    
class DirectorMessageView(View):
    def get(self, request):
        info = Information.objects.get(id=1)
        gallery = Gallery.objects.all()[:4]
        director_message = DirectorMessage.objects.all()
        
        data = {
            'info':info,
            'gallery':gallery,
            'director_message':director_message
            }
        return render(request, 'pages/director_message.html',data)
    

class MoreAbout(View):
    def get(self, request):
        info = Information.objects.get(id=1)
        gallery = Gallery.objects.all()[:4]
        about_school = AboutSchool.objects.all()
        data = {
            'info':info,
            'gallery':gallery,
            'about_school':about_school
            }
        return render(request, 'pages/about_more.html',data)
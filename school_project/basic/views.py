from django.shortcuts import render
from django.views import View
from school_project.basic.models import Information,SubjectWeTeach, Feedback,News,Gallery,Team,Events, Contact,GalleryCategory
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
        data = {
            'info':info,
            'subjects':subjects,
            'feedbacks':feedbacks,
            'latest_news':latest_news,
            'gallery':gallery
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
        data = {
            'info':info,
            'subjects':subjects,
            'feedbacks':feedbacks,
            'latest_news':latest_news,
            'gallery':gallery,
            'teams':teams
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
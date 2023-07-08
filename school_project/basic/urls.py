from django.urls import path

from school_project.basic.views import (
   HomePage,
   AboutPage,
   SubjectPage,
   EventPage,
   NewsPage,
   ContactPage,
   GalleryPage,
   GalleryDetail,
   CatgoryWiseGallery,
   NewsSingle,
   PrincipalMessageView,
   MoreAbout,
   DirectorMessageView
)

app_name = "basic"
urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path("about", AboutPage.as_view(), name="about_page"),
    path("subject", SubjectPage.as_view(), name="subject_page"),
    path("event", EventPage.as_view(), name="event_page"),
    path("news", NewsPage.as_view(), name="news_page"),
    path("contact", ContactPage.as_view(), name="contact_page"),
    path("gallery", GalleryPage.as_view(), name="gallery_page"),
    path("gallery/<int:id>", GalleryDetail.as_view(), name="gallery_detail"),
    path("gallery-category/<int:id>", CatgoryWiseGallery.as_view(), name="category_gallery"),
    path("news/<int:id>", NewsSingle.as_view(), name="news_single"),
    path("principal/", PrincipalMessageView.as_view(), name="principal_message"),
    path("director/", DirectorMessageView.as_view(), name="director_message"),
    path("more-about/", MoreAbout.as_view(), name="more-about"),
]

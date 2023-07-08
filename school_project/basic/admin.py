from django.contrib import admin
from school_project.basic.models import Information,Team,Feedback,News,Events,Gallery,GalleryCategory,Contact,SubjectWeTeach,BOD, PrincipalMessage, DirectorMessage, AboutSchool


admin.site.site_header = 'School Project'
admin.site.index_title = 'School project'

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass



@admin.register(GalleryCategory)
class GalleryCatAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(SubjectWeTeach)
class SubAdmin(admin.ModelAdmin):
    pass

@admin.register(BOD)
class BODAdmin(admin.ModelAdmin):
    pass

@admin.register(PrincipalMessage)
class PrincipalAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectorMessage)
class DirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutSchool)
class AboutAdmin(admin.ModelAdmin):
    pass
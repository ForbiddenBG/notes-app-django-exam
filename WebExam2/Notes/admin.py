from django.contrib import admin

from WebExam2.Notes.models import Profile, Note


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', "last_name"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["title"]

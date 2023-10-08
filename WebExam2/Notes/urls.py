from django.urls import path

from WebExam2.Notes.views import home_page, add_note, edit_note, delete_note, details_note, profile_page, delete_profile

urlpatterns = (
    path('', home_page, name='index'),
    path('add/', add_note, name='add'),
    path('edit/<int:id>/', edit_note, name='edit'),
    path('delete/<int:id>/', delete_note, name='delete'),
    path('details/<int:id>/', details_note, name='details'),
    path('profile/', profile_page, name='profile'),
    path('profile/delete', delete_profile, name='delete-profile'),
)
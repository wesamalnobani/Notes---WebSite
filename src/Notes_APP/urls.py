from django.urls import path
from .views import notes,note_details,note_add,note_edit

urlpatterns = [
    path('',notes,name='notes'),
    path('note_details/<str:slug>/',note_details,name='note_details'),
    path('note_add/',note_add,name='note_add'),
    path('note_edit/<str:slug>/',note_edit,name='note_edit'),
]

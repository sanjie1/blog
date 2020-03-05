from . import views
from django.urls import path
app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
from.import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('register/',views.register,name='register'),
#     path('details/',views.details,name='details'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('feedback/',views.feedback,name='feedback')
]

from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('api/$',views.Student_data.as_view()),
    re_path(r'^api_update/(?P<id>\d+)/$',views.Teacher_update_id.as_view()),
]

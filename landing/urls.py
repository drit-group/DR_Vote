from .views import DetailVideo,ListVideo
from django.urls import path
app_name = "landing"
urlpatterns = [
    path('', ListVideo.as_view(),name="home"),
    path("page/<int:page>", ListVideo.as_view(), name="home"),
    path('art/<slug:slug>', DetailVideo.as_view() ,name="single"),

]
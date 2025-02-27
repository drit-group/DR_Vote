from .views import DashBoard, addFilm, editFilm, addCategory, editCategory, allCategory, editProfile, listUsers
from django.urls import path
app_name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
    path('create', addFilm.as_view(),name="addFilm"),
    path("edit/<int:pk>", editFilm.as_view(), name="editFilm"),
    path("addCat/", addCategory.as_view(), name="addCategory"),
    path("editCat/", editCategory.as_view(), name="editCategory"),
    path("allCat/", allCategory.as_view(), name="allCategory"),
    path("profile/edit/<int:pk>", editProfile.as_view(), name="editprofile"),
    path("profile/list/", listUsers.as_view(), name="editprofile")
]

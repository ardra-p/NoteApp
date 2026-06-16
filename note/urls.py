from note import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_view import NoteViewset, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('note',NoteViewset, basename='note' )


urlpatterns = [
    path('home/', views.index,name="home"),
    path('create/', views.create_note,name="create"),
    path('notelist/', views.list_note,name="notelist"),
    path('notes/<pk>', views.single_note_list,name="notes"),
    path('edit/<pk>', views.edit_note, name="edit_note"),
    path('delete/<pk>', views.delete_note, name="delete_note"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('',views.home_page,name="home_page"),

    #API
    path('api/',include(router.urls)),
    # add urls of login register api tomorrow 16/06/2026
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),


]

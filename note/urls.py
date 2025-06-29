from note import views
from django.urls import path

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
]

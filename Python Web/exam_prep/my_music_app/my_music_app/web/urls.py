'''
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page

'''
from django.urls import include, path

from my_music_app.web.views import index, album_details, album_edit, album_add, album_delete, profile_delete, \
    profile_details, profile_add

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('details/<int:pk>/', album_details, name='album details'),
        path('add/', album_add, name='album add'),
        path('edit/<int:pk>/', album_edit, name= "album edit"),
        path('delete/<int:pk>/', album_delete, name='album delete')
    ])),
    path('profile/', include([
        path('add/', profile_add, name='profile add'),
        path('details/', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete')
    ]))
)
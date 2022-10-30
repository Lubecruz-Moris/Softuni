'''

•	http://localhost:8000/ - home page
•	http://localhost:8000/add/ - add book page
•	http://localhost:8000/edit/:id - edit book page
•	http://localhost:8000/details/:id - book details page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page

'''
from django.urls import path, include

from online_library.web.views import index, profile_details, profile_edit, profile_delete, profile_add, book_add, \
    book_details, book_edit, book_delete

urlpatterns = (
    path('', include([
        path('', index, name='index'),
        path('add/', book_add, name='book add'),
        path('details/<int:pk>/', book_details, name='book details'),
        path('edit/<int:pk>/', book_edit, name='book edit'),
        path('delete/<int:pk>/', book_delete, name='book delete')
    ])),
    path('profile/', include([
        path('', profile_details, name='profile details'),
        path('add/', profile_add, name='profile add'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),

        ])))
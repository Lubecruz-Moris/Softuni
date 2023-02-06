from django.urls import path, include

from exam.car_collection_app.views import index, catalogue, profile_details, profile_create, profile_edit, \
    profile_delete, car_details, car_create, car_edit, car_delete

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('create/', profile_create, name='profile create'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('details/<int:pk>/', car_details, name='car details'),
        path('create/', car_create, name='car create'),
        path('edit/<int:pk>/', car_edit, name='car edit'),
        path('delete/<int:pk>/', car_delete, name='car delete'),
    ]))
)

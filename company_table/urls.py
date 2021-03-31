from django.urls import path

from .import views


urlpatterns=[
    path('post-company-detail',views.company_detail),
    path('get-company-data',views.get_company_detail),
    path('get-unique_user',views.get_unique_user),
    path('get_active_users',views.get_active_users),
]

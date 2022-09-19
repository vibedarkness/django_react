from django.urls import path

from .views import LivreMixins



urlpatterns = [
    path('index/', LivreMixins.as_view(),),
    path('<int:pk>/update', LivreMixins.as_view(),),
    path('<int:pk>/delete', LivreMixins.as_view(),),
    path('create/', LivreMixins.as_view(),),

]

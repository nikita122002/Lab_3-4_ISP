from django.urls import path, include
from . import views
from .views import register, user_login, user_logout, feedback, tourtype, tourplace, get_category, view_tourplace

urlpatterns = [
    path('products/', include('products.urls')),
    path('', views.home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('feedback/', feedback, name='feedback'),
    path('tourtype/', tourtype, name='tourtype'),
    path('tourplace/', tourplace, name='tourplace'),
    path('category/<int:category_id>/', get_category),
    path('main/<int:category_id>/', view_tourplace, name='view_tourplace'),
    path('shop/', views.shop, name='shop')

]

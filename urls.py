from django.urls import path
from . import views
 
#this is a comment
urlpatterns = [
   path('', views.index, name='index'),
   path('getTypes/', views.getTypes, name='types'),
   path('getProducts/', views.getProducts, name='products'),
   path('productdetails/<int:id>', views.productdetails, name='productdetails')
   path('newProduct/', views.newProduct, name='newproduct'),
   path('newReview/', views.newReview, name='newreview'),
]
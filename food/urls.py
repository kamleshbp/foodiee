from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    # index page
    path('', views.index, name='index'),
    # path('item/', views.item, name='item'),
    # details page
    path('<int:item_id>/', views.detail, name='detail'),
    # add items
    path('add/', views.create_item, name='create_item'),
    # update item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # delete item
    path('delete/<int:item_id>/', views.delete_item, name='delete_item')
]

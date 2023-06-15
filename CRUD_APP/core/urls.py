from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
  path(''                                 , views.view_CRUD_APP, name='show_CRUD'),
  path('<int:pk>'                                 , views.view_CRUD_APP, name='show_CRUD'),
  path('Edit/<str:table_or_data>/<int:pk>/', views.edit_table_or_data, name='edit'),
  path('Edit/<str:table_or_data>/', views.edit_table_or_data, name='edit'),
  path('delete/<str:table_or_data>/<int:pk>/', views.delete, name='delete'),
  path('Add/value/<int:pk>/', views.add_value, name='add_value'),
  path('Add/value/', views.add_value, name='add_value'),
  path('Add/table/', views.add_table, name='add_table'),
  # path("table/<int:pk>", views.view_table, name='show_table'),
]

from django.urls import path
from . import views
from main_app.views import ReservationsList, Gear_itemList, Gear_itemDetail, ReservationIndex
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('rentals/', Gear_itemList.as_view()),
    path('rentals/<int:gear_item_id>', Gear_itemDetail.as_view()),
    path('about/', views.about, name='about'),
    # path('rentals/', views.rentals_index, name='index'),
    # path('rentals/<int:gear_item_id>', views.gear_item_detail, name='detail'),
    path('rentals/create', views.Gear_itemCreate.as_view(), name='gear_item_create'),
    path('rentals/<int:pk>/update', views.Gear_itemUpdate.as_view(), name='gear_item_update'),
    path('rentals/<int:pk>/delete', views.Gear_itemDelete.as_view(), name='gear_item_delete'),
    path('rentals/<int:gear_item_id>/add_photo/', views.add_photo, name='add_photo'),
    path('reservations/', ReservationIndex.as_view()),
    path('reservations/new', views.ReservationCreate.as_view(), name='reservation_create'),
    # path('reservations/<int:reservation_id>', views.reservation_detail, name='reservation_detail'),
    path('reservations/<int:reservation_id>', views.Reservation_itemDetail.as_view(), name='reservation_detail'),
    path('reservations/<int:pk>/update', views.ReservationUpdate.as_view(), name='reservation_update'),
    path('reservations/<int:reservation_id>/add_gear/<int:gear_item_id>', views.add_gear, name='add_gear'),
    path('reservations/<int:reservation_id>/remove_gear/<int:gear_item_id>', views.remove_gear, name='remove_gear'),
    path('reservations/<int:reservation_id>/add_quantity/', views.add_quantity, name='add_quantity'),
    path('reservations/<int:reservation_id>/remove_quantity/', views.remove_quantity, name='remove_quantity'),
    path('reservations/<int:pk>/delete', views.ReservationDelete.as_view(), name='reservation_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', views.getRoutes)

]
from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),  
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), 

    path('register/', RegisterView.as_view(), name='register'),

    path('propiedad/', views.PropiedadListCreate.as_view(), name='propiedad-list'), 
    path('propiedad/<int:pk>/', views.PropiedadDetail.as_view(), name='propiedad-detail'),
   
    path('reserva/', views.ReservaListCreate.as_view(), name='reserva-list'), 
    path('reserva/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),
    
    path('valoracion/', views.ValoracionListCreate.as_view(), name='valoracion-list'), 
    path('valoracion/<int:pk>/', views.ValoracionDetail.as_view(), name='valoracion-detail'),
   
    path('metodopago/', views.MetodoPagoListCreate.as_view(), name='metodopago-list'), 
    path('metodopago/<int:pk>/', views.MetodoPagoDetail.as_view(), name='metodopago-detail'),
    
    path('notificacion/', views.NotificacionListCreate.as_view(), name='notificacion-list'), 
    path('notificacion/<int:pk>/', views.NotificacionDetail.as_view(), name='notificacion-detail'),
   
    path('faq/', views.FAQListCreate.as_view(), name='faq-list'), 
    path('faq/<int:pk>/', views.FAQDetail.as_view(), name='faq-detail'),
   
    path('newsletter/', views.NewsletterListCreate.as_view(), name='newsletter-list'), 
    path('newsletter/<int:pk>/', views.NewsletterDetail.as_view(), name='newsletter-detail'),
   
    path('oferta/', views.OfertaListCreate.as_view(), name='oferta-list'), 
    path('oferta/<int:pk>/', views.OfertaDetail.as_view(), name='oferta-detail'),
   
    path('actividad/', views.ActividadListCreate.as_view(), name='actividad-list'), 
    path('actividad/<int:pk>/', views.ActividadDetail.as_view(), name='actividad-detail'),
   
    path('verificacionidentidad/', views.VerificacionIdentidadListCreate.as_view(), name='verificacionidentidad-list'), 
    path('verificacionidentidad/<int:pk>/', views.VerificacionIdentidadDetail.as_view(), name='verificacionidentidad-detail'),
   
    path('historialactividad/', views.HistorialActividadListCreate.as_view(), name='historialactividad-list'), 
    path('historialactividad/<int:pk>/', views.HistorialActividadDetail.as_view(), name='historialactividad-detail'),
   
    path('feedback/', views.FeedbackListCreate.as_view(), name='feedback-list'), 
    path('feedback/<int:pk>/', views.FeedbackDetail.as_view(), name='feedback-detail'),
   
    path('servicio/', views.ServicioListCreate.as_view(), name='servicio-list'), 
    path('servicio/<int:pk>/', views.ServicioDetail.as_view(), name='servicio-detail'),
    
    path('propiedadservicio/', views.PropiedadServicioListCreate.as_view(), name='propiedadservicio-list'), 
    path('propiedadservicio/<int:pk>/', views.PropiedadServicioDetail.as_view(), name='propiedadservicio-detail'),
    
    path('ubicacion/', views.UbicacionListCreate.as_view(), name='ubicacion-list'), 
    path('ubicacion/<int:pk>/', views.UbicacionDetail.as_view(), name='ubicacion-detail'),
    
    path('contrato/', views.ContratoListCreate.as_view(), name='contrato-list'), 
    path('contrato/<int:pk>/', views.ContratoDetail.as_view(), name='contrato-detail'),
    
    path('favorito/', views.FavoritoListCreate.as_view(), name='favorito-list'), 
    path('favorito/<int:pk>/', views.FavoritoDetail.as_view(), name='favorito-detail'),
    
    path('mantenimiento/', views.MantenimientoListCreate.as_view(), name='mantenimiento-list'), 
    path('mantenimiento/<int:pk>/', views.MantenimientoDetail.as_view(), name='mantenimiento-detail'),

    path('reseña/', views.ReseñaListCreate.as_view(), name='reseña-list'), 
    path('reseña/<int:pk>/', views.ReseñaDetail.as_view(), name='reseña-detail'),
    
    path('imagenpropiedad/', views.ImagenPropiedadListCreate.as_view(), name='imagenpropiedad-list'), 
    path('imagenpropiedad/<int:pk>/', views.ImagenPropiedadDetail.as_view(), name='imagenpropiedad-detail'),
    
    path('detallepropiedad/', views.DetallePropiedadListCreate.as_view(), name='detallepropiedad-list'), 
    path('detallepropiedad/<int:pk>/', views.DetallePropiedadDetail.as_view(), name='detallepropiedad-detail'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
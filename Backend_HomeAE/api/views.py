from rest_framework import generics
from rest_framework.views import APIView
from .models import (
    Propiedad, Reserva, Valoracion, MetodoPago, Notificacion, 
    FAQ, Newsletter, Oferta, Actividad, VerificacionIdentidad,
    HistorialActividad, Feedback, Servicio, PropiedadServicio,
    Ubicacion, Contrato, Favorito, Mantenimiento, Reseña)
from .serializers import (
    UserRegisterSerializer,PropiedadSerializer, ReservaSerializer, 
    ValoracionSerializer, MetodoPagoSerializer, NotificacionSerializer, 
    FAQSerializer, NewsletterSerializer, OfertaSerializer, 
    ActividadSerializer, VerificacionIdentidadSerializer, 
    HistorialActividadSerializer, FeedbackSerializer, ServicioSerializer, 
    PropiedadServicioSerializer, UbicacionSerializer, ContratoSerializer, 
    FavoritoSerializer, MantenimientoSerializer, ReseñaSerializer)
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsAdministrador(BasePermission):
    # Permiso para verificar si el usuario pertenece al grupo "Administrador"
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Administrador").exists()
    
class IsCliente(BasePermission):
    # Permiso para verificar si el usuario pertenece al grupo "Cliente"
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Cliente").exists()
    
class IsPropietario(BasePermission):
    # Permiso para verificar si el usuario pertenece al grupo "Propietario"
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Propietario").exists()  

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    # Permisos para acceder a la vista: autenticado y ser Admin, Cliente o Propietario
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente | IsPropietario]
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    # Permisos para acceder a la vista: autenticado y ser Admin
    permission_classes = [IsAuthenticated, IsAdministrador] 
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Usuario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


class PropiedadListCreate(generics.ListCreateAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer

class PropiedadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
    
class ValoracionListCreate(generics.ListCreateAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer

class ValoracionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    
    
class MetodoPagoListCreate(generics.ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    
    
class NotificacionListCreate(generics.ListCreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class NotificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    
    
class FAQListCreate(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    
class NewsletterListCreate(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewsletterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    
    
class OfertaListCreate(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    
    
class ActividadListCreate(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    
    
class VerificacionIdentidadListCreate(generics.ListCreateAPIView):
    queryset = VerificacionIdentidad.objects.all()
    serializer_class = VerificacionIdentidadSerializer

class VerificacionIdentidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VerificacionIdentidad.objects.all()
    serializer_class = VerificacionIdentidadSerializer
    
    
class HistorialActividadListCreate(generics.ListCreateAPIView):
    queryset = HistorialActividad.objects.all()
    serializer_class = HistorialActividadSerializer

class HistorialActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialActividad.objects.all()
    serializer_class = HistorialActividadSerializer
    
    
class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    
class ServicioListCreate(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    
    
class PropiedadServicioListCreate(generics.ListCreateAPIView):
    queryset = PropiedadServicio.objects.all()
    serializer_class = PropiedadServicioSerializer

class PropiedadServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropiedadServicio.objects.all()
    serializer_class = PropiedadServicioSerializer
    
    
class UbicacionListCreate(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class UbicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    
    
class ContratoListCreate(generics.ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
    
class FavoritoListCreate(generics.ListCreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class FavoritoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class MantenimientoListCreate(generics.ListCreateAPIView):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [IsAuthenticated]  # Solo los usuarios autenticados pueden acceder

class MantenimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [IsAuthenticated]  # Solo los usuarios autenticados pueden acceder

    
    
class ReseñaListCreate(generics.ListCreateAPIView):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer

class ReseñaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
from rest_framework import serializers
from .models import (
    Propiedad, Reserva, Valoracion, MetodoPago, Notificacion, FAQ,
    Newsletter, Oferta, Actividad, VerificacionIdentidad, HistorialActividad,
    Feedback, Servicio, PropiedadServicio, Ubicacion, Contrato, Favorito,
    Mantenimiento, Reseña
)

from django.contrib.auth.models import User, Group

class UserRegisterSerializer(serializers.ModelSerializer):
    # Campo 'role' se define como solo escritura
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Campos que se incluirán en la serialización
        fields = ('Usuario', 'Nombre', 'Apellidos', 'Correo', 'Contraseña', 'rol')
        
    def validate_password(self, value):
        # Validación para asegurar que la contraseña tenga al menos 6 caracteres
        if len(value) < 6:
            raise serializers.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return value

    def create(self, validated_data):
        # Extraer el rol del usuario del conjunto de datos validados
        rol = validated_data.pop('rol')
        # Crear una instancia de User con los datos validados
        user = User(**validated_data)
        # Establecer la contraseña encriptada
        user.set_password(validated_data['Contraseña'])
        # Guardar el usuario en la base de datos
        user.save()

        # Asignar el rol al grupo correspondiente si existe
        if rol: 
            try:
                group = Group.objects.get(name=rol)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError(f"El rol '{rol}' no existe")

        return user
    
    def update(self, instance, validated_data):
        # Actualizar los campos del usuario con los datos proporcionados
        instance.username = validated_data.get('Usuario', instance.username)
        instance.first_name = validated_data.get('Nombre', instance.first_name)
        instance.last_name = validated_data.get('Apellidos', instance.last_name)
        instance.email = validated_data.get('Correo', instance.email)

        # Si se proporciona una nueva contraseña, establecerla y guardar el usuario
        if 'Contraseña' in validated_data:
            instance.set_password(validated_data['Contraseña'])
            instance.save()  
    
        return instance 
    

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user    

# Serializer de Usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Usuario', 'Correo']


# Serializer de Propiedad
class PropiedadSerializer(serializers.ModelSerializer):
    propietario = UserSerializer(read_only=True)

    class Meta:
        model = Propiedad
        fields = '__all__'


# Serializer de Reserva
class ReservaSerializer(serializers.ModelSerializer):
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())
    inquilino = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        if data['fecha_inicio'] >= data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        return data


# Serializer de Valoración
class ValoracionSerializer(serializers.ModelSerializer):
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Valoracion
        fields = '__all__'

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5.")
        return value


# Serializer de Método de Pago
class MetodoPagoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = MetodoPago
        fields = '__all__'

    def validate_estado(self, value):
        if value not in ['activo', 'inactivo']:
            raise serializers.ValidationError("Estado inválido.")
        return value


# Serializer de Notificación
class NotificacionSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Notificacion
        fields = '__all__'


# Serializer de FAQ
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


# Serializer de Newsletter
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


# Serializer de Oferta
class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'


# Serializer de Actividad
class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

    def validate_calificacion(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 0 y 5.")
        return value


# Serializer de Verificación de Identidad
class VerificacionIdentidadSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = VerificacionIdentidad
        fields = '__all__'


# Serializer de Historial de Actividad
class HistorialActividadSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = HistorialActividad
        fields = '__all__'


# Serializer de Feedback
class FeedbackSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5.")
        return value


# Serializer de Servicio
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


# Serializer de PropiedadServicio
class PropiedadServicioSerializer(serializers.ModelSerializer):
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())
    servicio = serializers.PrimaryKeyRelatedField(queryset=Servicio.objects.all())

    class Meta:
        model = PropiedadServicio
        fields = '__all__'


# Serializer de Ubicación
class UbicacionSerializer(serializers.ModelSerializer):
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())

    class Meta:
        model = Ubicacion
        fields = '__all__'


# Serializer de Contrato
class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

    def validate(self, data):
        if data['fecha_inicio'] >= data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        return data


# Serializer de Favorito
class FavoritoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())

    class Meta:
        model = Favorito
        fields = '__all__'


# Serializer de Mantenimiento
class MantenimientoSerializer(serializers.ModelSerializer):
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())

    class Meta:
        model = Mantenimiento
        fields = '__all__'

    def validate_estado(self, value):
        if value not in ['Pendiente', 'En progreso', 'Completado']:
            raise serializers.ValidationError("Estado de mantenimiento inválido.")
        return value


# Serializer de Reseña
class ReseñaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    propiedad = serializers.PrimaryKeyRelatedField(queryset=Propiedad.objects.all())

    class Meta:
        model = Reseña
        fields = '__all__'

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5.")
        return value
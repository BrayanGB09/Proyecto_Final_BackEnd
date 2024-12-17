from django.db import models
from django.contrib.auth.models import User


# Modelo de Propiedades
class Propiedad(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    imagen = models.URLField(blank=True, null=True)
    propietario_id_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Propiedad {self.titulo} - {self.propietario_id_id}"
 
 
# Modelo de Reservas
class Reserva(models.Model):
    ESTADOS = [
        ('Confirmada', 'confirmada'),
        ('Pendiente', 'pendiente'),
        ('Cancelada', 'cancelada')
    ]

    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    huespedes = models.IntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_reserva = models.DateField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    
    def __str__(self):
        return f"Reserva de {self.cliente_id} en {self.propiedad_id}"


# Modelo de Valoraciones
class Valoracion(models.Model):
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(calificacion__gte=1, calificacion__lte=5), name="calificacion_range")
        ]

    def __str__(self):
        return f"Valoración de {self.usuario_id} para {self.propiedad_id}"


# Modelo de Métodos de Pago
class MetodoPago(models.Model):
    TIPOS = [
        ('Tarjeta de credito', 'tarjeta de crédito'),
        ('Paypal', 'paypal'),
        ('Transferencia bancaria', 'transferencia bancaria'),
    ]
    ESTADOS = [
        ('Activo', 'activo'),
        ('Inactivo', 'inactivo')
    ]

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25, choices=TIPOS)
    detalles = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')

    def __str__(self):
        return f"{self.tipo} de {self.usuario_id}"


# Modelo de Notificaciones
class Notificacion(models.Model):
    ESTADOS = [
        ('Leído', 'leído'),
        ('No leído', 'no leído')
    ]

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='no leído')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.usuario_id}"


# Modelo de Preguntas Frecuentes (FAQ)
class FAQ(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta


# Modelo de Inscripciones a Newsletter
class Newsletter(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Newsletter: {self.email}"


# Modelo de Ofertas Especiales
class Oferta(models.Model):
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.descripcion


# Modelo de Actividades y Experiencias
class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.CharField(max_length=50, blank=True, null=True)
    calificacion = models.FloatField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(calificacion__gte=0, calificacion__lte=5), name="calificacion_range_actividad")
        ]

    def __str__(self):
        return self.titulo


# Modelo de Verificación de Identidad
class VerificacionIdentidad(models.Model):
    TIPOS = [
        ('Documento de identidad', 'documento de identidad'),
        ('Comprobante de residencia', 'comprobante de residencia')
    ]
    ESTADOS = [
        ('Verificado', 'verificado'),
        ('En proceso', 'en proceso'),
        ('Rechazado', 'rechazado')
    ]

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_verificacion = models.CharField(max_length=30, choices=TIPOS)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_verificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_verificacion} de {self.usuario_id}"


# Modelo de Historial de Actividad del Usuario
class HistorialActividad(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    actividad = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Actividad de {self.usuario_id}"


# Modelo de Feedback
class Feedback(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    comentario = models.TextField()
    calificacion = models.IntegerField(
        choices=[
            (1, '⭐ 1 estrella'),
            (2, '⭐⭐ 2 estrellas'),
            (3, '⭐⭐⭐ 3 estrellas'),
            (4, '⭐⭐⭐⭐ 4 estrellas'),
            (5, '⭐⭐⭐⭐⭐ 5 estrellas'),
        ],
        help_text="Selecciona una calificación entre 1 (peor) y 5 (mejor)"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(calificacion__gte=1, calificacion__lte=5),
                name="calificacion_range_feedback"
            )
        ]

    def __str__(self):
        return f"Feedback de {self.usuario_id}"


# Modelo de Servicios
class Servicio(models.Model):
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Modelo de relación muchos a muchos entre Propiedad y Servicio
class PropiedadServicio(models.Model):
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    servicio_id = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('propiedad_id', 'servicio_id')


# Modelo de Ubicaciones
class Ubicacion(models.Model):
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}"


# Modelo de Contratos
class Contrato(models.Model):
    fecha_firma = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    documento = models.BinaryField()

    def __str__(self):
        return f"Contrato {self.id}"


# Modelo de Favoritos
class Favorito(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_agregado = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario_id', 'propiedad_id')


# Modelo de Mantenimiento
class Mantenimiento(models.Model):
    ESTADOS = [
        ('Pendiente', 'pendiente'),
        ('En progreso', 'en progreso'),
        ('Completado', 'completado')
    ]

    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_completado = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Mantenimiento {self.estado} - {self.propiedad_id}"


# Modelo de Reseñas
class Reseña(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    calificacion = models.IntegerField(
        choices=[
            (1, '⭐ 1 estrella'),
            (2, '⭐⭐ 2 estrellas'),
            (3, '⭐⭐⭐ 3 estrellas'),
            (4, '⭐⭐⭐⭐ 4 estrellas'),
            (5, '⭐⭐⭐⭐⭐ 5 estrellas'),
        ],
        help_text="Selecciona una calificación entre 1 (peor) y 5 (mejor)"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(calificacion__gte=1, calificacion__lte=5),
                name="calificacion_range_reseñas"
            )
        ]
        unique_together = ('usuario_id', 'propiedad_id')

    def __str__(self):
        return f"Reseña de {self.usuario_id} - {self.propiedad_id}"


# Modelo de Imagenes de Propiedades
class ImagenPropiedad(models.Model):
    propiedad_id = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='imagenes')
    url = models.URLField()
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Imagen de {self.propiedad_id.titulo}"   


class DetallePropiedad(models.Model):
    propiedad_id = models.OneToOneField(Propiedad, on_delete=models.CASCADE, related_name='detalle')
    ubicacion_id = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, related_name='detalle')
    imagenes_id = models.OneToOneField(ImagenPropiedad, on_delete=models.CASCADE, related_name='detalle')
    superficie = models.DecimalField(max_digits=10, decimal_places=2, help_text='Metros cuadrados')
    numero_habitaciones = models.IntegerField()
    numero_banos = models.IntegerField()
    amueblado = models.BooleanField(default=False)

    def __str__(self):
        return f"Detalle de {self.propiedad_id.titulo}"

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from django.contrib.messages import get_messages
from django.test import TestCase, Client
from Solicitudes.models import Solicitud
from datetime import datetime



class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)

        self.ciudadano_group = Group.objects.create(name='ciudadano')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_password_view(self):
        response = self.client.get(reverse('password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password.html')

    def test_inicio_view_authenticated(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')

    def test_registro_view_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html')

    def test_registro_view_post_existing_username(self):
        response = self.client.post(reverse('registro'), {
            'username': self.username,
            'password': 'newpassword',
            'email': 'test@example.com'
        })
        self.assertContains(response, 'Nombre de usuario ya existe.')

    def test_registro_view_post_existing_email(self):
        response = self.client.post(reverse('registro'), {
            'username': 'newuser',
            'password': 'newpassword',
            'email': self.user.email
        })
        self.assertContains(response, 'Correo electrónico ya existe.')

    def test_registro_view_post_valid(self):
        response = self.client.post(reverse('registro'), {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'test@example.com'
        })
        self.assertRedirects(response, reverse('index'))

    def test_index_view_post_valid_login(self):
        response = self.client.post(reverse('index'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('inicio'))

    def test_index_view_post_invalid_login(self):
        response = self.client.post(reverse('index'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertRedirects(response, reverse('index'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Nombre de usuario o contraseña incorrectos.')

    def test_logoutCustom_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))

    def test_perfil_view_authenticated_get(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')


class SolicitudesViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.group = Group.objects.create(name='ciudadano')
        self.user.groups.add(self.group)

        self.solicitud = Solicitud.objects.create(
            fecha_creacion=datetime.now(),
            resuelto=False,
            nombre='Ejemplo',
            tipo_problema='Problema',
            estado='Estado',
            municipio='Municipio',
            direccion='Dirección',
            codigo_postal=12345,
            telefono=1234567890,
            email='ejemplo@example.com',
            descripcion='Descripción',
        )

    def test_crear_solicitud_view(self):
        response = self.client.get(reverse('Solicitudes:crear_solicitud'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Solicitudes/crearSolicitud.html')

    def test_responder_solicitud_view(self):
        response = self.client.get(reverse('Solicitudes:responder_solicitud'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'Solicitudes/responderSolicitud.html')

    def test_solicitud_lista_view(self):
        response = self.client.get(reverse('Solicitudes:lista_solicitudes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Solicitudes/listaSolicitudes.html')

    def test_solicitud_creada_view(self):
        response = self.client.get(reverse('Solicitudes:solicitud_Creada'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Solicitudes/solicitudCreada.html')

    def test_detalles_solicitud_view(self):
        response = self.client.get(
            reverse('Solicitudes:detalles_solicitud', args=[self.solicitud.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'Solicitudes/detalles_solicitud.html')
        self.assertContains(response, self.solicitud.nombre)
        self.assertContains(response, self.solicitud.tipo_problema)
        self.assertContains(response, self.solicitud.estado)
        self.assertContains(response, self.solicitud.municipio)
        self.assertContains(response, self.solicitud.descripcion)

    def test_obtener_solicitud_lista(self):
        response = self.client.get(reverse('Solicitudes:lista_solicitudes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.solicitud, response.context['solicitudes'])
        self.assertTemplateUsed(response, 'Solicitudes/listaSolicitudes.html')



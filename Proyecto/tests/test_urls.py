from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Proyecto.views import index, registro, password, logoutCustom, inicio, perfil
from django.urls import reverse
from Solicitudes.views import crear_solicitud, responder_solicitud, lista_solicitud, solicitud_Creada, detalles_solicitud, editar_solicitud, generar_reporte_excel, SolicitudDetalleView, SolicitudListaView, respuesta_de_solicitud
from open311.views import lista_solicitudes, generar_reporte


class UrlTesting(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_registro_url(self):
        url = reverse('registro')
        self.assertEqual(resolve(url).func, registro)

    def test_password_url(self):
        url = reverse('password')
        self.assertEqual(resolve(url).func, password)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutCustom)

    def test_inicio_url(self):
        url = reverse('inicio')
        self.assertEqual(resolve(url).func, inicio)

    def test_perfil_url(self):
        url = reverse('perfil')
        self.assertEqual(resolve(url).func, perfil)


class SolicitudesUrlsTestCase(SimpleTestCase):

    def test_crear_solicitud_url(self):
        url = reverse('Solicitudes:crear_solicitud')
        self.assertEqual(resolve(url).func, crear_solicitud)

    def test_responder_solicitud_url(self):
        url = reverse('Solicitudes:responder_solicitud')
        self.assertEqual(resolve(url).func, responder_solicitud)

    def test_lista_solicitud_url(self):
        url = reverse('Solicitudes:lista_solicitudes')
        self.assertEqual(resolve(url).func, lista_solicitud)

    def test_solicitud_creada_url(self):
        url = reverse('Solicitudes:solicitud_Creada')
        self.assertEqual(resolve(url).func, solicitud_Creada)

    def test_detalles_solicitud_url(self):
        url = reverse('Solicitudes:detalles_solicitud', args=[24])
        self.assertEqual(resolve(url).func, detalles_solicitud)

    def test_editar_solicitud_url(self):
        url = reverse('Solicitudes:editar_solicitud', args=[24])
        self.assertEqual(resolve(url).func, editar_solicitud)

    def test_respuesta_de_solicitud_url(self):
        url = reverse('Solicitudes:respuesta_de_solicitud', args=[24])
        self.assertEqual(resolve(url).func, respuesta_de_solicitud)

    def test_solicitud_lista_url(self):
        url = reverse('Solicitudes:solicitud-lista')
        self.assertEqual(resolve(url).func.view_class, SolicitudListaView)

    def test_solicitud_detalle_url(self):
        url = reverse('Solicitudes:solicitud-detalle', args=[24])
        self.assertEqual(resolve(url).func.view_class, SolicitudDetalleView)

    def test_crear_reporte_url(self):
        url = reverse('Solicitudes:crear_reporte')
        self.assertEqual(resolve(url).func, generar_reporte_excel)


class Open311UrlsTestCase(SimpleTestCase):
    def test_lista_open311_url(self):
        url = reverse('open311:lista_open311')
        self.assertEqual(resolve(url).func, lista_solicitudes)

    def test_generar_reporte_url(self):
        url = reverse('open311:generar_reporte')
        self.assertEqual(resolve(url).func, generar_reporte)

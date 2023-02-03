from django.test import TestCase

from vhsApp.models import Cassette


class CassetteTests(TestCase):

    def test_creacion_de_cassette(self):
        
        cassette_nombre_valido = Cassette.objects.create(
            nombre="nombre corto", genero="dra"
            )

        self.assertEqual(Cassette.objects.all().count(), 1)
        self.assertIsNotNone(cassette_nombre_valido.id)

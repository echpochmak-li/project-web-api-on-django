from django.test import TestCase
from API.models import Serials

class SerialsModelTest(TestCase):

    def test_create_serial(self):
        """Проверка создания нового сериала"""
        serial = Serials.objects.create(
            name='Игра престолов',
            rating=18,
            genres='Фэнтези',
            info='Популярный фэнтезийный сериал.'
        )
        self.assertEqual(serial.name, 'Игра престолов')
        self.assertEqual(serial.rating, 18)
        self.assertEqual(serial.genres, 'Фэнтези')
        self.assertEqual(serial.info, 'Популярный фэнтезийный сериал.')

    def test_str_representation(self):
        """Проверка метода __str__ для представления сериала"""
        serial = Serials.objects.create(
            name='Игра престолов',
            rating=18,
            genres='Фэнтези',
            info='Популярный фэнтезийный сериал.'
        )
        self.assertEqual(str(serial), f'{serial.pk}Игра престолов')

from django.contrib.auth.models import User
import unittest

from .models import Category
from .models import TourizmType

class ModelTest(unittest.TestCase):

    def setUP(self):
        self.login_url = 'main/login'
        user = User.objects.create(username='testuser')
        user.set_password('1234nikia5')
        user.save()
        self.client.login(username='testuser', password='1234nikia5')

    def test_registration(self):
        form_data = {'username': "testuserr", 'email': "test2@gmail.com",
                     'password1': "nikitaqwe34", 'password2': "nikitaqwe34"}
        response = self.client.post("/main/register", data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        form_data = {'username': "testuserr", 'password1': "nikitaqwe34", 'password2': "nikitaqwe34"}
        response = self.client.post("/main/login", data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('main/logout')
        self.assertEqual(response.status_code, 200)

    def Model(self):
        self.sport = Category.title.create(verbose_name='Спорт')

    def Tourizm(self):
        self.title = TourizmType.title.create(verbose_name='Велосипедный')
        self.content = TourizmType.content.create(verbose_name='захватывающий')




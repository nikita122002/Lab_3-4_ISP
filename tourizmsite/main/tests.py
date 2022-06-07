from django.contrib.auth.models import User
from django.test import TestCase
from django.http import response
# Create your tests here.

class TEST1(TestCase):
    def setUP(self):
        self.login_url = 'main/login'
        user = User.objects.create(username='testuser')
        user.set_password('qwezxc123')
        user.save()
        self.client.login(username='testuser', password='qwezxc123')
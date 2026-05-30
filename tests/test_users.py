from django.test import TestCase

from django.contrib.auth.models import User


class UserTest(TestCase):

    def test_user_creation(self):

        user = User.objects.create_user(
            username='admin',
            password='admin123'
        )

        self.assertEqual(
            user.username,
            'admin'
        )

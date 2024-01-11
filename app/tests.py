from django.test import TestCase
from app.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        # Create a user
        user = CustomUser.objects.create_user(name='Narges salehi', email='narges@example.com', password='password')

        # Check that the user is created with the correct attributes
        self.assertEqual(user.name, 'Narges salehi')
        self.assertEqual(user.email, 'narges@example.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        # Check that the user's password is correctly set and encrypted
        self.assertTrue(user.check_password('password'))

    def test_create_superuser(self):
        # Create a superuser
        superuser = CustomUser.objects.create_superuser(name='Admin', email='admin@example.com', password='password')

        # Check that the superuser is created with the correct attributes
        self.assertEqual(superuser.name, 'Admin')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

        # Check that the superuser's password is correctly set and encrypted
        self.assertTrue(superuser.check_password('password'))
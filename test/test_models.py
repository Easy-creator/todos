from rest_framework.test import APITestCase
from users.models import User

class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = User.objects.create_user(
            'exe','exe@exe.com', 'eazydev'
        )
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'exe@exe.com')

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'exe','exe@exe.com', 'eazydev'
        )
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'exe@exe.com')

    def test_raise_value_error_username(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='exe@exe.com', password='eazydev')
        self.assertRaisesMessage(ValueError, 'username must be set')

    def test_raise_value_error_email(self):
        self.assertRaises(ValueError, User.objects.create_user, username='eazydev', email='', password='eazydev')
        self.assertRaisesMessage(ValueError, 'email must be set')

    def test_create_super_user_is_staff(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='eazydev', email='exe@exe.com', password='eazydev', is_staff=False)

    def test_create_super_user_is_superuser(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='eazydev', email='exe@exe.com', password='eazydev', is_superuser=False)
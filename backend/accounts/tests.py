from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class UserAccountTests(TestCase):
    
    def test_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testuser@user.com', 'username', 'first_name', 'password')
        self.assertEqual(super_user.email, 'testuser@user.com')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.username, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'username')
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@user.com', user_name='username', first_name='first_name', password='password', is_superuser=False
            )
            
    def test_user(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testuser@user.com', 'username', 'first_name', 'password')
        self.assertEqual(super_user.email, 'testuser@user.com')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.username, 'username')
        self.assertFalse(super_user.is_superuser)
        self.assertFalse(super_user.is_staff)
        self.assertFalse(super_user.is_active)
        self.assertEqual(str(super_user), 'username')
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@user.com', user_name='username', first_name='first_name', password='password', is_superuser=True
            ) 
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@user.com', user_name='username', first_name='first_name', password='password', is_active=True
            ) 
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@user.com', user_name='username', first_name='first_name', password='password', is_staff=True
            ) 

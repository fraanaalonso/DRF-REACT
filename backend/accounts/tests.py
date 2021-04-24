from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class UserAccountTests(TestCase):
    
    def test_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testuser1@super.com', 'username', 'first_name', 'password')
        self.assertEqual(super_user.email, 'testuser1@super.com')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.user_name, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'testuser1@super.com')
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser2@super.com', user_name='username1', first_name='first_name', password='password', is_superuser=False
            )
            
    def test_user(self):
        db = get_user_model()
        super_user = db.objects.create_user('testuser1@user.com', 'username1', 'first_name', 'password')
        self.assertEqual(super_user.email, 'testuser1@user.com')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.user_name, 'username1')
        self.assertFalse(super_user.is_superuser)
        self.assertFalse(super_user.is_staff)
        self.assertFalse(super_user.is_active)
        self.assertEqual(str(super_user), 'testuser1@user.com')
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', user_name='username2', first_name='first_name', password='password') 

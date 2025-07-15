# get_user_model gets user model from the referenced user model.
from django.contrib.auth import get_user_model

from django.test import TestCase


# Model tests
class ModelTest(TestCase):

    def test_create_user_with_email_success(self):
        email = 'test@example.com'
        password = 'testpass123'

        User = get_user_model()
        user = User.objects.create_user(
            email= email,
            password= password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_email= [
            ['abc@Example.com', 'abc@example.com'],
            ['test@EXAMPLE.COM', 'test@example.com']
        ]

        for email, expected_email in sample_email:
            User = get_user_model()
            user = User.objects.create_user(email=email, password= '1234455')

            self.assertEqual(user.email, expected_email)

    def test_email_required(self):

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email='', password='asd')



    def test_create_super_user(self):

        user = get_user_model().objects.create_superuser(email= 'test@email.com', password='1234')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        

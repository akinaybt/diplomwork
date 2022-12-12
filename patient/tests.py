from django.test import TestCase
from rest_framework.reverse import reverse

from .models import CustomUser, UserProfile, Appointment


class CustomUserTest(TestCase):
    def setUp(self) -> None:
        custom_user_data = {
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': '+996555555555',
            'is_patient': True,
        }
        user = CustomUser.objects.create(**custom_user_data)

    def test_user_detail(self):
        url = reverse('customuser-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        url = reverse('customuser-list')
        response = self.client.post(url, data={
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': '+99612345678'
        })

        self.assertEqual(response.status_code, 201)

    def test_user_delete(self):
        user = CustomUser.objects.get()
        url = reverse('customuser-detail', args=(user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_user_update(self):
        user = CustomUser.objects.first()

        url = reverse('customuser-detail', args=(user.pk,))
        response = self.client.put(url, data={
            'username': "test_username2",
            'first_name': "test_name2",
            'last_name': "test_last_name2",
            'phone_number': '+996777077233'
        }, content_type='application/json')

        self.assertEqual(response.status_code, 200)


class UserProfileTest(TestCase):
    def setUp(self) -> None:
        user_data = {
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': '+996555555555',
            'is_patient': True,
        }
        user = CustomUser.objects.create(**user_data)
        profile_data = {
            'user': user,
            'gender': "gender",
            'phone_number': "+996999333777"
        }
        profile_object = UserProfile.objects.create(**profile_data)

    def test_user_profile_detail(self):
        url = reverse('user-profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



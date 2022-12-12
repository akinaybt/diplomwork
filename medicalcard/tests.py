from django.test import TestCase
from rest_framework.reverse import reverse
from patient.models import UserProfile, CustomUser
from .models import Card


class CardTest(TestCase):
    def setUp(self) -> None:
        custom_user_data = {
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': "+996555555555",
            'is_patient': True
        }
        user = CustomUser.objects.create(**custom_user_data)
        profile_data = {
            'user': user,
            'gender': "male",
            'phone_number': "+996555555555"
        }
        profile = UserProfile.objects.create(**profile_data)
        card_data = {
            'patient': profile,
            'allergies': "Аллергий нет",
            'birth_date': "12.12.2012",
            'blood_group': "Первая положительная",
            'appointment': True
        }
        clinic = Card.objects.create(**card_data)

    def test_card_detail(self):
        url = reverse('card-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_card_delete(self):
        card = Card.objects.get()
        url = reverse('card-retrieve', args=(card.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_card_create(self):
        custom_user_data = {
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': "+996555555555",
            'is_patient': True
        }
        user = CustomUser.objects.create(**custom_user_data)
        profile_data = {
            'user': user,
            'gender': "male",
            'phone_number': "+996555555555"
        }
        profile = UserProfile.objects.create(**profile_data)
        url = reverse('card-list')
        response = self.client.post(url, data={
            'patient': profile,
            'allergies': "Аллергий нет",
            'birth_date': "12.12.2012",
            'blood_group': "Первая положительная",
            'appointment': True
        }
                                    )
        self.assertEqual(response.status_code, 201)

    def test_card_update(self):
        custom_user_data = {
            'username': "test_username",
            'first_name': "test_name",
            'last_name': "test_last_name",
            'phone_number': "+996555555555",
            'is_patient': True
        }
        user = CustomUser.objects.create(**custom_user_data)
        profile_data = {
            'user': user,
            'gender': "male",
            'phone_number': "+996555555555"
        }
        profile = UserProfile.objects.create(**profile_data)
        clinic = Card.objects.first()
        url = reverse('card-retrieve', args=(clinic.pk,))
        response = self.client.put(url, data={
            'patient': profile,
            'allergies': "Аллергия на цветы",
            'birth_date': "11.11.2011",
            'blood_group': "Первая отрицательная",
            'appointment': True
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)

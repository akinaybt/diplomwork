from django.test import TestCase
from rest_framework.reverse import reverse

from .models import Clinic, Department


class ClinicTest(TestCase):
    def setUp(self) -> None:
        clinic_data = {
            'title': "Больница №1",
            'foundation_date': '2022-02-22',
        }

        clinic = Clinic.objects.create(**clinic_data)

    def test_clinic_detail(self):
        url = reverse('clinic-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clinic_delete(self):
        clinic = Clinic.objects.get()
        url = reverse('clinic-detail', args=(clinic.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_clinic_create(self):
        url = reverse('clinic-list')
        response = self.client.post(url, data={
            'title': "Больница №2",
            'foundation_date': '2021-01-21',
        }
    )

        self.assertEqual(response.status_code, 201)

    def test_clinic_update(self):
        clinic = Clinic.objects.first()

        url = reverse('clinic-detail', args=(clinic.pk,))
        response = self.client.put(url, data={
            'title': "Больница №3",
            'foundation_date': '2020-12-12',
        }, content_type='application/json')

        self.assertEqual(response.status_code, 200)

#
# class DepartmentTest(TestCase):
#     def setUp(self) -> None:
#         department_data = {
#             'clinic': Clinic.title,
#             'title': 'Педиатрия',
#             'head_doctor': 'Name of doctor'
#         }
#
#         department = Department.objects.create(**department_data)
#
#     def test_department_detail(self):
#         url = reverse('department-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_department_delete(self):
#         clinic = Department.objects.get()
#         url = reverse('department-detail', args=(clinic.pk,))
#         response = self.client.delete(url)
#
#         self.assertEqual(response.status_code, 204)
#
#     def test_department_create(self):
#         url = reverse('department-list')
#         response = self.client.post(url, data={
#             'clinic': Clinic.title,
#             'title': 'Хирургия',
#             'head_doctor': 'Name of doctor'
#         }
#     )
#
#         self.assertEqual(response.status_code, 201)
#
#     def test_department_update(self):
#         department = Department.objects.first()
#
#         url = reverse('department-detail', args=(department.pk,))
#         response = self.client.put(url, data={
#             'clinic': Clinic.title,
#             'title': ' Онкология',
#             'head_doctor': 'Name of doctor'
#         }, content_type='application/json')
#
#         self.assertEqual(response.status_code, 200)
#
#

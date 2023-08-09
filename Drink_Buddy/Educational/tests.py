from django.test import TestCase, Client
from django.utils import timezone
from .models import Educational
from django.urls import reverse
from django.shortcuts import get_object_or_404

class EducationalModelTest(TestCase):
    def setUp(self):
        self.educational = Educational.objects.create(
            title='Test Title',
            description='Test Description',
            date=timezone.now().date()
        )

    def test_educational_model_str(self):
        self.assertEqual(str(self.educational), 'Test Title')

    def test_educational_model_fields(self):
        self.assertEqual(self.educational.title, 'Test Title')
        self.assertEqual(self.educational.description, 'Test Description')
        self.assertEqual(self.educational.date, timezone.now().date())


class EducationalViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.insight = Educational.objects.create(
            title='Test Title',
            description='Test Description',
            date='2023-01-01'
        )

    def test_all_educational_view(self):
        response = self.client.get(reverse('Educational:all_educational'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Educational/all_educational.html')
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Description')

    def test_detail_view(self):
        response = self.client.get(reverse('Educational:detail', args=[self.insight.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Educational/detail.html')
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Description')

    def test_detail_view_with_invalid_id(self):
        response = self.client.get(reverse('Educational:detail', args=[0]))
        self.assertEqual(response.status_code, 404)

    # Add more test methods as needed

    def test_detail_view_with_nonexistent_id(self):
        non_existent_id = 0
        response = self.client.get(reverse('Educational:detail', args=[non_existent_id]))
        self.assertEqual(response.status_code, 404)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.
class SnacksTest(TestCase): 
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='tester',
            email='teas@email.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            name="snack", 
            description='info', 
            purchaser=self.user
            )
    
    def test_str_method(self):
        self.assertEqual(str(self.snack),"snack")

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list_view.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['snacks']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].name, "snack")
        self.assertEqual(snacks[0].description, 'info')
        self.assertEqual(snacks[0].purchaser.username, "tester") 

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail_view.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "snack")
        self.assertEqual(snack.description, 'info')
        self.assertEqual(snack.purchaser.username, "tester")

    def test_create_view(self):
        obj = {
            'name': 'snack2',
            'description': 'info2', 
            'purchaser': self.user.id
        }
        url = reverse('create_snack')
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertEqual(len(Snack.objects.all()),2)
        # self.assertRedirects(response, reverse('snack_detail', args=[2]))

    # def test_delete_view(self):
    #     url = reverse('delete_snack')
    #     self.client.delete(path=url, follow=True)
    #     self.assertEqual(len(Snack.objects.all()),0)
    #     # self.assertRedirects(response, reverse('snack_detail', args=[2]))
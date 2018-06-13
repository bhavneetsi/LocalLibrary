from django.test import TestCase

from catalog.models import Author
from django.urls import reverse

class AuthorListViewTest(TestCase):
     
    @classmethod 
    def setUpTestData(cls):

        num_of_author=13
        for author_num in range(num_of_author):
            Author.objects.create(first_name='testAuthor_%s' %author_num,last_name='Surname_%s' %author_num)

    def test_view_url_at_desired_location(self):
        resp = self.client.get('/catalog/authors')
        self.assertEquals(resp.status_code,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('authors'))
        self.assertEquals(resp.status_code,200)

    def test_view_template_used(self):
        resp = self.client.get(reverse('authors'))
        self.assertTemplateUsed(resp,'catalog/author_list.html')

    def test_pagination_is_10(self):
        resp = self.client.get(reverse('authors'))    
        self.assertTrue(resp.context['is_paginated'] == True)         
        self.assertTrue(len(resp.context['author_list'])==10)



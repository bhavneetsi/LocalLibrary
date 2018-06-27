from django.test import TestCase

# Create your tests here.

from catalog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big',last_name='Bob')

    def setUp(self):
        author=Author.objects.get(id=1)

    def test_first_name_lable(self):
        author=Author.objects.get(id=1)
        field_lable =author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_lable,'first name')        
    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/authors/1')
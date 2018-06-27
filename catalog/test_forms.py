from django.test import TestCase

# Create your tests here.

from catalog.forms import RenewBookForm

import datetime

from django.utils import timezone

class RenewBookFormTest(TestCase):

    def test_renew_date_to_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'renewal_date':date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_date_too_far(self):

        date= datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)

        form_data = {'renewal_date':date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_renew_date_to_max(self):
        date= datetime.date.today() + datetime.timedelta(weeks=4) 

        form_data = {'renewal_date':date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())


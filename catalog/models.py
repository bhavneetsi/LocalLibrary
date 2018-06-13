from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
	name=models.CharField(max_length=200,help_text="enter book genre")
	def __str__(self):
		return self.name
	
class Language(models.Model):
	name=models.CharField(max_length=200,help_text="Enter Book Language")
	
	def __str__(self):
		return self.name
		
class Author(models.Model):
	first_name=models.CharField(max_length=200,help_text="Enter Author Name")
	last_name=models.CharField(max_length=200,help_text="Enter Author Name")
	date_of_birth=models.DateField(null=True,blank=True)
	date_of_death=models.DateField(null=True,blank=True)
	
	
	class Meta:
		ordering = ["last_name","first_name"]
	
	def get_absolute_url(self):
		"""
		Returns the url to access a particular author instance.
		"""
		return reverse('author-details', args=[str(self.id)])
		
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return '{0}, {1}'.format(self.last_name,self.first_name)
		
		
class Book(models.Model):

	title=models.CharField(max_length=200,help_text="Enter Author Name")
	author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
	summary=models.TextField(max_length=1000,help_text="Enter Brief Description about book")
	isbn=models.CharField('ISBN',max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre=models.ManyToManyField(Genre,help_text="Select a genre for this book")
	language=models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)
	
	def display_genre(self):
		"""
		Creates a string for the Genre. This is required to display genre in Admin.
		"""
		return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
		display_genre.short_description = 'Genre'
	
	
	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('book-details', args=[str(self.id)])
    
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.title
		
import uuid # Required for unique book instances


from django.contrib.auth.models import User

class BookInstance(models.Model):
	
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Uniqueid for the book instance")
	book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
	imprint=models.CharField(max_length=200)
	due_back=models.DateField(null=True,blank=True)
	borrower=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
	
	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False
		
	LOAN_STATUS = (
		('d', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)
	status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')
	
	class Meta:
		ordering = ["due_back"]
		permissions = (("can_mark_returned", "Set book as returned"),)   

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		#return '%s (%s)' % (self.id,self.book.title)
		return '{0} ({1})'.format(self.id,self.book.title)
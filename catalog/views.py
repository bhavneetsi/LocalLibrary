from django.shortcuts import render
from django.http import request
# Create your views here.
from .models import Book,Author,BookInstance,Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.all().count()
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits + 1
    return render(request,'index.html',context={'num_books':num_books,'num_instances':num_instances,
    'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits})


from django.views import generic

class BookListView(generic.ListView):
    model = Book	
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
    

class AuthorListView(generic.ListView):
    model=Author

class AuthorDetailView(generic.DetailView):
    model=Author        

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllLoanedBooksListView(LoginRequiredMixin,generic.ListView,PermissionRequiredMixin):
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

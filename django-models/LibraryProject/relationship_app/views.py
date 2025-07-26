from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Author, Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    This view should render a simple text list of book titles and their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library, listing all books available
    in that library. This view should render a page that shows the library name and 
    all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Role checking functions


#############################################################################



# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def check_role(user, required_role):
    """Check if user has the required role"""
    if user.is_authenticated:
        try:
            # Access profile through the related name
            return user.profile.role == required_role
        except AttributeError:
            # Handle case where profile doesn't exist
            return False
    return False

# Define test functions for each role
def admin_test(user):
    return check_role(user, 'Admin')

def librarian_test(user):
    return check_role(user, 'Librarian')

def member_test(user):
    return check_role(user, 'Member')

@login_required
@user_passes_test(admin_test)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(librarian_test)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(member_test)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
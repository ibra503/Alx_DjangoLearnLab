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



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def check_role(user, required_role):
    """Check if user has the required role"""
    if user.is_authenticated:
        try:
            return user.profile.role == required_role
        except UserProfile.DoesNotExist:
            # Handle case where profile doesn't exist
            return False
    return False

def admin_required(view_func):
    """Decorator to ensure user has Admin role"""
    def wrapper(request, *args, **kwargs):
        if not check_role(request.user, 'Admin'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

def librarian_required(view_func):
    """Decorator to ensure user has Librarian role"""
    def wrapper(request, *args, **kwargs):
        if not check_role(request.user, 'Librarian'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

def member_required(view_func):
    """Decorator to ensure user has Member role"""
    def wrapper(request, *args, **kwargs):
        if not check_role(request.user, 'Member'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@admin_required
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@librarian_required
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@member_required
def member_view(request):
    return render(request, 'member_view.html')
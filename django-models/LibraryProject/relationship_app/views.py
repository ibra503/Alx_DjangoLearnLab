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



from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def check_role(user, required_role):
    try:
        return user.userprofile.role == required_role
    except:
        return False

def admin_check(user):
    if not check_role(user, 'Admin'):
        raise PermissionDenied
    return True

def librarian_check(user):
    if not check_role(user, 'Librarian'):
        raise PermissionDenied
    return True

def member_check(user):
    if not check_role(user, 'Member'):
        raise PermissionDenied
    return True

@login_required
@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html')


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

@permission_required('your_app_name.can_add_book')
def add_book(request):
    # Logic for adding a book
    pass

@permission_required('your_app_name.can_change_book')
def edit_book(request, book_id):
    # Logic for editing a book
    pass

@permission_required('your_app_name.can_delete_book')
def delete_book(request, book_id):
    # Logic for deleting a book
    pass
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
    class BookCreateView(PermissionRequiredMixin, View):
    permission_required = 'relationship_app.can_add_book
from django.contrib.auth.decorators import permission_required
    relationship_app.can_change_book relationship_app.can_delete_book
    Checks for An ‘Admin’ view that only users with the ‘Admin’ role can access. task

user_passes_test(lambda u: u.userprofile.role == 'Librarian')
    def librarian_view(request):
    return render(request, 'librarian_view.html')
    @user_passes_test(lambda u: u.userprofile.role == 'Member')
    def member_view(request):
    return render(request, 'member_view.html')
    # views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

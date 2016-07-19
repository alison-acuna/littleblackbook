from django.shortcuts import render
from .forms import ProfessionalForm
# Create your views here.
def home(request):
    """
    renders the home page
    """
    return render(request, 'littleblackbookapp/home.html', {})

def newprofessional(request):
    """
    allows user to create an entry for a new professional
    """
    if request.method == "POST":
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'littleblackbookapp/success.html', {'form': form})
    else:
        form = ProfessionalForm()
    return render(request, 'littleblackbookapp/new.html', {'form': form})

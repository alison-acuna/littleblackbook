from django.shortcuts import render
from .forms import ProfessionalForm, CompanyForm
from .models import Professional, Company
# Create your views here.
def home(request):
    """
    renders the home page
    """
    return render(request, 'littleblackbookapp/home.html', {})

def new(request):
    """
    renders the newprofessional form
    """
    if request.method == "POST":
        professionalform = ProfessionalForm(request.POST, prefix='professional')
        companyform = CompanyForm(request.POST, prefix='company')
        if professionalform.is_valid() and companyform.is_valid():
            post = professionalform.save(commit=False)
            post.save()
            post = companyform.save(commit=False)
            post.save()
            return render(request, 'littleblackbookapp/success.html', {
            'professionalform': professionalform,
            'companyform': companyform
            })
    else:
        professionalform = ProfessionalForm(prefix="professional")
        companyform = CompanyForm(prefix="company")

    return render(request, 'littleblackbookapp/new.html', {
    'professionalform': professionalform,
    'companyform': companyform
    })

# def new(request):
#     if request.method == "POST":
#             form = ProfessionalForm(request.POST)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.save()
#                 return render(request, 'littleblackbookapp/success.html', {'form': form})
#     else:
#         form = ProfessionalForm()
#
#     return render(request, 'littleblackbookapp/newprofessional.html', {'form': form})
#     if request.method == "POST":
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return render(request, 'littleblackbookapp/success.html', {'form': form})
#     else:
#         form = CompanyForm()
#     return render(request, 'littleblackbookapp/newcompany.html', {'form': form})
#
#
#
# def newprofessional(request):
#     """
#     renders the newprofessional form
#     """
#     if request.method == "POST":
#         form = ProfessionalForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return render(request, 'littleblackbookapp/success.html', {'form': form})
#     else:
#         form = ProfessionalForm()
#
#     return render(request, 'littleblackbookapp/newprofessional.html', {'form': form})
#
# def newcompany(request):
#     if request.method == "POST":
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return render(request, 'littleblackbookapp/success.html', {'form': form})
#     else:
#         form = CompanyForm()
#     return render(request, 'littleblackbookapp/newcompany.html', {'form': form})


def edit(request, id):
    """
    allows user to edit existing member
    """
    member = get_object_or_404(Member, pk=id)
    if request.method == "POST":
        form = ProfessionalForm(request.POST, instance=professional)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'littleblackbookapp/success.html', {'form': form})
    else:
        form = MemberForm(instance=professional)
    return render(request, 'littleblackbookapp/new.html', {
    'form': form,
    'id': id
    })

def professional(request, id):
    """
    renders individual member data
    """
    professional = Professional.objects.get(pk=id)
    # # meetups pull starts here
    # professional_id = member.meetupid
    # r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
    # meetups = (r.json()['topics'])
    # li = []
    # topics = (r.json()['topics'])
    # for topic in topics:
    #     li.append(topic['name'])
    # # meetups pull ends here
    return render(request, 'littleblackbookapp/professional.html', {
        'professional': professional,
        # 'meetups': li
    })

def displayall(request):
    """
    displays all members in database
    """
    professionals = Professional.objects.all()
    for professional in professionals:
        # # meetups pull starts here
        # try:
        #     meetup_id = member.meetupid
        #     r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
        #     meetups = (r.json()['topics'])
        #     li = []
        #     topics = (r.json()['topics'])
        #     for topic in topics:
        #         li.append(topic['name'])
        # except:
        #     continue
        # # meetups pull ends here
        return render(request, 'littleblackbookapp/displayall.html', {
            'professionals': professionals,
        # 'meetups': li
    })

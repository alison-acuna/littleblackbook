from django.shortcuts import render
from .forms import ProfessionalForm
from .models import Professional
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

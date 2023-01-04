from django.shortcuts import render,redirect
from django.urls import reverse
from django.conf import settings
from crm_app.EmailBackEnd import EmailBackEnd
from django.views import View
from .forms import CustomerRegistrationForm,LeadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import Leads,CustomUser
import io,csv



def Error404(request, exception):
    return render(request,'errors/404.html')

@login_required(login_url='login')
def home(request):
    return render(request,"homepage/home.html")

def admin_login(request):
    if request.method == "POST":
        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        print(request.POST.get("username"))
        if user!=None:
            login(request,user)
            if user.is_superuser == 1:
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(reverse("user_dashboard"))
        else:
            messages.error(request,"Invalid Login Or Password !!")
            return redirect('login')
            # return HttpResponseRedirect("login")
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"homepage/login.html")

# def add_user(request):
#     return render(request,"customer/customer.html")

def user_Dashboard(request):
    return render(request,"customer/user_dashboard.html")




class customerregistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'homepage/register.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password1=form.cleaned_data["password1"]
            password2=form.cleaned_data["password2"]

            if password1 != password2:
                return redirect('signup')
            user=CustomUser.objects.create_user(username=username,password=password1,email=email,user_type=2)
            user.save()
            messages.success(request,'Congratulations!! Registered Successfully')
           
            

        return render(request,'homepage/register.html',{'form':form})


def customer_list(request):
    
    return render(request,"customer/customer-list.html")

def profile(request):
    
    return render(request,"homepage/profile.html")




class leadView(View):
    
    def get(self,request):
        lead = Leads.objects.all()
        # profile = Profile.objects.all()
        
        form = LeadForm()
        return render(request,'customer/customer.html',{'form':form,'lead':lead})
    def post(self,request):
        form = LeadForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Lead Add Successfully')
            form.save()
            return redirect('add_lead')

        # return render(request,'customer/customer.html',{'form':form})

def edit_view(request):
    lead = Leads.objects.all()
    
    context={
        'lead':lead
    }
    return render(request,"customer/customer.html",context)

def update_lead(request):
    if request.method == "POST":
        lead_id = request.POST.get('lead_id')
        assign_id = request.POST.get('assign')
        lead_name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        destination = request.POST.get("destination")
        no_of_days = request.POST.get("no_of_days")
        no_of_people = request.POST.get("no_of_people")
        city2 = request.POST.get("city_nw")

        try:
            # profile = Profile.objects.get(user=assign_id)
            lead = Leads.objects.get(id=lead_id)
            
            lead.name = lead_name
            lead.phone = mobile
            lead.email = email
            lead.destination = destination
            lead.no_of_days = no_of_days
            lead.number_of_people = no_of_people
            lead.city = city2
            lead.assign=profile
            lead.save()
            return redirect('add_lead')
        except:
            messages.error(request,"Something Error Try Again !!")
            return redirect("add_lead")
            

def mylead(request):
    users = request.user
    # profile = Profile.objects.all()
    lead = Leads.objects.filter(assign = request.user.id)
   
    return render(request,'customer/my_lead.html',{'lead':lead})
        
            
def notification(request):
    return render(request,'customer/notification.html')
        
        
def upload_csv(request):
    data = Leads.objects.all()
    prompt = {
        'order': 'name,phone_number,email,destination,no_of_days,number_of_people,date,city',
        'profiles': data 
    }
    if request.method == "GET":
        return render(request, 'customer/customer.html', prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        
        Leads.objects.update_or_create(
        # id=column[0],
        name=column[0],
        phone=column[1],
        email=column[2],
        destination=column[3],
        no_of_days=column[4],
        number_of_people=column[5],
        date=column[6],
        city=column[7],
        # assign=column[8],
        
        
        # phone_number=column[2],
        
       
    )
    context = {}

    return redirect('add_lead')


def agent_list(request):
    # profile = Profile.objects.all()
    return render(request,'agent/agent-list.html')

def agent_lead_view(request):
    users = request.user
    lead = Leads.objects.filter(assign = request.user.id)
    print(lead)
    print(users)
    return render(request,"agent/lead_view.html",{'lead':lead})
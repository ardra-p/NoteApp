from django.shortcuts import render,redirect
from .models import Note,Customer
from django.core.paginator import Paginator
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@login_required(login_url='login')
def index(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    jango_user = request.user
    try:
        customer = Customer.objects.get(user=jango_user)
    except Customer.DoesNotExist:
        return redirect ('logout')
    note = Note.objects.filter(user=customer).order_by('-created_at')
    note_pagenator=Paginator(note,3)
    note=note_pagenator.get_page(page)
    print("Note ",note)
    return render(request,'index.html',{'notes':note})


@login_required(login_url='login')
def create_note(requset):
    if requset.method=="POST":
        title=requset.POST.get('title')
        content=requset.POST.get('content')
        if title and content:
            jango_user= requset.user
            try:
               customer = Customer.objects.get(user=jango_user)
            except Customer.DoesNotExist:
                #customer = Customer.objects.create(user=jango_user, name=jango_user.username, email=jango_user.email)  
                return redirect('logout')
            Note.objects.create(user=customer,title=title,content=content)
            return redirect('home')
            
    return render(requset,'create.html')

@login_required(login_url='login')
def list_note(request):
    jango_user = request.user
    try:
        customer = Customer.objects.get(user=jango_user)
    except Customer.DoesNotExist:
        return redirect('logout')
    note = Note.objects.filter(user=customer).order_by('-created_at')
    return render(request,'list.html',{'notes':note})


@login_required(login_url='login')
def single_note_list(request,pk):
    note = Note.objects.get(pk=pk)
    return render(request,'single_note.html',{'notes':note})


def edit_note(request,pk):
    note = Note.objects.get(pk=pk)

    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        note.title = title
        note.content = content
        note.save()
        if 'listedit' in request.POST:
          return redirect('notes',pk=note.id)
        else:
          return redirect('notelist')


    

    return render(request,'create.html',{'notes':note})


def delete_note(request,pk):
    note = Note.objects.get(pk=pk)
    if note:
        note.delete()
        return redirect('home')


def home_page(request):
    return render(request,'home_page.html')
       

def user_logout(request):
    logout(request)
    return redirect('home_page')

def user_login(request):
    context={}
    if request.method == "GET":
        form = request.GET.get("form")
        if form == "register":
            context['register'] = True
        else:
            context['register'] = False

     
    if request.method == "POST":
        form_type = request.POST.get("form_type")
     
        if form_type == "login":
            context['register']=False
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successful', extra_tags='successs')
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password", extra_tags="login")
            except Exception as e:
               errorss = " invalid credentials"
               messages.error(request,errorss, extra_tags="login")

                             
        elif form_type == "register":
            context['register']=True
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                messages.error(request, 'Passwords do not match', extra_tags='errors')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists', extra_tags='errors')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                Customer.objects.create(user=user,
                                    name=username,email=email)
                succsess = "Your account has been created successfully!"
                messages.success(request,succsess,extra_tags='successs')
                return redirect('home')
              
    return render(request, 'register_login.html',context)


def custom_404_view(request,exception):
    return render(request,'404.html',status=404)
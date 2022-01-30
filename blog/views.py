from datetime import date
from django.http import HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import addPost
import json
from django.views.generic import View, TemplateView
from datetime import timedelta, datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignUpForm
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve
# from django.views import View
# Create your views here.
def index(request):
    # earliest and latest throw error if query is empty
    # get method give error when queryset is empty but filter give empty queryset without error
    # obj = addPost.objects.all().earliest()
    # print(obj.postId)
    # obj = addPost.objects.latest()
    # print(obj.postId)

    # print(now())
    # other way to do that
    # dt1 = timezone.now() - timedelta(hours=3)
    # dt2 = timezone.now() - timedelta(minutes=1)
    # PostsLastHour = addPost.objects.filter(date__range=[dt1, dt2])
    # print(PostsLastHour)
    current_time = timezone.now()

    # start will be 2 hours ago
    start_time = current_time - timedelta(hours=2)

    # using 'greater than or equal' filter
    qs = addPost.objects.filter(date__gte=start_time)

    # careful: if the queryset is empty, the 'obj' will be 'None'
    obj = (qs.first())
    print(obj)
    # careful: in your version, this will raise IndexError if queryset is empty
    # print(qs[0].date) #empty queryset can not be indexed


    try:
        obj = addPost.objects.get(postId=5)
        print(obj)
    except ObjectDoesNotExist as e:
        print(e)
        print("nh huwa")
        obj = None
        print(obj)
    obj = list(addPost.objects.all().order_by("-date"))[0:10]
    print(obj)
    return render(request, "blog\home.html", {"obj":obj})
def writePost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                title = request.POST.get("title")
                category = request.POST.get("category")
                content = request.POST.get("content")
                image = request.FILES['image']
                addpost = addPost(title=title, category=category, content=content, image=image)
                addpost.save()
                messages.success(request, "Your post has been successfully added...",extra_tags='#check-circle-fill')
            except Exception as e:
                messages.error(request, "Something went wrong.. Make sure all fields must be filled, title should be clear, content should contain atleast 100 words", extra_tags='#exclamation-triangle-fill')
        return render(request, "blog/writepost.html")
    else:
        messages.warning(request, "Please login first: ", extra_tags='#exclamation-triangle-fill')
        return redirect("/blog/login")
    

class Template(TemplateView):
    def get(self, request, *args, **kwargs):
        # print(args, kwargs) #Empty
        if(resolve(request.path).url_name == "technology"):
            obj = list(addPost.objects.filter(category="Technology").values())[0:2]
        elif(resolve(request.path).url_name == "randomFacts"):
            obj = list(addPost.objects.filter(category="randomFacts").values())[0:2]
        elif(resolve(request.path).url_name == "sports"):
            obj = list(addPost.objects.filter(category="Sport").values())[0:2]
        elif(resolve(request.path).url_name == "poets"):
            obj = list(addPost.objects.filter(category="Poets").values())[0:2]
        try:
            title = obj[0]['category']
        except Exception:
            title = None
        return render(request, "blog/categories.html", {"obj":obj, 'title':title})
class JsonTemplate(View):
    def get(self, request, *args, **kwargs):
        # print(resolve(request.path).url_name)
        # print(request.path)
        # url_name = resolve(request.path).url_name
        lower = ""
        upper = kwargs.get("num_posts")
        # print(request, args, kwargs)
        lower = upper - 3
        if(resolve(request.path).url_name == "jsonTechnology"):
            obj = list(addPost.objects.filter(category="Technology").values())[lower:upper]
        # print(list(addPost.objects.values('postId', 'title'))) #give lists values
        # print(addPost.objects.values('postId', 'title'))  #give querysets of posid and title and only
            obj_size = list(addPost.objects.filter(category="Technology").values())
        elif(resolve(request.path).url_name == "jsonRandomFacts"):
            obj = list(addPost.objects.filter(category="randomFacts").values())[lower:upper]
            obj_size = list(addPost.objects.filter(category="randomFacts").values())
        elif(resolve(request.path).url_name == "jsonSports"):
            obj = list(addPost.objects.filter(category="Sport").values())[lower:upper]
            obj_size = list(addPost.objects.filter(category="Sport").values())
        elif(resolve(request.path).url_name == "jsonPoets"):
            obj = list(addPost.objects.filter(category="About poeters").values())[lower:upper]
            obj_size = list(addPost.objects.filter(category="About poeters").values())
        max_length = len(obj_size)
        check = True if upper > max_length else False
        return JsonResponse({"data":obj, "check":check})

def TemplateView(request, *args, **kwargs):
    print(args, kwargs)
    post = addPost.objects.filter(postId=kwargs.get("myid"))[0]
    return render(request, "blog/templateview.html", {"post":post})
#     addpost = list(addPost.objects.filter(category='Technology').values())
#     print(addpost)
#     context = json.dumps({"addDict":addpost})
#     # return HttpResponse(context)
#     return render(request, "blog/technology.html", {"addDict":context, "addpost":addpost, "title":addpost[0]})



def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, f"Welcome: Your account has been created..", extra_tags='#check-circle-fill')
            else:
                messages.warning(request, "Something went wrong..", extra_tags='#exclamation-triangle-fill')
        else:
            fm = SignUpForm(auto_id="my_%s")

        return render(request, "blog/signup.html", {"form":fm})
    else:
        return redirect("/blog")

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = CustomAuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get("username")
                upass = fm.cleaned_data.get("password")
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome {request.user.first_name}: You are successfully logged in. ", extra_tags='#check-circle-fill')
                    return redirect("/blog/")
            else:
                messages.error(request, "You are entering wrong username or password", extra_tags='#exclamation-triangle-fill')
        else:
            fm  = CustomAuthenticationForm()
        return render(request, "blog/login.html", {"form":fm})
    else:
        return redirect("/blog")
def Logout(request):
    logout(request)
    messages.success(request, "Your account has been logged out", extra_tags='#check-circle-fill')
    return redirect("/blog/login")
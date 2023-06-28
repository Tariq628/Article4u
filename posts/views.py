from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import View, TemplateView
from .forms import SignUpForm
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve

# Create your views here.


def index(request):
    obj = list(Post.objects.all().order_by("-date"))[0:10]
    return render(request, "blog/home.html", {"obj": obj})


def write_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                title = request.POST.get("title")
                category = request.POST.get("category")
                content = request.POST.get("content")
                image = request.FILES['image']
                post = Post(title=title, category=category, content=content, image=image)
                post.save()
                messages.success(request, "Your post has been successfully added...",
                                 extra_tags='#check-circle-fill')
            except Exception:
                messages.error(
                    request,
                    """
                    Something went wrong.. Make sure all fields must be filled,
                    title should be clear, content should contain atleast 100 words
                    """,
                    extra_tags='#exclamation-triangle-fill'
                )
        return render(request, "blog/writepost.html")
    else:
        messages.warning(request, "Please login first: ", extra_tags='#exclamation-triangle-fill')
        return redirect("/login")


class template(TemplateView):
    def get(self, request, *args, **kwargs):
        # print(args, kwargs) #Empty, bcz there is no slug
        catName = resolve(request.path).url_name
        obj = list(Post.objects.filter(category=catName).values())[0:2]
        try:
            title = obj[0]['category']
        except Exception:
            title = None
        return render(request, "blog/categories.html", {"obj": obj, 'title': title})


class json_template(View):
    def get(self, request, *args, **kwargs):
        lower = ""
        upper = kwargs.get("num_posts")
        lower = upper - 3
        urlName = resolve(request.path).url_name
        urlName = urlName.replace("json", "")
        obj = list(Post.objects.filter(category=urlName).values())[lower:upper]
        obj_size = list(Post.objects.filter(category=urlName).values())
        max_length = len(obj_size)
        check = True if upper > max_length else False
        return JsonResponse({"data": obj, "check": check})


def template_view(request, *args, **kwargs):
    post = Post.objects.filter(postId=kwargs.get("myid"))[0]
    return render(request, "blog/templateview.html", {"post": post})


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Welcome: Your account has been created..",
                                 extra_tags='#check-circle-fill')
                return redirect("/login")
            else:
                messages.warning(request, "Something went wrong..",
                                 extra_tags='#exclamation-triangle-fill')
        else:
            fm = SignUpForm(auto_id="my_%s")

        return render(request, "blog/signup.html", {"form": fm})
    else:
        return redirect("/")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = CustomAuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get("username")
                upass = fm.cleaned_data.get("password")
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request,
                        f"Welcome {request.user.first_name}: You are successfully logged in. ",
                        extra_tags='#check-circle-fill'
                    )
                    return redirect("/")
            else:
                messages.error(request, "You are entering wrong username or password",
                               extra_tags='#exclamation-triangle-fill')
        else:
            fm = CustomAuthenticationForm()
        return render(request, "blog/login.html", {"form": fm})
    else:
        return redirect("/")


def user_logout(request):
    logout(request)
    messages.success(request, "Your account has been logged out", extra_tags='#check-circle-fill')
    return redirect("/login")

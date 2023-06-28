from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import View, TemplateView
from .forms import SignUpForm
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve


def index(request):
    posts = Post.objects.all().order_by("-date")[0:10]
    return render(request, "blog/home.html", {"posts": posts})


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
                messages.success(request, "Your post has been successfully added.",
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
    def get(self, request):
        cat_name = resolve(request.path).url_name
        posts = Post.objects.filter(category=cat_name).values()[0:2]
        title = posts[0]['category'] if posts else None
        return render(request, "blog/categories.html", {"posts": posts, 'title': title})


class json_template(View):
    def get(self, request, *args, **kwargs):
        upper = int(kwargs.get("num_posts"))
        lower = max(upper - 3, 0)  # Ensure lower doesn't go below 0
        url_name = resolve(request.path).url_name
        url_name = url_name.replace("json_", "")
        posts = list(Post.objects.filter(category=url_name).values()[lower:upper])
        max_length = Post.objects.filter(category=url_name).count()
        check = upper > max_length
        return JsonResponse({"posts": posts, "check": check})


def template_view(request, *args, **kwargs):
    post = Post.objects.filter(id=kwargs.get("post_id"))[0]
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

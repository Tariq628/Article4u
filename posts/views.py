from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse
from .models import Comment, Post
from django.views.generic import View, TemplateView
from .forms import SignUpForm
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    posts = Post.objects.all().order_by("-created_at")[0:10]
    return render(request, "home.html", {"posts": posts})


def write_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                title = request.POST.get("title")
                category = request.POST.get("category")
                content = request.POST.get("content")
                image = request.FILES['image']
                post = Post(title=title, category=category, content=content, image=image, created_by=request.user)
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
        return render(request, "writepost.html")
    else:
        messages.warning(request, "Please login first: ", extra_tags='#exclamation-triangle-fill')
        return redirect("/login")


@method_decorator(login_required, name='dispatch')
class template(TemplateView):
    def get(self, request):
        cat_name = resolve(request.path).url_name
        posts = Post.objects.filter(category=cat_name)[0:2]
        return render(request, "categories.html", {"posts": posts, 'title': cat_name.capitalize()})


@method_decorator(login_required, name='dispatch')
class json_template(View):
    def get(self, request, *args, **kwargs):
        upper = int(kwargs.get("num_posts"))
        lower = max(upper - 3, 0)  # Ensure lower doesn't go below 0
        url_name = resolve(request.path).url_name
        url_name = url_name.replace("json_", "")
        posts = list(
            Post.objects.filter(category=url_name).values(
                'id', 'title', 'category', 'image', 'content', 'created_at',
                'created_by__username'  # Include the username field
            )[lower:upper]
        )
        max_length = Post.objects.filter(category=url_name).count()
        check = upper > max_length
        print(check)
        return JsonResponse({"posts": posts, "check": check})


@login_required(login_url='login')
def template_view(request, *args, **kwargs):
    post = Post.objects.filter(id=kwargs.get("post_id"))[0]
    return render(request, "templateview.html", {"post": post})


@login_required(login_url='login')
def post_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
    return redirect("/template-view/6")


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

        return render(request, "signup.html", {"form": fm})
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
        return render(request, "login.html", {"form": fm})
    else:
        return redirect("/")


def user_logout(request):
    logout(request)
    messages.success(request, "Your account has been logged out", extra_tags='#check-circle-fill')
    return redirect("/login")

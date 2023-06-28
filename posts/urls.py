from django.urls import path
from . import views
from .views import template, json_template

urlpatterns = [
    # API to post a comment
    path("", views.index, name="index"),
    path("write-post/", views.write_post, name="write_post"),
    path("random-facts/", template.as_view(), name="random_facts"),
    path(
        "randomfacts/<int:num_posts>/", json_template.as_view(), name="json_random_facts"
    ),
    path("technology/", template.as_view(), name="technology"),
    path("technology/<int:num_posts>/", json_template.as_view(), name="json_technology"),
    path("sports/", template.as_view(), name="sports"),
    path("sports/<int:num_posts>/", json_template.as_view(), name="json_sports"),
    path("poets/", template.as_view(), name="poets"),
    path("poets/<int:num_posts>/", json_template.as_view(), name="json_poets"),
    path("template-view/<int:myid>/", views.template_view, name="template_view"),
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]

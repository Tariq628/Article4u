from django.urls import path
from . import views
from .views import Template, JsonTemplate
urlpatterns = [
    # API to post a comment
    path("", views.index, name="index"),
    path("write-post/", views.writePost, name="writePost"),
    path("randomfacts/", Template.as_view(), name="randomFacts"),
    path("randomfacts/<int:num_posts>/", JsonTemplate.as_view(), name="jsonRandomFacts"),
    path("technology/", Template.as_view(), name="Technology"),
    path("technology/<int:num_posts>/", JsonTemplate.as_view(), name="jsonTechnology"),
    path("sports/", Template.as_view(), name="Sports"),
    path("sports/<int:num_posts>/", JsonTemplate.as_view(), name="jsonSports"),
    path("poets/", Template.as_view(), name="Poets"),
    path("poets/<int:num_posts>/", JsonTemplate.as_view(), name="jsonPoets"),
    path("templateview/<int:myid>/", views.TemplateView, name="templateView"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.Logout, name="logout")
]
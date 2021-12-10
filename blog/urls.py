from django.urls import path
from . import views
from .views import Template, JsonTemplate
urlpatterns = [
    # API to post a comment
    # path("", views.templateView, name='templateView'),
    path("", views.index, name="index"),
    path("write-post/", views.writePost, name="writePost"),
    path("technology/", Template.as_view(), name="technology"),
    path("technology/<int:num_posts>/", JsonTemplate.as_view(), name="jsonTechnology"),
    path("templateview/<int:myid>/", views.TemplateView, name="jsonTechnologyView"),
    path("randomfacts/", Template.as_view(), name="randomFacts"),
    path("randomfacts/<int:num_posts>/", JsonTemplate.as_view(), name="jsonRandomFacts"),
    path("randomfactsview/<int:myid>/", views.TemplateView, name="randomFactsView"),
    path("sports/", Template.as_view(), name="sports"),
    path("sports/<int:num_posts>/", JsonTemplate.as_view(), name="jsonSports"),
    path("poets/", Template.as_view(), name="poets"),
    path("poets/<int:num_posts>/", JsonTemplate.as_view(), name="jsonPoets"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.Logout, name="logout")
]
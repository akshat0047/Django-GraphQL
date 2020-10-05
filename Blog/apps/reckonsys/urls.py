from django.contrib import admin
from django.urls import path
from . import views as v
from graphene_django.views import GraphQLView
from Blog.schema import schema

app_name = "reckonsys"

urlpatterns = [
        path('graphql/', GraphQLView.as_view(graphiql=True), name='graphql')
     ]

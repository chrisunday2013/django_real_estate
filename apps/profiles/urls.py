from django.urls import path 

from .views import (AgentListView, GetProfileView, TopAgentListView, UpdateProfileView)


urlpatterns = [
    path("me/", GetProfileView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileView.as_view(), name="update_profile"),
    path("agents/all/", AgentListView.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentListView.as_view(), name="top-agents"),
]
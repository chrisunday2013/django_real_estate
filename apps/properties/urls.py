from django.urls import path 

from . import views 


urlpatterns = [
    path("all/", views.ListAllPropertiesView.as_view(), name="all-properties"),
    path("agents/", views.ListAgentsPropertyView.as_view(), name="agent-properties"),
    path("details/<slug:slug>/", views.PropertyDetailView.as_view(), name="property-details"),
    path("search/", views.PropertySearchAPI.as_view(), name="property-search"),
    path("update/<slug:slug>/", views.update_property_api, name="update-property"),
    path("delete/<slug:slug>/", views.delete_property_api, name="delete-property"),
    path("create/", views.create_property_api, name="property-create"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('regist-state', views.regist_states),
    path('states/<int:pk>', views.get_all_states),
    path('category/<int:pk>', views.get_all_category),
    # path('states/<int:pk>', views.get_user_comment),
    path('state-not-found', views.state_not_found),
    path('search', views.search_state),
    path('add-comment', views.add_comment),
    path('sign-up', views.register),
]
from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name = "poll_index"), #when someone visits the root location, render list_view
    path('polls/<int:poll_id>', detail_view, name = 'poll_detail'), #matches list.html

    # essentially when user visits poll/poll_id we will render detail.html through detail_view. Name of this url pattern is "poll_detail"
    # when user visits home page, when they click on a title they will be taken to poll/poll_id. Django knows to do this because it searchs for "poll_detail" url
]
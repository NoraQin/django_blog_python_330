from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name = 'poll_index'),
    #path('polls/<int:poll_id>', detail_view, name = 'poll_detail'), #matches list.html
    path('polls/<int:pk>', PollDetailView.as_view(), name = 'poll_detail')
]
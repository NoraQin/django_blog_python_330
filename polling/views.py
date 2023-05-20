from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

def list_view(request):
    context = {'polls': Poll.objects.all()}
    # take every single poll in Poll table
    # pass it into "polls" as html context

    return render(request, 'polling/list.html', context)
    # this is the reason why we create a polling folder under template
    # if we don't here it will just say render(request, 'list.html', context) which
    # isn't very descriptive

def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        if request.POST.get('vote') == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
    
    context = {'poll': poll}

    return render(request, 'polling/detail.html', context)

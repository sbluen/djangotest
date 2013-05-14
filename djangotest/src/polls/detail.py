from django.shortcuts import render, get_object_or_404
from polls.models import Poll
def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
from django.shortcuts import render, get_object_or_404

from journal.models import Entry


def entries_list(request):
    entries = Entry.objects.all().order_by("-created")
    return render(request, 'journal/entries_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'journal/entry_detail.html', {'entry': entry})

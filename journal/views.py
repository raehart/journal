from django.shortcuts import render


def entries_list(request):
    return render(request, 'journal/entries_list.html')


def entry_detail(request):
    return render(request, 'journal/entry_detail.html')

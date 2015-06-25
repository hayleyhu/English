from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'history_and_future_of_the_book/post_list.html', {})
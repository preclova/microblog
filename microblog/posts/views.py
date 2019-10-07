from django.shortcuts import render
from django.views.generic import View


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'posts/index.html')


def hello_world(request):
    context = {
        'name': 'Piotr',
    }
    return render(request, 'posts/index.html', context)

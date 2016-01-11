from django.http.response import HttpResponse
from django.shortcuts import render
from test_tag.settings import TEMPLATE_DIRS


def test_tags(request):
    print TEMPLATE_DIRS
    return render(request, 'test.html', locals())
    # return HttpResponse("helloworld")
    # return render(request, 'D:\\workplace\\test_tag\\templates\\test\\test.html', locals())

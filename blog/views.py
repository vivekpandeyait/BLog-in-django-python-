from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages


from .models import touch, Blog, data


def index(request):
    return render(request, 'blog/home.html')

def footer(request):
    return render(request, 'blog/footer.html')

def logout1(request):
    return render(request, 'blog/home.html')



def upload(request):
    if request.method == 'POST':
        title = request.POST.get('name1')
        Your_body = request.POST.get('name2')
        my_author = request.POST.get('name3')
        var_data = data(title=title, body=Your_body, author=my_author)
        var_data.save()
        return render(request, 'blog/thanks.html')
    else:
        return render(request, 'blog/upload.html')


def about(request):
    var_1 = Blog.objects.all()
    return render(request, 'blog/about.html', {'var_1': var_1})


def detail(request, blog_id):
    detail_page = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail_blog': detail_page})


def contact(request):
    if request.method == 'POST':
        Your_firstname = request.POST.get('name1')
        Your_lastname = request.POST.get('name2')
        Subject = request.POST.get('name3')
        Message = request.POST.get('name4')

        var_touch = touch(first_name=Your_firstname, last_name=Your_lastname, subject=Subject, message=Message)
        var_touch.save()
        return render(request, 'blog/thanks.html')

    else:
        return render(request, 'blog/contact.html')

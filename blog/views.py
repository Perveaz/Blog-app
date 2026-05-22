from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# BLOG LIST

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})

# BLOG DETAILS

def blog_details(request, id):
    blogs = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blogs': blogs})

# BLOG CREATE

def blog_create(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Blog.objects.create(title=title, content=content)
            return redirect('blog_list')
    return render(request,'blog/create.html')

# BLOG UPDATE

def blog_update(request, id):
    blogs = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            blogs.title = title
            blogs.content = content
            blogs.save()
            return redirect('blog_details', id = blogs.id)
    return render(request, 'blog/update.html',{'blogs':blogs})

# BLOG DELETE

def blog_delete(request, id):
    blogs = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        blogs.delete()
        return redirect('blog_list')
    return render(request, 'blog/delete.html',{'blogs':blogs})
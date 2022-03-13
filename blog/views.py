from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.http import Http404
# Create your views here.


class BlogList(ListView):
    template_name = "blog/blog-list.html"
    model = Blog
    paginate_by =1

    def get_queryset(self):
        return Blog.objects.get_published()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['setting'] = Information.objects.first()
    #     return context




def blog_detail(request, pk):
    # settings = Information.objects.first()
    blog = Blog.objects.get(id=pk)
    # blog_form = CreateBlogForm(request.POST or None, initial={'blog_id': blog_id})
    if blog is None:
        raise Http404()

    blog.view += 1
    blog.save()

    # if blog_form.is_valid():
    #     full_name = blog_form.cleaned_data.get("full_name")
    #     email = blog_form.cleaned_data.get("email")
    #     text = blog_form.cleaned_data.get("text")
    #     blogId = blog_form.cleaned_data.get("blog_id")

    #     blog = Blog.objects.get_by_id(blog_id=blogId)

    #     new_comment = BlogForm.objects.create(full_name=full_name, email=email, text=text, blogId=blog.id)
    #     if new_comment is not None:
    #         return redirect(f"/blog/{blog.id}/{blog.title}")
    #     blog_form = CreateBlogForm()

    # comments = BlogForm.objects.filter(blogId=blog_id, is_read=True)

    context = {
        "blog": blog,
        # "setting": settings,
        # "blog_form": blog_form,
        # "comments": comments
    }
    return render(request, "blog/blog-detail.html", context)
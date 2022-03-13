from django.shortcuts import redirect, render
from django.views.generic import ListView

from blog.forms import BlogCommentForm
from .models import *
from django.http import Http404
# Create your views here.


class BlogList(ListView):
    template_name = "blog/blog-list.html"
    model = Blog
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.get_published()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['setting'] = Information.objects.first()
    #     return context




def blog_detail(request, pk):
    # settings = Information.objects.first()
    blog = Blog.objects.get(id=pk)
    comment_form = BlogCommentForm(request.POST)
    if blog is None:
        raise Http404()

    blog.view += 1
    blog.save()

    if comment_form.is_valid():
        full_name = comment_form.cleaned_data.get("full_name")
        email = comment_form.cleaned_data.get("email")
        text = comment_form.cleaned_data.get("text")
        blog = Blog.objects.get(id=pk)

        new_comment = BlogComment.objects.create(full_name=full_name, email=email, text=text, blog=blog)
        if new_comment is not None:
            return redirect(f"/blog/{blog.id}/")
    else:
        comment_form = BlogCommentForm()

    comments = BlogComment.objects.filter(blog=blog, is_read=True)

    context = {
        "blog": blog,
        # "setting": settings,
        "comment_form": comment_form,
        "comments": comments
    }
    return render(request, "blog/blog-detail.html", context)
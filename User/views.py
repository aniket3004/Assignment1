from django.shortcuts import render
from . forms import PostForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required,name='post')
class PostView(View):
    def get(self,request):
        form = PostForm()
        context = {'form':form}
        return render(request,"User/post.html",context)

    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
                messages.success(request,"Congratulations!!, Post Created Successfully!!")
                form.save()
        context = {'form':form}
        return render(request,"User/post.html",context)

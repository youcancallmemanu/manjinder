from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse
from .models import Post
from .models import BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)




def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
    if len(comment)>0:
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    else:
        messages.warning(request,"Please write something")
    

        
    return redirect(f"/blog/{post.slug}")

# def postComment(request):
#     if request.method == "POST":
#         comment=request.POST.get('comment')
#         user=request.user
#         postSno =request.POST.get('postsno')
#         post= Post.objects.get(sno=postSno)
#         parentSno= request.POST.get('parentsno')
#         if parentSno=='parentsno':
#             comment=BlogComment(comment= comment, user=user, post=post)
#             comment.save()
#             messages.success(request, "Your comment has been posted successfully")
#         else:
#             parent= BlogComment.objects.get(sno=parentSno)
#             comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
#             comment.save()
#             messages.success(request, "Your reply has been posted successfully")
#         return redirect(f"/blog/{post.slug}")

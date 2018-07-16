from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import ArticleColumn,ArticlePost
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Comment
from .forms import CommentForm

def article_titles(request,username=None):
	if username:
		user=User.objects.get(username=username)
		articles_title=ArticlePost.objects.filter(author=user)
		try:
			userinfo=user.userinfo
		except:
			userinfo=None
	else:
		articles_title=ArticlePost.objects.all()
	paginator=Paginator(articles_title,5)
	page=request.GET.get('page')
	try:
		current_page=paginator.page(page)
		articles=current_page.object_list
	except PageNotAnInteger:
		current_page=paginator.page(1)
		articles=current_page.object_list
	except EmptyPage:
		current_page=paginator_page(paginator.num_pages)
		articles=current_page.object_list
	if username:
		return render(request,"article/list/author_articles.html",{"articles":articles,"page":current_page,"user":user,"userinfo":userinfo})
	else:
		return render(request,"article/list/article_titles.html",{"articles":articles,"page":current_page})


'''def article_detail(request,id,slug):
	article=get_object_or_404(ArticlePost,id=id,slug=slug)
	return render(request,"article/list/article_detail.html",{"article":article})'''

def article_detail(request,id,slug):
	article=get_object_or_404(ArticlePost,id=id,slug=slug)

	if request.method=="POST":
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.article=article
			new_comment.commentator=request.user
			new_comment.save()
	else:
		comment_form=CommentForm
	return render(request,"article/list/article_detail.html",{"article":article,"comment_form":comment_form})
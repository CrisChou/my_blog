from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'main/index.html')


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/file_manage/index')
		else:
			return render(request, 'myadmin/login.html', {'msg':'用户名不存在或密码错误'})
	return render(request,'main/login.html',{})


def user_logout(request):
	"""
    登出
    """
	# logger.info("logout(): Administrator(%s) whose ip is %s logouted UBoxAdmin..." % (
	# 	request.user, request.META['REMOTE_ADDR']))
	logout(request)
	return HttpResponseRedirect("/file_manage/login")


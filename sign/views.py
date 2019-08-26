from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from sign.models import menus
# Create your views here.

def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, "index.html")

# 登录动作
@login_required
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == 'admin123':
        if user == None:
            auth.login(request, user) # 登录
            # return HttpResponse('登录成功')
            #response.set_cookie('user', username, 3600) # 添加浏览器cookie
            response = HttpResponseRedirect('/event_manage/')
            request.session['user'] = username # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error':'用户名或密码错误!'})


# 接口管理
# @login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '') #读取浏览器cookie
    username = request.session.get('user', '') # 读取浏览器session
    return render(request, 'event_manage.html', {'user': username})
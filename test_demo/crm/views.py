from django.shortcuts import render
from crm.models import UserInfo
from django.shortcuts import HttpResponse
# Create your views here.


def loginView(request):
    # 处理http的post请求
    title = '用户提交数据'
    if request.method == 'POST':
        infos = request.POST
        # print(infos)
        username = infos.get('username')
        phone = infos.get('phone')
        age = infos.get('age')
        # print(age)
        print(username, phone)
        if UserInfo.objects.filter(phone=phone):
            state = '该用户已存在请重新填写'
            return render(request, 'register.html', locals())
        else:
            user = UserInfo.objects.create(username=username, phone=phone, age=age)
            user.save()
            return HttpResponse('提交成功!!!!')
    else:
        infos = request.POST
    return render(request, 'register.html', locals())
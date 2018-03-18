from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):

    # 查询

    # all_messages = UserMessage.objects.filter(address='上海')
    # for message in all_messages:
    #     print (message.name)

    # 插入
    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     message = request.POST.get('message', '')
    # user_message = UserMessage()
    # user_message.name = name
    # user_message.address = address
    # user_message.email =  email
    # user_message.message = message
    # user_message.save()

    #删除
    # message = UserMessage.objects.filter(address='上海')
    # message.delete()

    all_messages = UserMessage.objects.filter(address='北京')
    if  all_messages:
        message = all_messages[0]
    return render(request, 'message_form.html',{'mymessage':message})
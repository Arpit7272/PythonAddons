from django.shortcuts import render
from subprocess import run,PIPE
from . import Whats_AutoReply



# Create your views here.

def send_message(request):
    return render(request,'details.html')


def message_sent(request):
    if request.method =='POST':
            num= request.POST.get('number')
            text=request.POST.get('text')
            time=request.POST.get('time')
            dic=Whats_AutoReply.SendReply(num,text,time)


  #  out = run(sys.executable,["//home//muth//environments//Whats_AutoReply.py",num,text,time],shell= False, stdout=PIPE)
    return render(request,'reply.html',context={'dict':dic})



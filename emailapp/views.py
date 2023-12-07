from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    return render(request,"home.html")
def send(request):
    x=request.GET["fn"]
    y=request.GET["ln"]
    z=request.GET["em"]
    from_mail=settings.EMAIL_HOST_USER
    to_list= [z]
    msg="hi "+x+" "+y+" thank you for contacting to get in back few hours"
    send_mail( "kvkdpit",msg,from_mail, to_list, fail_silently=False)
    return HttpResponse("email sent sucessfully")
# Create your views here.

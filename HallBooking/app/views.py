from django.shortcuts import render,redirect
from .models import *

from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail
from django.conf import settings
from datetime import date,datetime

def login(request):

      if request.method == 'POST':
            username = request.POST['email']
            pwd = request.POST['pass']
            if username == "bhc@edu.in" and pwd == '555':
                  return render(request,'adminhm.html')
            else:
                  messages.error(request,"invalid username or password")
                  return redirect('login')
      return render(request,'login.html')

def staff_login(request):
      if request.method == "POST":
            username = request.POST['staffemail']
            pwd = request.POST['staffpass']
            try:
                  record = AddStaffs.objects.get(email = username,password = pwd)
                  if record:
                        messages.success(request,"login successfulyy")
                        return render(request,'home.html')
            except:
                  messages.error(request,"invalid username or password")
                  return redirect('login')

      return render(request,'home.html')

            

def home(request) :
  
  return render(request,'home.html')


def about(request):
  return render(request,'about.html')



def search(request):                              
      if request.method == "POST":
            Username = request.POST['name']
            Hallname = request.POST['hname']
            Date = request.POST['date']
            StartTime = request.POST['stime']
            EndTime = request.POST['etime']
          
            record = SearchHall(Username = Username,Hallname = Hallname,Date = Date,StartTime = StartTime,EndTime = EndTime)
            record.save()
            try:
                  Hallbook.objects.get(Hallname = Hallname,Date = Date)
                  # if StartTime >= StartTime and StartTime <= EndTime:
                  messages.error(request,"hall not available")
                 
            
                
            except:
                messages.error(request,"hall  avilable")
                return render(request,'hallbook.html')
                 
            return redirect('search')
      return render(request,'search.html')

def hallbook(request):
      if request.method == "POST":
            Username = request.POST['name']
            Department=request.POST['dept']
            Email = request.POST['email']
            Hallname = request.POST['hname']
            NumberofAttendees=request.POST['attendees']
            Phone = request.POST['phone']
            Date = request.POST['date']
            NameofEvent=request.POST['ename']
            StartTime = request.POST['stime']
            EndTime = request.POST['etime']
            otherRequest = request.POST['orequest']
            equipments = request.POST.getlist('equip')
           
            # print(datetime.strptime(Date,'%y-%m-%d'))
            # strdate = Date.split('-')
            # # datetime(strdate[0],strdate[1],strdate[2])
            # dt = datetime.strptime(Date,'%y/%m/%d')
            # today = date.today()
            # if Date >= today:
            records1 =Hallbook(Username=Username,Department=Department,Email= Email,NumberofAttendees=NumberofAttendees,Phone=Phone,Date=Date,NameofEvent=NameofEvent,StartTime=StartTime,EndTime=EndTime,otherRequest=otherRequest,Hallname =Hallname,Equipments = equipments)
            records1.save()
                  # email sending\
            new_line = '\n'
            subject = "HALL BOOKING"
            message = f"Hello {Username}, {new_line}Hallname:{Hallname}{new_line}NameOfEvent:{NameofEvent}{new_line}Date:{Date}{new_line}start_time:{StartTime}{new_line}end_time:{EndTime}{new_line}Your Hall Booking is Confirmed..{new_line}Thank You..!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Email]
            send_mail(subject,message,email_from,recipient_list)
            return redirect('hallbook')
            # else:
            #      messages.error(request,"please enter valid date. ")
      return render(request,'hallbook.html')
  

def adminhm(request):
  return render(request,'adminhm.html')

def viewuser(request):
      records = AddStaffs.objects.all()
      return render(request,'adviewuser.html',{'records':records})

def viewbook(request):
      records1 = Hallbook.objects.all()
      return render(request,'adviewbook.html',{'records':records1})

def adminstf(request):
      if request.method  == "POST":
            name = request.POST['name']
            email = request.POST['email']
            dept = request.POST['Department']
            pwd = request.POST['pass']
            record = AddStaffs(name = name,email=email, Department = dept,password = pwd)
            record.save()
            #email sending 
           
            return redirect('adminhm')
      return render(request,'adminstf.html')

def index(request):
      
      return render(request,'index.html')


def feedback(request):
     return render(request,'feedback.html')

def download(request,id):
     records =Hallbook.objects.get(id = id)  
     context={'record':records} 
     return render(request,'download.html',context)

def download1(request,id):
     records =Hallbook.objects.get(id=id)
     template_path ='download1.html'
     context = {'record' : records}
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename ="download.pdf"'
     template = get_template(template_path)
     html = template.render(context)
     pisa_status =pisa.CreatePDF(
       html,dest=response)
     if pisa_status.err:
          return HttpResponse('we had some errors <pre>' + html + '</pre>')
     return response
     return render(request,'download1.html',context)

def approve(request):
     records = Hallbook.objects.all()
     return render(request,'adapprove.html',{'records':records})
   
def delete_book(request,id):
     record = Hallbook.objects.get(id = id)
     record.delete()
     new_line = '\n'
     subject = "HALL BOOKING"
     message = f"Hello {record.Username}, {new_line}Your Hall Booking has been Canceled..{new_line}Thank You..!"
     email_from = settings.EMAIL_HOST_USER
     recipient_list = [record.Email]
     send_mail(subject,message,email_from,recipient_list)
     return redirect('approve')

def update_book(request,id):
     record = Hallbook.objects.get(id = id)
     if request.method == "POST":
            record.Username = request.POST['name']
            record.Department=request.POST['dept']
            record.Email = request.POST['email']
            record.Hallname = request.POST['hallname']
            record.NumberofAttendees=request.POST['attendees']
            record.Phone = request.POST['phone']
            record.Date = request.POST['date']
            record.NameofEvent=request.POST['ename']
            record.StartTime = request.POST['stime']
            record.EndTime = request.POST['etime']
            record.Equipments  = request.POST.getlist('equip')
            record.otherRequest = request.POST['orequest']
            # record =Hallbook(Username=Username,Department=Department,Email= Email,NumberofAttendees=NumberofAttendees,Phone=Phone,Date=Date,NameofEvent=NameofEvent,StartTime=StartTime,EndTime=EndTime,Equipments = equipments,otherRequest=otherRequest,Hallname =Hallname)
            record.save()
            #email
            new_line = '\n'
            subject = "HALL BOOKING"
            message = f"Hello {record.Username}, {new_line}Hallname:{record.Hallname}{new_line}NameOfEvent:{record.NameofEvent}{new_line}Date:{record.Date}{new_line}start_time:{record.StartTime}{new_line}end_time:{record.EndTime}{new_line}Your Hall Booking has been updated....{new_line}Thank You..!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [record.Email]
            send_mail(subject,message,email_from,recipient_list)
            return redirect('adviewbook')
     
          

     return render(request,'update.html',{'record':record})

def feedback1(request):
     if request.method  == "POST":
            Username = request.POST['name']
            email = request.POST['email']
            feedback = request.POST['comment']
            record = Feedback( Username = Username,Email=email, Feedback = feedback)
            record.save()
            return redirect('login')
     return render(request,'feedback.html')
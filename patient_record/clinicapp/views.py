from django.shortcuts import render , redirect,HttpResponse
from clinicapp.models import record
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponse
import csv
# for generating pdf dynamically 
from django.http import FileResponse 
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# name= admin , password= admin
# new user:
# name= sansu , password= s@nsu1234
# name= harry , password = harry@1234
# Create your views here.

#generate pdf files
def details_pdf(request):
    #create Bytestream buffer
    buf=io.BytesIO()
    # create a canvas
    c=canvas.Canvas(buf, pagesize=letter,bottomup=0)
    # create a text object
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",12)

    #lines=[" sans"]
    record_list=record.objects.all()
    lines=[]
    for rec in record_list:
        lines.append(rec.name)
        lines.append(rec.email)
        lines.append(rec.number)
        lines.append(rec.disease)
        lines.append(rec.condition)
        lines.append(rec.curr_prescribed)
        lines.append(rec.prev_prescribed)
        lines.append("")

    for line in lines:
        textob.textLine(line)

    #finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True,filename='details.pdf')



# generate csv files 
def details_csv(request):
   response=HttpResponse(content_type='text/csv')
   response['Content-Disposition']='attachment; filename=details.csv'
   # create a csv writer
   writer=csv.writer(response)
   
   
   # designate the models
   record_list=record.objects.all()
   
   # add column heading to csv file
   writer.writerow(['Patient Name','Email','phone Number','Disease','condition','current prescrived medicine','previous prescribed medicine'])
   
   for rec in record_list:
       writer.writerow([rec.name,rec.email,rec.number,rec.disease,rec.condition,rec.curr_prescribed,rec.prev_prescribed])

   
   return response
#https://s.hdnux.com/photos/37/32/44/8235288/3/rawImage.jpg



# generate textfile 
def details_text(request):
   response=HttpResponse(content_type='text/plain')
   response['Content-Disposition']='attachment; filename=details.txt'
   # designate the models
   record_list=record.objects.all()
   lines=[]
   for rec in record_list:
       lines.append(f'{rec.name}\n{rec.email}\n{rec.number}\n{rec.disease}\n{rec.curr_prescribed}\n{rec.condition}\n{rec.prev_prescribed}\n\n\n\n\n')

   response.writelines(lines) #write to textfiles
   return response


def home(request):
    return render(request,'homepage.html')

def show_record(request):
    record_list=record.objects.all()
    print("User is", request.user)
    return render(request, 'show_record.html',{'record_list' : record_list})

def details(request,id):
    record_list=record.objects.get(pk=id)

    return render(request, 'record.html',{'record_list' : record_list})

def search(request):
     if request.method == "POST":
        query_name = request.POST.get('search',False)
         
        results = record.objects.filter(name__contains=query_name)
        return render(request, 'search.html', {'results':results,'query_name':query_name})

     return render(request, 'search.html')

def login_user(request):
     
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return render(request, 'home.html',{'user':user})
            
        else:
            messages.info(request, f'account does not exist plz sign in again !!! if dont have account create first')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

     

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form': form, 'title':'reqister here'})

def add_details(request): 
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        disease=request.POST.get('disease')
        condition=request.POST.get('condition')
        curr_pres=request.POST.get('curr_prescribed')
        prev_pres=request.POST.get('prev_prescribed')
        upl_img=request.FILES.get('upl_img')
        records=record(name=name,email=email,number=number,disease=disease,condition=condition, curr_prescribed=curr_pres, prev_prescribed=prev_pres,venue_image=upl_img)   
        records.save()
        messages.success(request,'Your Health Details has been submitted !! successfully')
        return render(request,'home.html')
     
    return render(request,'patient/add_details.html')
    #return render(request,'patient/record.html',{records:'records'})



def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def hosinfo(request):
    return render(request,'bio.html')

def edit(request,id):
    record_user=record.objects.get(pk=id)
     
     
    
    return render(request,'patient/edit.html',{'record_user':record_user})


def detail_text(request,id):
    response=HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment; filename=details.txt'
    # designate the models
    record_list=record.objects.get(pk=id)
    lines=[]
    lines.append(f'{record_list.name}\n{record_list.email}\n{record_list.number}\n{record_list.disease}\n{record_list.condition}\n{record_list.prev_prescribed}\n{record_list.curr_prescribed}\n')
    #for rec in record_list:
    #lines.append(f'{rec.name}\n{rec.email}\n{rec.number}\n{rec.disease}\n{rec.curr_prescribed}\n{rec.condition}\n{rec.prev_prescribed}\n\n\n\n\n')

    response.writelines(lines) #write to textfiles
    return response

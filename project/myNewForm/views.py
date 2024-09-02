from django.shortcuts import render
from myNewForm.forms import RegistrationForm,LoginForm, queryForm
from .models import *
# Create your views here.

def home(request):
    form = RegistrationForm()
    if request.method=='POST':
        data = RegistrationForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['stu_name']
            email=data.cleaned_data['stu_email']
            city=data.cleaned_data['stu_city']
            contact=data.cleaned_data['stu_mobile']
            password = data.cleaned_data['stu_password']
            print(name,email,city,contact,password)
            data.save()
            msg="Registration Successfully"
            return render(request,'home.html',{'form':form,'msg':msg})
    else:
        return render(request,'home.html',{'form':form})
    
def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['stu_email']
            password = data.cleaned_data['stu_password']
            # print(email,password)
            user = StudentModel.objects.filter(stu_email=email)
            
            if user:
                user = StudentModel.objects.get(stu_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.stu_name
                    email = user.stu_email
                    contact = user.stu_mobile
                    city = user.stu_city
                    password = user.stu_password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city,
                        'password':password
                    }
                    initial_data={
                        'stu_name':name,
                        'stu_email':email
                    }
                    form1=queryForm(initial=initial_data)
                    return render(request,'dashboard.html',{'data':data,'query':form1})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    
# def query(request):
#     form= queryForm()
#     if request.method=='POST':
#         query_data=queryForm(request.POST)
#         if query_data.is_valid():
#             name=query_data.cleaned_data['stu_name']
#             email=query_data.cleaned_data['stu_email']
#             query=query_data.cleaned_data['stu_query']
#             print(name,email,query)
#             query_data.save()

def query(request):
    # return HttpResponse("hi.............")
    form = queryForm()
    if request.method=="POST":
        query_data = queryForm(request.POST) 
        # print(query_data)
        if query_data.is_valid():
            name =  query_data.cleaned_data['stu_name']
            email = query_data.cleaned_data['stu_email']
            query = query_data.cleaned_data['stu_query']
            # print(email,name,query)
            query_data.save()
            user = StudentModel.objects.get(stu_email=email)
            
            name = user.stu_name
            email = user.stu_email
            contact = user.stu_mobile
            city = user.stu_city
            password = user.stu_password
            data = {
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password
                }
            initial_data = {
                                'stu_name': name,
                                'stu_email': email
                            } 
            form1=queryForm(initial=initial_data)
            data1 = StudentQuery.objects.filter(stu_email=email)
                
            return render(request,'dashboard.html',{'data':data,'query':form1,'data1':data1})
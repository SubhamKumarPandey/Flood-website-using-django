from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Aboutngo, Contact, Data1, Data2, Data3, Data4, Donation, Issue, Location, Reliefcamp, Rivers
from django.contrib import messages
from django.contrib.auth.models import User, auth
import wolframalpha
import wikipedia
import webbrowser
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("THIS IS HOMEPAGE")
def about(request):
    #return HttpResponse("THIS IS About")

    ngos = Aboutngo.objects.all()

    return render(request, 'about.html',{'ngos':ngos})
def home1(request):
    #return HttpResponse("THIS IS home")
    weather_data = None;
    if 'city'in request.GET:

        city = request.GET.get('city')
        html_content = get_content(city)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        weather_data = dict()
        weather_data['region'] = soup.find('div',attrs={'id':'wob_loc'}).text
        weather_data ['daytime'] = soup.find('div',attrs={'id':'wob_dts'}).text
        weather_data['status'] = soup.find('span',attrs={'id':'wob_dc'}).text
        weather_data['temp'] = soup.find('span',attrs={'id':'wob_tm'}).text
    return render(request, 'home1.html',{'weather': weather_data })

def get_content(city):
            import requests
            USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
            LANGUAGE = "en-US,en;q=0.5"
            session = requests.Session()
            session.headers['User-Agent'] = USER_AGENT
            session.headers['Accept-Language'] = LANGUAGE
            session.headers['Content-Language'] = LANGUAGE
            city = city.replace(' ','+')
            html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
            return html_content

def weather(request):
     #return HttpResponse("THIS IS weather")
    weather_data = None;
    if 'city'in request.GET:

        city = request.GET.get('city')
        html_content = get_content(city)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        weather_data = dict()
        weather_data['region'] = soup.find('div',attrs={'id':'wob_loc'}).text
        weather_data ['daytime'] = soup.find('div',attrs={'id':'wob_dts'}).text
        weather_data['status'] = soup.find('span',attrs={'id':'wob_dc'}).text
        weather_data['temp'] = soup.find('span',attrs={'id':'wob_tm'}).text

    return render(request,'weather.html',{'weather': weather_data })


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    #return HttpResponse("THIS IS Contact")
    return render(request, 'contact.html')
def data(request):
    #return HttpResponse("THIS IS data")
    return render(request, 'data.html')

def reliefcamp(request):
    #return HttpResponse("THIS IS relief")
    camps = Reliefcamp.objects.all()
    return render(request, 'reliefcamp.html',{'camps':camps})

def rivers(request):
    #return HttpResponse("THIS IS relief")
    rivers = Rivers.objects.all()
    return render(request, 'rivers.html',{'rivers':rivers})


def help(request):
    query = request.GET.get('query')


    try:
        client = wolframalpha.Client("UHAULU-9VQ5JEWT4J")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'help.html', {'ans': ans, 'query': query})


    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'help.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'help.html', {'ans': ans, 'query': query})



def data1(request):
    #return HttpResponse("THIS Is help")
    data1 = Data1.objects.all()
    return render(request, 'data1.html',{'data1':data1})



def data2(request):
        #return HttpResponse("THIS Is help")
     data2 = Data2.objects.all()
     return render(request, 'data2.html',{'data2':data2})


def data3(request):
    #return HttpResponse("THIS Is help")

     data3 = Data3.objects.all()
     return render(request, 'data3.html',{'data3':data3})


def data4(request):
    #return HttpResponse("THIS Is help")

     data4 = Data4.objects.all()
     return render(request, 'data4.html',{'data4':data4})


def register(request):
    #return HttpResponse("THIS IS Registraion form")

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
                messages.info(request,'Registration Successfull')

        else:
            messages.info(request,'Password Does not Match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')



def login(request):
    #return HttpResponse("THIS IS login")
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    #return HttpResponse("THIS IS Logout")
    auth.logout(request)
    return redirect('/')


def issue(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        issue = Issue(name=name, phone=phone, desc=desc, date = datetime.today())
        issue.save()
        messages.success(request, 'We Record your issue!')
    return render(request, 'issue.html')


def location(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc1 = request.POST.get('desc1')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        location = Location(name=name, desc1=desc1, phone=phone, desc=desc, date = datetime.today())
        location.save()
        messages.success(request, 'Your request has been Recorded! Our NDRF team will be their soon!')

    return render(request, 'location.html')

def donation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        exampleFormControlSelect1 = request.POST.get('exampleFormControlSelect1')
        exampleFormControlFile1 = request.POST.get('exampleFormControlFile1')
        donation = Donation(name=name, exampleFormControlFile1=exampleFormControlFile1, phone=phone, exampleFormControlSelect1=exampleFormControlSelect1, date = datetime.today())
        donation.save()
        messages.success(request, 'Thank You !')

    return render(request, 'donation.html')
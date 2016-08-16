from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import loader #To load an html template using loader.get_template("name.html")
from dateutil import parser
from .forms import DateForm
from django.contrib import messages


# Create your views here.
def index(request,string):
    template = loader.get_template("index.html")
    form = DateForm()
    today = parser.parse(string)
    today.replace(hour=0, minute=0, second=0)
    if(request.GET.get('check')):
        context ={
            'title':string,
        }
    else:
        context = {
                'title':string, # pass context to HTML page i.e passing title here
                'date':today,
                'form':form,
            }
        print(today)
    return HttpResponse(template.render(context,request)) # Rendering the template
    
def dateInput(request):
    template = loader.get_template("index.html")
    if request.method == 'POST':
        form = DateForm(request.POST)
        context={'form': form}
        if form.is_valid():
            inputDate = form.cleaned_data['check_date']
            return HttpResponse(loader.get_template("index.html").render({'date':inputDate,'form':form},request))
        else:
            return HttpResponse(template.render(context,request)) # HttpResponseRedirect(request.META.get('HTTP_REFERER')) For same URL redirect
    else:
        form = DateForm()
        context={'form': form}
        return HttpResponse(template.render(context,request)) # Rendering the template
            
    
   
    
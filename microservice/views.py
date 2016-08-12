from django.http import HttpResponse
import datetime
from django.template import loader #To load an html template using loader.get_template("name.html")
from django.utils.dateparse import parse_date 
from dateutil import parser
from .forms import DateForm


# Create your views here.
def index(request,string):
    template = loader.get_template("index.html")
    today = parser.parse(string)
    if(request.GET.get('check')):
        context ={
            'title':string,
        }
        print("ghh")
    else:
        context = {
                'title':string, # pass context to HTML page i.e passing title here
                'date':today,
            }
        print(today)
    return HttpResponse(template.render(context,request)) # Rendering the template
    
def dateInput(request):
    template = loader.get_template("form.html")
    
    if request.method == 'POST':
        form = DateForm(request.POST)
            
    else:
        form = DateForm()
        
    context={'form': form}
    return HttpResponse(template.render(context,request)) # Rendering the template
            
    
   
    
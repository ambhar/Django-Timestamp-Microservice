from django.http import HttpResponse
from django.template import loader #To load an html template using loader.get_template("name.html")

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {
            'title':"Timestamp Microservice", # pass context to HTML page i.e passing title here
        }
    return HttpResponse(template.render(context,request)) # Rendering the template
from django.shortcuts import render
from  . import models
from . import  forms
from . import my_func
from django.http import response

# Create your views here.
def index(request):
    return render(request,'index.html')

def film_list(request):
    films= models.Film.objects.all()
    return render(request,'list_film.html', {'films':films})
def filmId(request):
    if request.method=='GET':
        var =request.GET['id']
    elif request.method=='POST':
        text_f=request.POST['feedback']
        rat=my_func.model_learn(text_f)
        feedback=models.Feedback(name=request.POST['name'],
                                 film_id=models.Film.objects.get(id=request.POST['film_id']),
                                 feedback=text_f,
                                 positiv=rat.positive,
                                 rating=rat.rating)
        feedback.save()
        var = feedback.film_id.id
    form_for_feedback = forms.Feedback

    fl=models.Film.objects.get(id=var)
    list_feedback = models.Feedback.objects.filter(film_id=fl)
    cet = {'list_feedback':list_feedback,
        'form_for_feedback': form_for_feedback(initial={'film_id': var}),
           'film': models.Film.objects.get(id=var),


           }
    return render(request,'film.html',cet)





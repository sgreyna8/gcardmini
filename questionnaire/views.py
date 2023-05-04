from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Survey

def survey_form(request):

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        print(form.data)
        
        if form.is_valid():
            survey = form.save()
            return redirect('thank_you')
        
    else:
        form = SurveyForm()
        
    return render(request, 'index.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def survey_results(request):
    surveys = Survey.objects.all()
    return render(request, 'survey_results.html', {'surveys': surveys})
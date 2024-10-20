from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from .forms import ContactForm
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    paginator = Paginator(latest_question_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'polls/index.html',{'page_obj':page_obj})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return redirect('polls:thanks')
    else:
        form = ContactForm()
    return render(request, 'polls/contact.html', {'form': form})



# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# # Create your views here.

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     context={"latest_question_list":latest_question_list}
#     return render(request,'polls/index.html',context)
# def home(request):
#     return HttpResponse('this is home page')

# def about(request):
#     return HttpResponse('this is about page')

# def contact(request):
#     return HttpResponse('this is contact page')

# class IndexView(views):
#     def get(self, request):
        # return HttpResponse('<h1>hello world, you are at the index</h1>')
# def detail(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})


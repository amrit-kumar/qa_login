from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User


def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'login/index.html', context)
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return render_to_response(
                'registration/success.html',
                {'user': request.user}
            )
         # return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )
@login_required
def add_question(request):

        if request.method == 'POST':
            question = request.POST.get('question')
            if question and question !='':
                username = request.user
                form = Question(question=question, username=request.user)

                form.save()
                latest_question_list = Question.objects.all()
                context = {'form': form, 'latest_question_list': latest_question_list}
                return render(request, 'login/index.html', context)
            else:
                return render(request, 'login/error.html')
        else:
            form = Question()
            return render(request, 'login/index.html')

def detail(request,question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'login/detail.html', {'question': question})

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    if request.POST:
        if '_upvote' in request.POST:
            selected_choice = question.answer_set.get(pk=request.POST['answer'])
            selected_choice.upvotes += 1
            selected_choice.save()
            return  render(request, 'login/results.html',{'question':question})

            #return HttpResponseRedirect(reverse('login:results', args=(question.id,)))

        elif '_downvote' in request.POST:
            selected_choice1 = question.answer_set.get(pk=request.POST['answer'])
            selected_choice1.downvotes += 1
            selected_choice1.save()
            return  render(request, 'login/results.html',{'question':question})

            #return HttpResponseRedirect(reverse('login:results', args=(question.id,)))
    else:

        return HttpResponse("you have no access")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'login/results.html', {'question': question})

def search(request):
    if request.method == 'POST':
        text=(request.POST['search'])
        print "hiiiiiiiiii", text
        search=Question.objects.filter(question__icontains=text)
        print  search
        # search=Question.objects.filter(Question(content__icontains=text))

        if search:
             # return HttpResponse("in the if loop")
             return render_to_response("login/index.html", {'object_list': search})
        else:
            return HttpResponse("in else loop")
        #     msg="Requested post not found"
        #     return render_to_response("index.html", {'msg': msg}, context_instance=RequestContext(request))

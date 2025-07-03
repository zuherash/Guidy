from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Question, Answer
from .forms import QuestionForm


def index(request):
    questions = Question.objects.select_related("job_role").all()
    return render(request, "interviews/index.html", {"questions": questions})


@login_required
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            Answer.objects.create(
                question=question,
                author=request.user,
                text=form.cleaned_data["answer_text"],
            )
            return redirect("index")
    else:
        form = QuestionForm()
    return render(request, "interviews/create_question.html", {"form": form})

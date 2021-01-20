from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, Devtool
from .forms import IdeaForm, DevtoolForm



def idea_list(request):
    ideas = Idea.objects.all()
    ctx = {
        "ideas": ideas
    }
    return render(request, "page/idea_list.html", ctx)


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    ctx = {
        "idea": idea
    }
    return render(request, "page/idea_detail.html", ctx)


def idea_create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("page:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm()
        ctx = {
            "form": form
        }
        return render(request, "page/idea_create.html", ctx)



def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":

        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect("page:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {
            "form": form
        }
        return render(request, "page/idea_update.html", ctx)


def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        idea.delete()
        return redirect("page:idea_list")
    else:
        return redirect("page:idea_detail", pk=idea.pk)
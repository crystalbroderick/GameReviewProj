from django.shortcuts import render, get_object_or_404
from .models import Game, Review
from .forms import GameForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'gamereviewapp/index.html')

def getGame(request):
    game_list=Game.objects.all()
    return render(request, 'gamereviewapp/game.html' ,{'game_list' : game_list})

def gamedetail(request, id):
    vg=get_object_or_404(Game, pk=id)
    reviewcount=Review.objects.filter(game=id).count()
    reviews=Review.objects.filter(game=id)
    context={
        'vg' : vg,
        'reviews' : reviews,
        'reviewcount' : reviewcount
    }
    return render(request, 'gamereviewapp/gamedetail.html', context=context)

@login_required
def newGame(request):
     form=GameForm
     if request.method=='POST':
          form=GameForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=GameForm()
     else:
          form=GameForm()
     return render(request, 'gamereviewapp/newgame.html', {'form': form})
@login_required
def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'gamereviewapp/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'gamereviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'gamereviewapp/logoutmessage.html')


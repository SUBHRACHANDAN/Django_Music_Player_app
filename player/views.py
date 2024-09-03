from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm

def music_list(request):
    music_files = Music.objects.all()
    return render(request, 'player/music_list.html', {'music_files': music_files})

def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'player/upload_music.html', {'form': form})

import sys

from django.shortcuts import render, redirect
from gtts import gTTS
from .forms import MusicForm
from .models import Music
import os
from django.contrib import messages

text = """Thousand Faces is a Alternative Rock band based in srinagar kashmir 'UT'. Playing is passion for us. We try 
to give the  best of which we know a little. THE BAND THOUSAND Faces HAS A BASIC GENRE ROCK BUT WE always WANT TO ADD 
Something NEW TO THE GENRE LIKE Alternate ROCK, SUFI ROCK, CLASSICAL ROCK, PUNK ROCK, HARD ROCK. Our motto is to 
provide music with that touches the heart of a listener. We have dreamt to enhance the propinquity of the people 
towards music so that they will feel quite propitious to listen us. We do have our sentiments living in our hearts 
with the positive spirit within our souls. There is a saying, "There is a time to let things happen and there is a 
time to make things happen". Things happened as the usual course till date. Now we will make things happen by our 
dedication and emotions so that, the time will come when this description will not be consulted instead the 
listeners, the fans and overall the public will describe us in their own good words. We always try to make ourselves 
better and better to fulfill your expectations. Thanks for supporting us. Band Members:- Obaid Fayaz lead guitarist, 
composer and lyricist. Momin Mushatq vocalist and rhythm guitarist. Romaan Naaz drummer and vocalist. """


def text_to_speech():
    language = 'en'
    voice = gTTS(text=text, lang=language, slow=False)
    voice.save("TF_about.mp3")
    os.system("start TF_about.mp3")


def index(request):
    return render(request, "index.html", {'title': 'Home'})


def members(request):
    form = MusicForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            file_name = str(form.cleaned_data['Mp3'])
            if not file_name.endswith('.mp3'):
                messages.warning(request, 'Please Upload mp3 file only!!!')
                return redirect('members')
            if file_name.endswith('.mp3'):
                form.save()
                messages.success(request, f'File <{file_name}> Uploaded Successfully, check our fans Songs')
                return redirect('downloads')

    else:
        form = MusicForm()
    context = {
        'title': 'Members',
        'heading': 'Members',
        'form': form,
    }
    return render(request, "members.html", context)


def download(request):
    songs = Music.objects.all()
    context = {
        'title': 'Downloads',
        'heading': 'Downloads',
        'songs': songs
    }
    return render(request, 'downloads.html', context)


def delete(request, pk):
    if request.method == 'POST':
        songs = Music.objects.get(pk=pk)
        songs.delete()
    return redirect('downloads')


def videos(request):
    context = {
        'title': 'Videos',
        'heading': 'Videos',
    }
    return render(request, "videos.html", context)


def about(request):
    context = {
        'title': 'About',
        'heading': 'About',
        'text': text_to_speech,
    }
    return render(request, "about.html", context)
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import FaveSongsModel
from .forms import SongEntry


def favesongs_home(request):
    return render(request, 'FaveSongs/favesongs_home.html')

# Story 2. Create model and entry form/page
def favesongs_create(request):
    # get the SongEntry form
    form = SongEntry(data=request.POST or None)
    # check if the request is post
    if request.method == 'POST':
        # checks to see if the form is valid before it can save
        if form.is_valid():
            form.save()
            # returns user to the homepage
            return redirect('favesongs_thelist')
    # saves content as a dictionary
    content = {'form': form}
    # adds the content to the page
    return render(request, 'FaveSongs/favesongs_create.html', content)

# story 3. Create a list of all the entries in the dB
def favesongs_thelist(request):
    songs = FaveSongsModel.objects.all()
    content = {'songs': songs}
    return render(request, 'FaveSongs/favesongs_thelist.html', content)

# story 4. Create a details page that links to the song list
def favesongs_details(request, pk):
    details = get_object_or_404(FaveSongsModel, pk=pk)
    content = {'details': details}
    return render(request, 'FaveSongs/favesongs_details.html', content)

def favesongs_edit(request, pk):
    entry = get_object_or_404(FaveSongsModel, pk=pk)
    form = SongEntry(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('favesongs_thelist')
    return render(request, 'FaveSongs/favesongs_edit.html', {'form': form, 'entry': entry})

def favesongs_delete(request, pk):
    entry = get_object_or_404(FaveSongsModel, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('favesongs_thelist')
    content = {'entry': entry}
    return render(request, 'FaveSongs/favesongs_delete.html', content)

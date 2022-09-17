from django.shortcuts import render, redirect
from user.models import *
from core.filters import AlbumFilter, ShowFilter, UserPayrollFilter
from .forms import *
from django.http import JsonResponse, HttpResponse
from .models import *


def login(request):
    form = ManagerLoginForm()

    if request.POST:

        username = request.POST['username']
        password = request.POST['password']

        validate = ManagerAuth.objects.filter(username=username, password=password)
        if validate.count() == 1:

            return JsonResponse({'valid': 'True', 'manager_id': validate[0].id})
        else:
            return JsonResponse({'valid': 'False'})

    context = {'form': form}

    return render(request, 'ManagerAccounts/login.html', context)


def dashboard(request):
    artists = UserDetail.objects.all()
    albums = UserAlbum.objects.all()
    artist_details = UserDetail.objects.all().order_by('-id')[:4]
    studios = Studio.objects.all()

    context = {'artists_count': artists.count(), 'albums': albums.count(), 'studios': studios.count(),
               'artists': artist_details}

    return render(request, 'ManagerAccounts/index.html', context)


def artists(request):
    artists = UserDetail.objects.all()

    form = AddArtistForm()

    context = {'artists': artists, 'form': form}

    return render(request, 'ManagerAccounts/artists.html', context)


def new_artist(request):
    if request.POST:

        form = AddArtistForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            # RESPONSE WHEN DATA IS SAVED

            return JsonResponse({"saved": "Yes"})
        else:
            # RESPONSE WHEN AN ERROR OCCURS

            return JsonResponse({"saved": "No"})


def update_artist(request, pk):
    artist = UserDetail.objects.get(id=pk)
    form = AddArtistForm(instance=artist)

    if request.method == "POST" or request.method == "FILES":

        myform = AddArtistForm(request.POST, request.FILES, instance=artist)

        if myform.is_valid():
            myform.save()

            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})

    context = {'form': form, 'pk': pk}

    return render(request, 'ManagerAccounts/update-profile.html', context)


def delete_artist(request):
    pk = request.POST['pk']
    artist = UserDetail.objects.get(id=pk)
    if request.POST:
        artist.delete()
        if artist:

            return JsonResponse({"deleted": "Yes"})

        else:
            return JsonResponse({"deleted": "No"})
    else:

        return JsonResponse({"post": False})


def studios(request):
    my_studios = Studio.objects.all()

    form = AddStudioForm(request.POST)

    context = {'studios': my_studios, 'form': form}

    return render(request, 'ManagerAccounts/studios.html', context)


def new_studio(request):
    if request.POST:
        form = AddStudioForm(request.POST)
        if form.is_valid():

            form.save()

            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})


def update_studio(request, pk):
    studio = Studio.objects.get(id=pk)
    form = AddStudioForm(instance=studio)

    if request.POST:
        my_form = AddStudioForm(request.POST, instance=studio)
        if my_form.is_valid():
            my_form.save()

            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})

    context = {'form': form, 'pk': pk}

    return render(request, 'ManagerAccounts/update-studio.html', context)


def delete_studio(request):
    pk = request.POST['pk']
    studio = Studio.objects.get(id=pk)
    if request.POST:
        studio.delete()
        if studio:

            return JsonResponse({"deleted": "Yes"})

        else:
            return JsonResponse({"deleted": "No"})
    else:

        return JsonResponse({"post": False})


def studio_sessions(request):
    form = AddStudioSessionForm()
    sessions = StudioSession.objects.filter(status='Pending')

    context = {'form': form, 'sessions': sessions}

    return render(request, 'ManagerAccounts/studio-sessions.html', context)


def add_studio_sessions(request):
    if request.POST:
        my_form = AddStudioSessionForm(request.POST or None)

        if my_form.is_valid():
            my_form.save()
            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})


def albums(request):
    form = AddAlbumForm()
    # GET ALL ALBUMS
    all_albums = UserAlbum.objects.all().order_by('artist_id')
    # SEARCH FOR THE SPECIFIED ALBUM
    filter = AlbumFilter(request.GET, queryset=all_albums)

    all_albums = filter.qs

    context = {'form': form, 'filter': filter, 'albums': all_albums}

    return render(request, 'ManagerAccounts/albums.html', context)


# view artist personal information
def view_artist(request, pk):
    artist = UserDetail.objects.get(id=pk)

    try:
        artist_payroll = UserPayroll.objects.filter(artist_id=pk).latest('id')
    # when the id of a payroll record is not available
    except UserPayroll.DoesNotExist:
        artist_payroll = 0
    # fetch the album details for the selected artist
    try:

        artist_albums = UserAlbum.objects.filter(artist_id=pk)
        no_of_albums = artist_albums.count()
        certified_gold = artist_albums.filter(certification='GOLD').count()
        certified_platinum = artist_albums.filter(certification='PLATINUM').count()
        certified_diamond = artist_albums.filter(certification='DIAMOND').count()

    except UserAlbum.DoesNotExist():
        no_of_albums = 'N/A'
        certified_gold = 0
        certified_platinum = 0
        certified_diamond = 0

    context = {'artist': artist, 'payroll': artist_payroll, 'no_of_albums': no_of_albums,
               'platinum': certified_platinum, 'gold': certified_gold,
               'diamond': certified_diamond}

    return render(request, 'ManagerAccounts/view-profile.html', context)


# add album
def add_album(request):
    if request.POST:
        new_album = AddAlbumForm(request.POST, request.FILES or None)

        if new_album.is_valid():
            new_album.save()
            return JsonResponse({"saved": "Yes"})

        else:
            return JsonResponse({"saved": "No"})


def update_album(request, pk):
    album = UserAlbum.objects.get(id=pk)
    form = AddAlbumForm(instance=album)

    if request.POST:
        my_form = AddAlbumForm(request.POST, instance=album)
        if my_form.is_valid():
            my_form.save()

            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})

    context = {'form': form, 'pk': pk}

    return render(request, 'ManagerAccounts/update-album.html', context)


# delete album

def delete_album(request):
    pk = request.POST["pk"]
    try:
        album = UserAlbum.objects.get(id=pk)
        album.delete()
        return JsonResponse({"deleted": "Yes"})

    except UserAlbum.DoesNotExist:

        return JsonResponse({"deleted": "No"})


def show_tour(request):
    form = AddShowTourForm()
    shows = ShowsTours.objects.all()
    my_filter = ShowFilter(request.GET, queryset=shows)

    all_shows = my_filter.qs

    context = {'form': form, 'shows': all_shows, 'my_filter': my_filter}

    return render(request, 'ManagerAccounts/shows-tours.html', context)


def add_show_tour(request):
    if request.POST:
        new_show = AddShowTourForm(request.POST or None)

        if new_show.is_valid():
            user = UserDetail.objects.get(id=request.POST["artist_id"])
            notification = MyNotification.objects.create(title='New Show', to=int(user.id), message='ok',
                                                         read='No')
            notification.save()
            new_show.save()
            return JsonResponse({"saved": "Yes"})

        else:
            return JsonResponse({"saved": "No"})


def update_show(request, pk):
    show = ShowsTours.objects.get(id=pk)
    form = AddShowTourForm(instance=show)

    if request.POST:
        my_form = AddShowTourForm(request.POST, instance=show)
        if my_form.is_valid():
            my_form.save()

            return JsonResponse({"saved": "Yes"})
        else:
            return JsonResponse({"saved": "No"})

    context = {'form': form, 'pk': pk}

    return render(request, 'ManagerAccounts/update-shows-tours.html', context)


# payroll module
def payroll(request):
    form = AddPayrollForm()
    my_payroll = UserPayroll.objects.all()
    my_filter = UserPayrollFilter(request.GET, queryset=my_payroll)

    payrolls = my_filter.qs

    context = {'payrolls': payrolls, 'form': form, 'filter': my_filter}
    return render(request, 'ManagerAccounts/payroll.html', context)


def add_payroll(request):
    form = AddPayrollForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/manager/payroll')
    else:
        return HttpResponse("Form not Valid")


def update_payroll(request, pk):
    my_payroll = UserPayroll.objects.get(id=pk)
    form = AddPayrollForm(instance=my_payroll)

    if request.POST:
        my_form = AddPayrollForm(request.POST, instance=my_payroll)
        if my_form.is_valid():
            my_form.save()
            return redirect('/manager/payroll')
        else:
            return HttpResponse("Update Failed")

    context = {
        'form': form
    }
    return render(request, 'ManagerAccounts/update-payroll.html', context)


def logout(request):
    return render(request, 'ManagerAccounts/logout-manager.html')


def update_session(request, pk):
    session = StudioSession.objects.get(id=pk)
    form = AddStudioSessionForm(instance=session)
    if request.POST:
        my_form = AddStudioSessionForm(request.POST, instance=session)

        if my_form.is_valid():
            my_form.save()
            return redirect('/manager/studiosessions')
        else:
            return HttpResponse("Update Failed")

    context = {
        'form': form
    }

    return render(request, 'ManagerAccounts/update-session.html', context)


def delete_session(request, pk):
    if request.POST:

        try:
            session = StudioSession.objects.get(id=pk)
            session.delete()

            return redirect('/manager/studiosessions')

        except UserAlbum.DoesNotExist:

            return HttpResponse("Deleting Failed")

    return render(request, 'ManagerAccounts/delete-session.html')


def view_album(request, pk):
    try:
        album = UserAlbum.objects.get(id=pk)

        context = {'album': album}

        return render(request, 'ManagerAccounts/view-album.html', context)

    except UserAlbum.DoesNotExist():

        return HttpResponse("Album Does Not Exist")


def delete_payroll(request, pk):
    if request.POST:

        try:
            my_payroll = UserPayroll.objects.get(id=pk)
            my_payroll.delete()

            return redirect('/manager/payroll')

        except UserPayroll.DoesNotExist:

            return HttpResponse("Deleting Failed")

    return render(request, 'ManagerAccounts/delete-payroll.html')

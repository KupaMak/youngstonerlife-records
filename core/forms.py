from itertools import filterfalse
from django import forms
from .models import *


class ManagerLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ), required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ), required=False)

    class Meta:
        model = ManagerAuth


class AddArtistForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ), required=False, label=False)
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ), required=False, label=False)

    national_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "National ID",
                "class": "form-control"
            }
        ), required=False, label=False)

    gender = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Gender",
                "class": "form-control"
            }
        ), choices=UserDetail.GENDER, required=False, label=False)
    department = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Department",
                "class": "form-control"
            }
        ), choices=UserDetail.DEPARTMENT, required=False, label=False)

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "class": "form-control"
            }
        ), required=False, label=False)
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ), required=False, label=False)
    date_of_birth = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date Of Birth",
                "class": "form-control",
                "type": "date"
            }
        ), required=False, label=False)
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ), required=False, label=False)

    account_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Account Number",
                "class": "form-control"
            }
        ), required=False, label=False)
    stage_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Stage Name",
                "class": "form-control"
            }
        ), required=False, label=False)

    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'address', 'national_id',
                  'date_of_birth', 'department', 'stage_name', 'account_number', 'picture']


class AddStudioForm(forms.ModelForm):
    studio_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Studio Name",
                "class": "form-control"
            }
        ), required=False)
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Studio Location",
                "class": "form-control"
            }
        ), required=False)

    main_producer = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Studio",
                "class": "form-control"
            }
        ), required=False, queryset=UserDetail.objects.filter(department='Producer'), label=False)

    class Meta:
        model = Studio
        fields = '__all__'


class AddStudioSessionForm(forms.ModelForm):
    booked_date = forms.DateField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "Enter Booked Date",
                "class": "form-control",
                "type": "date",
            }
        ), required=False, label=False)

    studio = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Studio",
                "class": "form-control"
            }
        ), required=False, queryset=Studio.objects.all(), label=False)

    artist = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Artist",
                "class": "form-control"
            }
        ), required=False, queryset=UserDetail.objects.filter(department='Artist'), label=False)

    producer = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Producer",
                "class": "form-control"
            }
        ), required=False, queryset=UserDetail.objects.filter(department='Producer'), label=False)

    status = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Status",
                "class": "form-control"
            }
        ), required=False, label=False, choices=StudioSession.STATUS)

    class Meta:
        model = StudioSession
        fields = '__all__'
        exclude = ['date']


class AddAlbumForm(forms.ModelForm):
    album = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Album Name",
                "class": "form-control"
            }
        ), required=False)
    no_of_tracks = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Number of Tracks",
                "class": "form-control",
                "type": "text",
            }
        ), required=False)
    first_week_sales = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "First Week Sales",
                "class": "form-control",
                "type": "text",
            }
        ), required=False)
    date_released = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date Released",
                "class": "form-control",
                "type": "date"
            }
        ), required=False)
    artist_id = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Status",
                "class": "form-control"
            }
        ), required=False, label=False, queryset=UserDetail.objects.all())
    certification = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Certification",
                "class": "form-control"
            }
        ), required=False, label=False, choices=UserAlbum.CERTIFICATION)

    class Meta:
        model = UserAlbum
        fields = '__all__'


class AddShowTourForm(forms.ModelForm):
    artist_id = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Status",
                "class": "form-control"
            }
        ), required=False, label=False, queryset=UserDetail.objects.all())

    show_amount = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter Show Amount",
                "class": "form-control",
                "type": "text",
            }
        ), required=False)

    disk_jokey = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Disk Jokey",
                "class": "form-control",
                "type": "text",
            }
        ), required=False, label=False, queryset=UserDetail.objects.filter(department='Disk Jokey'))

    start_date = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": " Start Date ",
                "class": "form-control",
                "type": "date"
            }
        ), required=False)

    end_date = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "End Date",
                "class": "form-control",
                "type": "date"
            }
        ), required=False)

    venue = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Venue",
                "class": "form-control"
            }
        ), required=False)

    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Country",
                "class": "form-control"
            }
        ), required=False)

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter City",
                "class": "form-control"
            }
        ), required=False)

    duration = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Show Duration",
                "class": "form-control"
            }
        ), required=False)

    class Meta:
        model = ShowsTours
        fields = '__all__'


class AddPayrollForm(forms.ModelForm):
    artist_id = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Artist",
                "class": "form-control",
                "type": "text",
            }
        ), required=False, label=False, queryset=UserDetail.objects.all())
    general_salary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter General Salary",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    show_tour_income = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Show/ Tour Income",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    platforms_income = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Platforms Income",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    insurance = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Insurance Expenses",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    transport = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Transport Expenses",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    accommodation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Accommodation Expenses",
                "class": "form-control",
                "type":"number"
            }
        ), required=False)
    month = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Enter Transport Expenses",
                "class": "form-control"
            }
        ), required=False, choices=UserPayroll.MONTH)

    class Meta:
        fields = '__all__'
        exclude = ['date_paid']
        model = UserPayroll

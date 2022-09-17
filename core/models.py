from django.db import models


class ManagerAuth(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username





class UserDetail(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    DEPARTMENT = (

        ('Artist', 'Artist'),
        ('Producer', 'Producer'),
        ('Chief Executive Officer', 'Chief Executive Officer'),
        ('Manager', 'Manager'),
        ('Disk Jokey', 'Disk Jokey')

    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=50, default='0000000')
    gender = models.CharField(max_length=50, choices=GENDER)
    department = models.CharField(max_length=30, choices=DEPARTMENT, default='Artist')
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    date_employed = models.DateField(auto_now_add=True)
    date_of_birth = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    account_number = models.CharField(max_length=50)
    stage_name = models.CharField(max_length=40, default='N/A')
    picture = models.ImageField(null=True, blank=True, upload_to='profile')

    def __str__(self):
        return self.stage_name


class UserAlbum(models.Model):
    CERTIFICATION = (
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
        ('Diamond', 'Diamond'),
        ('N/A', 'N/A')

    )

    album = models.CharField(max_length=40, default='N/A')
    artist_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    no_of_tracks = models.CharField(max_length=50)
    first_week_sales = models.CharField(max_length=40, default='N/A')
    date_released = models.DateField()
    certification = models.CharField(max_length=20, choices=CERTIFICATION)
    cover_art = models.FileField(upload_to='cover_art')

    def __str__(self):
        return self.album


class UserPayroll(models.Model):
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )

    artist_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    general_salary = models.CharField(max_length=50)
    show_tour_income = models.CharField(max_length=50)
    platforms_income = models.CharField(max_length=50)
    insurance = models.CharField(max_length=50)
    transport = models.CharField(max_length=50)
    accommodation = models.CharField(max_length=50)
    month = models.CharField(max_length=40, choices=MONTH)
    date_paid = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.general_salary


class Studio(models.Model):
    studio_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    main_producer = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.studio_name


class StudioSession(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Missed', 'Missed')

    )

    booked_date = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    artist = models.ForeignKey(UserDetail, related_name='Producer', on_delete=models.CASCADE)
    producer = models.ForeignKey(UserDetail, related_name='Artist', on_delete=models.CASCADE)


class ShowsTours(models.Model):
    artist_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    show_amount = models.CharField(max_length=50)
    disk_jokey = models.CharField(max_length=50)
    start_date = models.CharField(max_length=40)
    end_date = models.CharField(max_length=40)
    venue = models.CharField(max_length=40)
    duration = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)

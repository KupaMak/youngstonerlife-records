# Generated by Django 4.0.6 on 2022-08-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('national_id', models.CharField(default='0000000', max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('department', models.CharField(choices=[('Artist', 'Artist'), ('Producer', 'Producer'), ('Chief Executive Officer', 'Chief Executive Officer'), ('Manager', 'Manager'), ('Disk Jokey', 'Disk Jokey')], default='Artist', max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('date_employed', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('account_number', models.CharField(max_length=50)),
                ('stage_name', models.CharField(default='N/A', max_length=40)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserPayroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_salary', models.CharField(max_length=50)),
                ('show_tour_income', models.CharField(max_length=50)),
                ('platforms_income', models.CharField(max_length=50)),
                ('insurance', models.CharField(max_length=50)),
                ('transport', models.CharField(max_length=50)),
                ('accommodation', models.CharField(max_length=50)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=40)),
                ('date_paid', models.DateField(auto_now_add=True)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='UserAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(default='N/A', max_length=40)),
                ('no_of_tracks', models.CharField(max_length=50)),
                ('first_week_sales', models.CharField(default='N/A', max_length=40)),
                ('date_released', models.DateField()),
                ('certification', models.CharField(choices=[('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond'), ('N/A', 'N/A')], max_length=20)),
                ('cover_art', models.FileField(upload_to='cover_art')),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='StudioSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Missed', 'Missed')], max_length=50)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Producer', to='core.userdetail')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Artist', to='core.userdetail')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.studio')),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='main_producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail'),
        ),
        migrations.CreateModel(
            name='ShowsTours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_amount', models.CharField(max_length=50)),
                ('disk_jokey', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=40)),
                ('end_date', models.CharField(max_length=40)),
                ('venue', models.CharField(max_length=40)),
                ('duration', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail')),
            ],
        ),
    ]
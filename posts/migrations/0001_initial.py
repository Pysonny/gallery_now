
# Generated by Django 3.2.18 on 2023-05-18 05:22


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

        ('taggit', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ko', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('nationality', models.CharField(choices=[('KOR', 'South Korea'), ('USA', 'United States'), ('JPN', 'Japan'), ('CHN', 'China')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('period', models.CharField(blank=True, default=1, max_length=100)),
                ('time', models.CharField(blank=True, default=1, max_length=100)),
                ('charge', models.CharField(blank=True, default=1, max_length=100)),
                ('grade', models.CharField(blank=True, default=1, max_length=100)),
                ('venue', models.TextField(blank=True, default=1, max_length=100)),
                ('thumbnail', models.ImageField(blank=True, upload_to=posts.models.Exhibition.img_path)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('closed_days', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, upload_to=posts.models.Item.img_path)),
                ('title', models.TextField(blank=True)),
                ('alternativeTitle', models.TextField(blank=True)),
                ('creator', models.TextField(blank=True)),
                ('regDate', models.TextField(blank=True)),
                ('collectionDb', models.TextField(blank=True)),
                ('subjectCategory', models.TextField(blank=True)),
                ('subjectKeyword', models.TextField(blank=True)),
                ('extent', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('spatial', models.TextField(blank=True)),
                ('temporalCoverage', models.TextField(blank=True)),
                ('person', models.TextField(blank=True)),
                ('language', models.TextField(blank=True)),
                ('sourceTitle', models.TextField(blank=True)),
                ('referenceIdentifier', models.TextField(blank=True)),
                ('rights', models.TextField(blank=True)),
                ('copyrightOthers', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('contributor', models.TextField(blank=True)),
                ('eventPeriod', models.TextField(blank=True)),
                ('charge', models.TextField(blank=True)),
                ('grade', models.TextField(blank=True)),
                ('venue', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('thumbnails', models.ImageField(blank=True, upload_to=posts.models.Theme.img_path)),
                ('exhibitions', models.ManyToManyField(related_name='themes', to='posts.Exhibition')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),

                ('exhibition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.exhibition')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),

            ],
        ),
        migrations.AddField(
            model_name='exhibition',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.item'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

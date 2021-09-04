# Generated by Django 3.1.4 on 2021-04-22 06:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('logo', django_resized.forms.ResizedImageField(crop=None, default='post.jpg', force_format='PNG', keep_meta=True, quality=100, size=[200, 200], upload_to='company_logo')),
                ('founded', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=150)),
                ('website', models.URLField()),
                ('jobs', models.URLField()),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('follower', models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['?'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_genre', models.IntegerField(choices=[(1, 'Java'), (2, 'Javascript'), (3, 'Python'), (4, 'C#'), (5, 'Human Resource'), (6, 'Personality'), (7, 'Other')], default=7)),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='api.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Option')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is this correct option?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', django_resized.forms.ResizedImageField(crop=None, default='article.jpg', force_format='PNG', keep_meta=True, quality=100, size=[400, 300], upload_to='article_thumbnails')),
                ('approved', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
                ('read_time', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('liked_by', models.ManyToManyField(related_name='articleLikedBy', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.IntegerField(choices=[(1, 'Vancouver')], default=1)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('job_type', models.IntegerField(choices=[(1, 'Full time'), (2, 'Part time'), (3, 'Internship'), (4, 'Remote'), (5, 'Partnership'), (6, 'Contract')], default=1)),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('salary', models.IntegerField(blank=True, default=0, help_text='Please put hourly salary, if unpaid leave it blank.', null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)])),
                ('deadline', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('external_resource', models.BooleanField(default=False)),
                ('apply_link', models.URLField(blank=True, help_text='Redirect to origin site if wanted', null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.company')),
                ('favourite', models.ManyToManyField(related_name='JobFavourite', to=settings.AUTH_USER_MODEL)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('technologies', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
    ]

from django.db import models
from users.models import User
from django.utils.crypto import get_random_string
from api.models.choices import QUESTION_GENRE_CHOICES
from time import time
from django.utils.text import slugify


class Question(models.Model):
    question_genre = models.IntegerField(choices=QUESTION_GENRE_CHOICES, default=7)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField('Option', max_length=255)
    is_correct = models.BooleanField('Is this correct option?', default=False)

    def __str__(self):
        return self.text


class Quiz(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="quizzes")
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    questions = models.ManyToManyField(Question)

    @property
    def number_of_questions(self):
        return self.questions.all().count()

    def is_quiz_empty(self):
        return not self.questions.exists()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        strtime = "".join(str(time()).split("."))
        string = "%s%s" % (get_random_string(length=4),strtime[6:])
        self.slug = slugify(string)
        super(Quiz, self).save()

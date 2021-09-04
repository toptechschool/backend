from django.contrib import admin
from api.models import Note,Company,VideoLink,Job,Question,Option,Quiz


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','author','date_updated','views']
    list_filter = ['approved','featured','date_updated']
    search_fields = ['title','content','tags']
    ordering = ['date_updated']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['company','title']
    list_filter = ['location','job_type','posted_at','salary'] 
    search_fields = ['company','title','description','technology']
    ordering = ['deadline']

class OptionInline(admin.TabularInline):
    model = Option

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline, ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)

admin.site.register(Company)
admin.site.register(VideoLink)
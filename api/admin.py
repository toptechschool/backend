from django.contrib import admin
from api.models import Company,Job,Question,Option,Quiz


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


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]
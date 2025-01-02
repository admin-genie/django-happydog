from django.contrib import admin
from .models import CustomUser, SurveyResult, SitterSurveyResult, Post
from .forms import UserSignupForm, SurveyForm, SitterSurveyForm

class CustomUserAdmin(admin.ModelAdmin):
    form = UserSignupForm

class SurveyResultAdmin(admin.ModelAdmin):
    form = SurveyForm  

class SitterSurveyResultAdmin(admin.ModelAdmin):
    form = SitterSurveyForm  

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'author', 'created_at')  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SurveyResult, SurveyResultAdmin)
admin.site.register(SitterSurveyResult, SitterSurveyResultAdmin) 
admin.site.register(Post, PostAdmin)
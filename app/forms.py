from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, SurveyResult, SitterSurveyResult, Post
from django.contrib.auth.forms import AuthenticationForm

class UserSignupForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="생년월일",
        help_text="연도-월-일",
    )
    gender = forms.ChoiceField(
        choices=CustomUser.GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=False,
        label="성별",
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '전화번호'}),
        required=False,
        label="전화번호",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': '이메일 주소'}),
        required=True,
        label="이메일",
    )
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='유형을 선택하세요.',
        label="유형",
    )
    local = forms.ChoiceField(
        choices=CustomUser.LOCAL_CHOICES, 
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='지역을 선택하세요.',
        label="지역",
    )    

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'birth_date', 'gender', 'phone_number', 'email', 'user_type', 'local']  
        labels = {'first_name': '이름'}

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResult
        fields = ['question1_response', 'question2_response', 'question3_response', 'question4_response', 'question5_response', 'question6_response', 'question7_response', 'question8_response']

class SitterSurveyForm(forms.ModelForm):
    class Meta:
        model = SitterSurveyResult
        fields = ['question1_response', 'question2_response', 'question3_response', 'question4_response', 'question5_response', 'question6_response', 'question7_response']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디'}),
        label="아이디",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'}),
        label="비밀번호",
    )
            
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class ReservationForm(forms.Form):
    start_date = forms.DateTimeField(label="시작 날짜")
    end_date = forms.DateTimeField(label="마침 날짜")
    pickup_time = forms.DateTimeField(label="데려가는 시간")
    dropoff_time = forms.DateTimeField(label="맡기는 시간")

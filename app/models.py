from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('남', '남'),
        ('여', '여'),
    )
    USER_TYPE_CHOICES = (
        ('user', '사용자'),
        ('sitter', '돌봄이')
    )
        
    LOCAL_CHOICES = (
        ('지역을 선택하세요.', '지역을 선택하세요.'),
        ('강남구', '강남구'),
        ('강동구', '강동구'),
        ('강북구', '강북구'),
        ('강서구', '강서구'),
        ('관악구', '관악구'),
        ('광진구', '광진구'),
        ('구로구', '구로구'),
        ('금천구', '금천구'),
        ('노원구', '노원구'),
        ('도봉구', '도봉구'),
        ('동대문구', '동대문구'),
        ('동작구', '동작구'),
        ('마포구', '마포구'),
        ('서대문구', '서대문구'),
        ('서초구', '서초구'),
        ('성동구', '성동구'),
        ('성북구', '성북구'),
        ('송파구', '송파구'),
        ('양천구', '양천구'),
        ('영등포구', '영등포구'),
        ('용산구', '용산구'),
        ('은평구', '은평구'),
        ('종로구', '종로구'),
        ('중구', '중구'),
        ('중랑구', '중랑구'),    
    )

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    local = models.CharField(max_length=10, choices=LOCAL_CHOICES, default='지역을 선택하세요.')
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')  
    
    def __str__(self):
        return self.username
    
    def get_age(self):
        today = date.today()

        # 생년월일을 기준으로 나이 계산
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
        return age

class SurveyResult(models.Model):
    question1_response = models.FloatField()
    question2_response = models.FloatField()
    question3_response = models.FloatField()
    question4_response = models.FloatField()
    question5_response = models.FloatField()
    question6_response = models.FloatField()
    question7_response = models.FloatField()
    question8_response = models.FloatField()
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

class SitterSurveyResult(models.Model):
    question1_response = models.FloatField()
    question2_response = models.FloatField()
    question3_response = models.FloatField()
    question4_response = models.FloatField()
    question5_response = models.FloatField()
    question6_response = models.FloatField()
    question7_response = models.FloatField()
    writer1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

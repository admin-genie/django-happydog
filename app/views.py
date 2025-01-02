from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignupForm, SurveyForm, SitterSurveyForm, PostForm, PostEditForm
from .models import SurveyResult, SitterSurveyResult, Post, CustomUser
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
import numpy as np
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def sitter(request):
    return render(request, 'sitter.html')

def ex_sitter(request):
    return render(request, 'ex_sitter.html')

def sitterapplication(request):
    return render(request, 'sitterapplication.html')

def community(request):
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page', 1)
    page_posts = paginator.get_page(page_number)

    return render(request, 'community.html', {'posts': page_posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostEditForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, pk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=pk)
            if request.user == post.author:
                post.delete()
                return JsonResponse({'success': True})
        except Post.DoesNotExist:
            pass
    
    return JsonResponse({'success': False})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            if user.user_type == 'user':
                welcome_message = f"{user.username}님 반갑습니다."
                redirect_url = 'login_end.html'
            elif user.user_type == 'sitter':
                welcome_message = f"{user.username}돌보미님 반갑습니다."
                redirect_url = 'sitter_login_end.html'
            else:
                welcome_message = ""
                redirect_url = 'login_end.html' 

            return render(request, redirect_url, {'welcome_message': welcome_message})
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def login_end(request):
    return render(request, 'login_end.html')

def sitter_login_end(request):
    return render(request, 'sitter_login_end.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')

def user_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            user_type = user_form.cleaned_data.get('user_type')
            if user_type == 'user':
                return redirect('next_step')  
            elif user_type == 'sitter':
                return redirect('next_step1')
            return redirect('next_step')  
    else:
        user_form = UserSignupForm()

    return render(request, 'user_signup.html', {'user_form': user_form})

def next_step(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            question1_response = form.cleaned_data['question1_response']
            question2_response = form.cleaned_data['question2_response']
            question3_response = form.cleaned_data['question3_response']
            question4_response = form.cleaned_data['question4_response']
            question5_response = form.cleaned_data['question5_response']
            question6_response = form.cleaned_data['question6_response']
            question7_response = form.cleaned_data['question7_response']
            question8_response = form.cleaned_data['question8_response']

            # SurveyResult 모델에 데이터 저장
            survey_result = SurveyResult(
                question1_response=question1_response,
                question2_response=question2_response,
                question3_response=question3_response,
                question4_response=question4_response,
                question5_response=question5_response,
                question6_response=question6_response,
                question7_response=question7_response,
                question8_response=question8_response,
                writer = request.user
            )
            survey_result.save()

            return redirect('signup_end') 

    else:
        form = SurveyForm()

    return render(request, 'next_step.html', {'form': form})

def next_step1(request):
    if request.method == 'POST':
        form = SitterSurveyForm(request.POST)
        if form.is_valid():
            question1_response = form.cleaned_data['question1_response']
            question2_response = form.cleaned_data['question2_response']
            question3_response = form.cleaned_data['question3_response']
            question4_response = form.cleaned_data['question4_response']
            question5_response = form.cleaned_data['question5_response']
            question6_response = form.cleaned_data['question6_response']
            question7_response = form.cleaned_data['question7_response']

            # SitterSurveyResult 모델에 데이터 저장
            sittersurvey_result = SitterSurveyResult(
                question1_response=question1_response,
                question2_response=question2_response,
                question3_response=question3_response,
                question4_response=question4_response,
                question5_response=question5_response,
                question6_response=question6_response,
                question7_response=question7_response,
                writer1 = request.user
            )
            sittersurvey_result.save()

            return redirect('signup_end') 

    else:
        form = SitterSurveyForm()

    return render(request, 'next_step1.html', {'form': form})

def signup_end(request):
    return render(request, 'signup_end.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def sitter_profile(request):
    return render(request, 'sitter_profile.html')

def calculate_top_sitters(request):
    user_id = request.user.id

    try:
        user = CustomUser.objects.get(id=user_id)
        user_local = user.local 
        user_survey_result = SurveyResult.objects.get(writer=user)
        user_region_importance = user_survey_result.question1_response

        if user_region_importance == 1.0:
            petSitterList = CustomUser.objects.filter(user_type='sitter', local=user_local)
        else:
            petSitterList = CustomUser.objects.filter(user_type='sitter')

        survey_result = SurveyResult.objects.get(writer=user)
        userSizePref = survey_result.question2_response
        userPickupPref = survey_result.question3_response
        userWalkPref = survey_result.question4_response
        userMultiPref = survey_result.question5_response
        userDayOverPref = survey_result.question6_response
        userVisitPref = survey_result.question7_response
        userLicensePref = survey_result.question8_response

        userCount = 0
        dataCount = len(petSitterList) 

        sitter_results = []

        for sitter in petSitterList:
            try:
                sitter_survey = SitterSurveyResult.objects.get(writer1=sitter)
            except SitterSurveyResult.DoesNotExist:
                continue

            # 시터와 사용자 간의 연관성 점수 계산
            sitterSizeCapability = sitter_survey.question1_response
            sitterPickupCapability = sitter_survey.question2_response
            sitterWalkCapability = sitter_survey.question3_response
            sitterMultiCapability = sitter_survey.question4_response
            sitterDayOverCapability = sitter_survey.question5_response
            sitterVisitCapability = sitter_survey.question6_response
            sitterLicenseCapability = sitter_survey.question7_response

            score = 0  

            if userSizePref == 1 and sitterSizeCapability == 1:
                score += 2
            elif userSizePref == 0.3 and sitterSizeCapability == 1:
                score += 1.3
            elif userSizePref == 0 and sitterSizeCapability == 0:
                score += 0

            if userPickupPref == 1 and sitterPickupCapability == 1:
                score += 2
            elif userPickupPref == 0.3 and sitterPickupCapability == 1:
                score += 1.3
            elif userPickupPref == 0 and sitterPickupCapability == 0:
                score += 0
                
            if userWalkPref == 1 and sitterWalkCapability == 1:
                score += 2
            elif userWalkPref == 0.3 and sitterWalkCapability == 1:
                score += 1.3
            elif userWalkPref == 0 and sitterWalkCapability == 0:
                score += 0

            if userMultiPref == 1 and sitterMultiCapability == 1:
                score += 2
            elif userMultiPref == 0.3 and sitterMultiCapability == 1:
                score += 1.3
            elif userMultiPref == 0 and sitterMultiCapability == 0:
                score += 0

            if userDayOverPref == 1 and sitterDayOverCapability == 1:
                score += 2
            elif userDayOverPref == 0.3 and sitterDayOverCapability == 1:
                score += 1.3
            elif userDayOverPref == 0 and sitterDayOverCapability == 0:
                score += 0
                
            if userVisitPref== 1 and sitterVisitCapability == 1:
                score += 2
            elif userVisitPref == 0.3 and sitterVisitCapability == 1:
                score += 1.3
            elif userVisitPref == 0 and sitterVisitCapability == 0:
                score += 0
                
            if userLicensePref== 1 and sitterLicenseCapability == 1:
                score += 2
            elif userLicensePref == 0.3 and sitterLicenseCapability == 1:
                score += 1.3
            elif userLicensePref == 0 and sitterLicenseCapability == 0:
                score += 0
            
            if user_region_importance == 1 and user_local == sitter.local:
                score += 1
                
            sitter_results.append({'sitter': sitter, 'sitter_survey': sitter_survey, 'score': np.round(score, 3)})

        # 정확도(score)를 기준으로 내림차순 정렬
        sitter_results.sort(key=lambda x: x['score'], reverse=True)

        top_sitters = sitter_results[:10]

        context = {
            'top_sitters': top_sitters,
        }

        return render(request, 'calculate_top_sitters.html', context)

    except CustomUser.DoesNotExist:
        return render(request, 'index.html')

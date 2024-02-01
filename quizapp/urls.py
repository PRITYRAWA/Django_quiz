"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from authentication.views import register, user_login
from django.contrib import admin
from django.urls import include, path
from quiz.views import QuizQuestionListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', user_login, name='user_login'),
    path('', include('quiz.urls')),
    path('api/questions/', QuizQuestionListCreateView.as_view(), name='question-list-create'),
]

# urls.py

from django.urls import path

from .views import (QuizPageView, QuizQuestionListCreateView, QuizResultsView,
                    restart_quiz)

urlpatterns = [
    path('quiz/', QuizPageView.as_view(), name='quiz_page'),
    path('quiz/results/', QuizResultsView.as_view(), name='quiz_results'),
    path('quiz/restart/', restart_quiz, name='restart_quiz'),
    path('api/questions/', QuizQuestionListCreateView.as_view(), name='question-list-create'),
]

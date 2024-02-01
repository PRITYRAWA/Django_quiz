from django.contrib import messages
from django.contrib.sessions.models import Session
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from rest_framework import generics

from .models import QuizQuestion, QuizSession, UserResponse
from .serializers import QuizQuestionSerializer


class QuizQuestionListCreateView(generics.ListCreateAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    
class QuizPageView(View):
    template_name = 'quiz/quiz_page.html'

    def get(self, request, *args, **kwargs):
        questions = QuizQuestion.objects.all()
        return render(request, self.template_name, {'questions': questions})

    def post(self, request, *args, **kwargs):
        questions = QuizQuestion.objects.all()
        score = 0

        try:
            session_id = request.session.session_key
            django_session = Session.objects.get(session_key=session_id)
        except Session.DoesNotExist:
            return redirect('quiz_results')

        quiz_session, created = QuizSession.objects.get_or_create(user=request.user, session=django_session)

        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}")
            print(f"Question {question.id} - Selected Option: {selected_option}")

            if selected_option is not None:
                UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=selected_option,
                    quiz_session=quiz_session
                )

                if selected_option == question.correct_option:
                    score += 1

        request.session['quiz_score'] = score
        return redirect('quiz_results')

class QuizResultsView(View):
    template_name = 'quiz/quiz_result.html'

    def get(self, request, *args, **kwargs):
        quiz_session = QuizSession.objects.filter(user=request.user).first()

        if not quiz_session:
            messages.error(request, 'No quiz session found. Please take the quiz first.')
            return redirect('quiz_page')
        
        user_responses = UserResponse.objects.filter(user=request.user, quiz_session=quiz_session)

        questions = QuizQuestion.objects.all()
        score = request.session.get('quiz_score', 0)

        context = {
            'questions': questions,
            'user_responses': user_responses,
            'score': score,
        }

        return render(request, self.template_name, context)



def restart_quiz(request):
    UserResponse.objects.filter(user=request.user).delete()
    
    if 'quiz_score' in request.session:
        del request.session['quiz_score']

    messages.success(request, 'Quiz results have been reset. You can now restart the quiz.')
    return redirect('quiz_page')
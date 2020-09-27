from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_invalid(self, form):
        result = super().form_valid(form)
        user_data = form.cleaned_data
        user = authenticate(username=user_data['username'], password=user_data['password1'])
        login(self.request, user)

        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_invalid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)

        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])





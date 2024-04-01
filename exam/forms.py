from django import forms
from django.forms import inlineformset_factory
from .models import Question, Course, Option

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'question_number', 'total_marks']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['value']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'course', 'photo']  # Include the photo field
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control form-control-sm arrondi-0', 'required': True}),
            'course': forms.Select(attrs={'class': 'form-control form-control-sm arrondi-0'}),
            #'marks': forms.TextInput(attrs={'class': 'form-control form-control-sm arrondi-0', 'placeholder': 'Example: 5'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Add a file upload widget for the photo
        }

OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm, extra=1)

QuestionFormSet = inlineformset_factory(Course, Question, form=QuestionForm, extra=1)

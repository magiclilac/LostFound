from django import forms
from .models import Report


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report

        fields = [
            'student_name',
            'enrollment_number',
            'phone_number',
            'report_type',
            'item_name',
            'category',
            'description',
            'location',
            'date_time',
            'status',
        ]

        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),

            'enrollment_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter enrollment number'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'report_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the item...',
                'rows': 4
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where was it lost/found?'
            }),

            'date_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
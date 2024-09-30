from django import forms

class NotesForm(forms.Form):
    title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,  # Number of rows
            'cols': 40,  # Number of columns
            'placeholder': 'Enter title here...',
        })
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 10,  # Number of rows
            'cols': 40,  # Number of columns
            'placeholder': 'Enter content here...',
        })
    )
from django import forms
from .models import Paper

class PaperForm(forms.ModelForm):
    # Form-only fields (not in model)
    save_for_future = forms.BooleanField(
        required=False,
        label='Save for future reference',
        widget=forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'})
    )
    reference_note = forms.CharField(
        required=False,
        label='Reference Note',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Add any notes or reminders about this submission',
            'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )

    class Meta:
        model = Paper
        fields = [
            'title',
            'paper_file',
            'area_of_research',
            'author_name',
            'institution',
            'email',
            'mobile',
            'address_line1',
            'address_line2',
            'country',
            'state',
            'city',
            'pincode',
            'prev_paper'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter paper title',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'area_of_research': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'author_name': forms.TextInput(attrs={
                'placeholder': 'Enter author name',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'institution': forms.TextInput(attrs={
                'placeholder': 'Enter institution name',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'mobile': forms.TextInput(attrs={
                'placeholder': 'Enter mobile number',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'address_line1': forms.TextInput(attrs={
                'placeholder': 'Enter address line 1',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'address_line2': forms.TextInput(attrs={
                'placeholder': 'Enter address line 2 (optional)',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter country',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'Enter state',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter city',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'pincode': forms.TextInput(attrs={
                'placeholder': 'Enter pincode',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'prev_paper': forms.TextInput(attrs={
                'placeholder': 'Enter previous paper details (optional)',
                'class': 'w-full border border-gray-300 rounded px-3 sm:px-4 py-2 text-sm sm:text-base focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        } 
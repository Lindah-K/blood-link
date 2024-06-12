from django.contrib import admin
from .models import ContactDetails
from ckeditor.widgets import CKEditorWidget
from django import forms

class ContactDetailsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    display_contact_info = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = ContactDetails
        fields = '__all__'

class ContactDetailsAdmin(admin.ModelAdmin):
    form = ContactDetailsAdminForm

admin.site.register(ContactDetails, ContactDetailsAdmin)

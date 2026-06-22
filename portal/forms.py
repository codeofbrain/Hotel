
from django import forms
from .models import MaintenanceRequest, Announcement

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['description']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['content']
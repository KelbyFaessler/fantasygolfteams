from django import forms

class TeamForm(forms.Form):
    num_teams = forms.IntegerField(required=False)
    players = forms.CharField(widget=forms.Textarea, max_length=2000)
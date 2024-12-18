from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from category.models import Category
from django.forms import Form
from language.models import Language
from school.models import School
from dusza_web.settings import UNIFIED_MAX_LENGTH,UNIFIED_MIN_LENGTH
from .models import Team

class TeamMissingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TeamMissingForm, self).__init__(*args, **kwargs)
        # add custom error messages
        for field in self.fields:
            self.fields[field].error_messages.update({
                'required': 'Ez a mező szükséges!',
                'max_length': f"Meghaladja a karakterhatárt!",
                'min_length': f"Nem haladja meg a karakterhatárt!",
            })

    missing = forms.CharField(label='Üzenet',max_length=UNIFIED_MAX_LENGTH,min_length=UNIFIED_MIN_LENGTH)

    def save(self, request, team_id):
        #TODO: visszavonja a jóváhagyást a sulitól
        team = Team.objects.get(pk=team_id)
        if team.joined:
            self.add_error("missing","A csapat már csatlakozott!")
            return False
        team.missing = self.cleaned_data['missing']
        team.approved = False
        team.approval_file = None
        team.save()
        return team
class TeamApprovalForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super(TeamApprovalForm,self).__init__(*args,**kwargs)
        # add custom error messages
        for field in self.fields:
            self.fields[field].error_messages.update({
                'required': 'Ez a mező szükséges!',
                'invalid': f"Nem érvényes fájl!",
                'missing': f"Adjon meg egy fájlt!",
                "empty":f"A fájl üres!",
            })

    file = forms.FileField(label='Aláírt jelentkezési lap', help_text='max. 128 megabytes')
    def check(self):
        mime = self.cleaned_data["file"].content_type.split("/")[1]
        if mime != "pdf":
            self.add_error("file","Nem pdf formátum!")
            return False
        if self.cleaned_data["file"].size/1024/1024 > 128:
            self.add_error("file","A megadott fájl meghaladja a 128 megabyte-ot")
            return False
        return True

    def save(self, request,team_id):
        team = Team.objects.get(pk=team_id)
        team.approval_file = request.FILES["file"]
        team.approved = True
        team.missing = None
        team.save()
class TeamCreationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)

        # add custom error messages
        for field in self.fields:
            self.fields[field].error_messages.update({
                'required': 'Ez a mező szükséges!',
                'max_length': f"Meghaladta a maximális karakterhatárt ({UNIFIED_MAX_LENGTH})",
                'min_length': f"Nem haladta meg a minimális karakterhatárt ({UNIFIED_MIN_LENGTH})",
                "min_value":f"Minimum értéket nem haladta meg ({1})",
                "invalid":f"Megadott érték nem szám!",
                "max_decimal_places":"Egész számnak kell lennie!",
                "max_digits":"Maximum 2 számjegy adható meg!",
                "max_whole_digits":"Maximum 2 számjegy adható meg!"
            })
    name = forms.CharField(label='Csapat neve', min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH)
    contestant1_name = forms.CharField(label='1. versenyző neve',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH )
    contestant1_grade = forms.DecimalField(label='1. versenyző évfolyama', decimal_places=0,max_digits=2,min_value=1)
    contestant2_name = forms.CharField(label='2. versenyző neve',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH )
    contestant2_grade = forms.DecimalField(label='2. versenyző évfolyama', decimal_places=0,max_digits=2 ,min_value=1)
    contestant3_name = forms.CharField(label='3. versenyző neve',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH )
    contestant3_grade = forms.DecimalField(label='3. versenyző évfolyama', decimal_places=0,max_digits=2 ,min_value=1)
    contestant4_name = forms.CharField(label='Póttag neve',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH,required=False )
    contestant4_grade = forms.DecimalField(label='Póttag évfolyama', decimal_places=0,max_digits=2 ,min_value=1,required=False)
    school = forms.ModelChoiceField(label="Iskola", queryset=School.objects.all(),initial=Category.objects.first())
    teachers = forms.CharField(label='Felkészítő tanár neve',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH )
    category =  forms.ModelChoiceField(label="Kategória",queryset=Category.objects.all(),initial=Category.objects.first())
    language =  forms.ModelChoiceField(label="Nyelv",queryset=Language.objects.all(),initial=Category.objects.first())
    def check(self,request):
        name = self.cleaned_data['name']
        new = Team.objects.filter(name=name).first()
        if new and new.id != Team.objects.filter(user=request.user).first().id:
            self.add_error("name", "Ilyen csapatnév már létezik.")
            return False
        if (self.cleaned_data['contestant4_name'] != "" and self.cleaned_data['contestant4_grade'] is None) or (
                self.cleaned_data['contestant4_name'] == "" and self.cleaned_data['contestant4_grade']):
            self.add_error("contestant4_grade", "Póttag évfolyama vagy neve hiányzik")
            return False
        return True
    def name_clean(self):
        name = self.cleaned_data['name']
        return name
    def update(self,request):
        team = Team.objects.filter(user=request.user).update(
            name=self.cleaned_data['name'],
            contestant1_name=self.cleaned_data['contestant1_name'],
            contestant1_grade=self.cleaned_data['contestant1_grade'],
            contestant2_name=self.cleaned_data['contestant2_name'],
            contestant2_grade=self.cleaned_data['contestant2_grade'],
            contestant3_name=self.cleaned_data['contestant3_name'],
            contestant3_grade=self.cleaned_data['contestant3_grade'],
            contestant4_name=self.cleaned_data['contestant4_name'],
            contestant4_grade=self.cleaned_data['contestant4_grade'],
            teachers=self.cleaned_data['teachers'],
            school=self.cleaned_data['school'],
            category=self.cleaned_data['category'],
            language=self.cleaned_data['language'],
        )
        return team
    def save(self,request, commit=True):
        team = Team.objects.create(
            name=self.cleaned_data['name'],
            contestant1_name=self.cleaned_data['contestant1_name'],
            contestant1_grade=self.cleaned_data['contestant1_grade'],
            contestant2_name=self.cleaned_data['contestant2_name'],
            contestant2_grade=self.cleaned_data['contestant2_grade'],
            contestant3_name=self.cleaned_data['contestant3_name'],
            contestant3_grade=self.cleaned_data['contestant3_grade'],
            contestant4_name=self.cleaned_data['contestant4_name'],
            contestant4_grade=self.cleaned_data['contestant4_grade'],
            teachers=self.cleaned_data['teachers'],
            school=self.cleaned_data['school'],
            user=request.user,
            category=self.cleaned_data['category'],
            language=self.cleaned_data['language'],
        )
        return team
from django import forms
from .models import Contact,Apply
from .models import Partner,Candidate,Enquiry 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','mail','contact_Number','message')
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control' }),
            'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'message':forms.Textarea(attrs={'rows' : 4, 'cols' : 23 , 'class' : 'form-control'})
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('name','email','contact_Number','current_City','upload_Resume')
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'current_City':forms.TextInput(attrs={'class' : 'form-control'}),
            # 'upload_Resume' :forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }
        

class EnquiryForm(forms.ModelForm):
    class Meta :
        model = Enquiry
        fields = ('name','company','post','mail','contact_Number','city','description')
        widgets={
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'company' : forms.TextInput(attrs={'class': 'form-control'}),
                'post': forms.TextInput(attrs={'class': 'form-control'}),
                'mail': forms.EmailInput(attrs={'class': 'form-control' }),
                'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
                'city':forms.TextInput(attrs={'class' : 'form-control'}),
                'description':forms.Textarea(attrs={'rows' : 4, 'cols' : 23,'class' : 'form-control'})
                }
class PartnerForm(forms.ModelForm):
    class Meta :
        model = Partner
        fields = ('organisation_Type','organisationName','name','email','contact_Number','experience')
        widgets={
                'organisation_Type': forms.Select(attrs={'class': 'form-control'}),
                'organisationName' : forms.TextInput(attrs={'class': 'form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control' }),
                'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
                'experience':forms.Select(attrs={'class' : 'form-control'}),
#                 'description':forms.Textarea(attrs={'rows' : 4, 'cols' : 23,'class' : 'form-control'})
                }

class CandidateForm(forms.ModelForm):
    class Meta :
        model = Candidate
        fields = ('full_Name','email','contact_Number','father_Name','education','PAN_Number','aadhar_Number','location','last_Salary','last_Company','upload_Resume')
        # widgets={
        #         'full_Name': forms.TextInput(attrs={'class':'form-control'}),
        #         'email': forms.EmailInput(attrs={'class': 'form-control' }),
        #         'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
        #         'father_Name':forms.TextInput(attrs={'class': 'form-control'}),
        #         'education':forms.TextInput(attrs={'class': 'form-control'}),
        #         'PAN_Number':forms.NumberInput(attrs={'class' : 'form-control'}),
        #         'aadhar_Number':forms.NumberInput(attrs={'class': 'form-control'}),
        #         'location' : forms.TextInput(attrs={'class':'form-control'}),
        #         'last_Salary' :forms.NumberInput(attrs={'class':'form-control'}),
        #         'last_Company':forms.TextInput(attrs ={'class':'form-control'}),
        #         'upload_Resume': forms.ClearableFileInput(attrs={'class':'form-control-file'})
        #         # 'experience':forms.Select(attrs={'class' : 'form-control'}),
        #         }

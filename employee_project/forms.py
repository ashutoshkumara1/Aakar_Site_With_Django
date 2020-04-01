from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # For Fields You can Provide a Tuple instead of __all__
        # you can change the order of tuple in Display.
        fields = '__all__' #{'position', 'emp_code', 'mobile', 'fullname', }  # '__all__'
        # Labels for Change the Name of Form Field with Default Name
        labels = {
            'fullname':'Full Name',
            'mobile':'Mobile',
            'emp_code':'Employee Code',
            'position':'Position'

        }

    def __init__(self, *args, **kwagrs):
        super(EmployeeForm,self).__init__(*args, **kwagrs)
        self.fields['position'].empty_label = "Select" # For Fill the Empty Field with "Select"
        self.fields['emp_code'].required = False # For Validation Remove
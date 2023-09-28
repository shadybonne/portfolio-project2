from django import forms
from django.forms import ModelForm
from .models import Member, Transaction, AccountSummary

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','lname', 'mname', 'dob', 'email', 'phone', 'occupation', 'address', 'nok']
        

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount']

#class AccountSummary(ModelForm):
#    class Meta:
 #       model = AccountSummary
 #       fields = ['total_deposits', 'current_balance']
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Member, AccountSummary, Transaction
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main.html')

def membership(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Hey, Registered Successfully.")
        return redirect("storeroom:index")
    
    else:
        return render(request, "memberform.html")
    


def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    account_summary = AccountSummary.objects.get(member=member)
    transactions = Transaction.objects.filter(member=member)
    return render(request, 'members/member_detail.html', {'member': member, 'account_summary': account_summary, 'transactions': transactions})



def financial_contributions(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    transactions = Transaction.objects.filter(member=member)

    if request.method == 'GET':
        year = request.GET.get('year')
        if year:
            transactions = transactions.filter(transaction_date__year=year)

    return render(request, 'members/financial_contributions.html', {'member': member, 'transactions': transactions})


def account_summary(request):
    
    account_summary = AccountSummary.objects.get(member=account_summary)

    return render(request, 'account_summary.html', {'member_accounts': account_summary})


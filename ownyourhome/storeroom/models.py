from django.db import models


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    occupation = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    nok = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Transaction(models.Model):
    TRANSACTION_CHOICES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    total_deposits = models.FloatField()
   

    def __str__(self):
        return f"{self.get_transaction_type_display()} of #{self.amount} for {self.member}"
    
    def update_summary(self):
        transactions = Transaction.objects.filter(member=self.member)

        # Calculate the total deposits
        total_deposits = transactions.filter(transaction_type='deposit').aggregate(total=models.Sum('amount'))['total']


class AccountSummary(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    account_balance = models.FloatField()
    date_joined = models.DateTimeField(auto_now_add=True)
    total_deposits = models.FloatField()
    total_withdrawals = models.FloatField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account Summary for {self.member}"
    
    def update_summary(self):
        transactions = Transaction.objects.filter(member=self.member)

        # Calculate the total deposits and total withdrawals
        total_deposits = transactions.filter(transaction_type='deposit').aggregate(total=models.Sum('amount'))['total']
        total_withdrawals = transactions.filter(transaction_type='withdrawal').aggregate(total=models.Sum('amount'))['total']

        # Calculate the current balance
        current_balance = self.member.account_balance + total_deposits - total_withdrawals

        # Update the account summary
        self.total_deposits = total_deposits or 0
        self.total_withdrawals = total_withdrawals or 0
        self.current_balance = current_balance
        self.save()
    
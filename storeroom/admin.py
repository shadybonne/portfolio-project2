from django.contrib import admin
from userauths.models import User
from .models import Member, Transaction, AccountSummary
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'phone', 'occupation']

class Transaction(admin.ModelAdmin):
    list_display = ['member', 'total_deposits']


admin.site.register(User, UserAdmin,)
admin.site.register(Member, MemberAdmin)
admin.site.register(Transaction)
admin.site.register(AccountSummary)
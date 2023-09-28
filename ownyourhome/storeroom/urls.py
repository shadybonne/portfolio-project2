from django.urls import path
from storeroom.views import index
from storeroom.views import membership
from storeroom import views
#from storeroom.views import member_detail




app_name = "storeroom"

urlpatterns = [
    path("", index, name="index"),
    path("membership/", membership, name="membership" ),
   # path("", account_summary, name="account_summary" )
    #path("", member_detail, name="member_detail" )
    #path("", financial_contributions, name="financial_contributions" )
]
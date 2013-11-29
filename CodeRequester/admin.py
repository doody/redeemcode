from django.contrib import admin
from CodeRequester.models import User, RedeemCode, RedeemObject

admin.site.register(User)
admin.site.register(RedeemCode)
admin.site.register(RedeemObject)

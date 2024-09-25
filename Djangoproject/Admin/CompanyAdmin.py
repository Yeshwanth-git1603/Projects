from django.contrib import admin
from Myproject.models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name","origin","ceo","type","valuation"]

admin.site.register(Company,CompanyAdmin)



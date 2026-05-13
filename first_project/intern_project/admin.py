from django.contrib import admin
from .models import chaiVarity,ChaiReviews,Store,ChaiCertificate

# Register your models here.
class ReviewChaiInLine(admin.TabularInline):
    model = ChaiReviews
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ReviewChaiInLine]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varity',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')


admin.site.register(chaiVarity,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)

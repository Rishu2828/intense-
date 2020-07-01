from django.contrib import admin
from .models import Job
from .models import Contact,Apply ,Partner,Candidate,Enquiry

# Register your models here.
class JobAdmin(admin.ModelAdmin):
	fields = [
				"job_title",
				"job_des",
				"job_sal", 
				"job_loc"
				]

search_fields = ('job_title',)


class ContactAdmin(admin.ModelAdmin):
		fields = [
					"name",
					"mail",
					"contact_Number", 
					"message"
					]
		search_fields = ('name',)

class PartnerAdmin(admin.ModelAdmin):
	fields = [
				"name",
				"company",
				"post", 
				"mail",
				"contact_Number",
				"city",
				"description",
				]
	search_fields = ('name',)

class EnquiryAdmin(admin.ModelAdmin):

	fields = [
				"PLACEMENT_AGENCY",
				"FREELANCER",
				"NGO", 
				"TRAINING_INSTITUTE",
				"CYBER_CAFE",
				"COLLEGE",
				"TYPES",
				]
	search_fields = ('TYPES',)

class CandidateAdmin(admin.ModelAdmin):
	
	fields = [
			"full_Name",
			"contact_Number",
			"email", 
			"father_Name",
			"PAN_Number",
			"aadhar_Number",
			"location",
			"last_Salary",
			"last_Company",
			"upload_Resume",
			"uploaded_at",
				]


	search_fields = ('uploaded_at',)
admin.site.register(Job , JobAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Apply)
admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Partner,PartnerAdmin)
admin.site.register(Candidate,CandidateAdmin)
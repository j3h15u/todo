from django.contrib import admin
from list.models import Task

class TaskAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,				{'fields':['user']}),
		('To-do', 			{'fields':['task']}),
		('Due date',		{'fields':['due_date']}),
		('Completion date',	{'fields':['done_date']}),
		('Details', 		{'fields':['notes']})
	]
	list_display = ('user','task','is_done','due_date','done_date','notes')
	list_filter = ['user']
	#date_hierarchy = 'due_date'
admin.site.register(Task,TaskAdmin)
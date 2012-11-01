from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Task(models.Model):
	user = models.CharField(max_length=100)
	task = models.CharField(max_length=2000)
	due_date = models.DateTimeField('due date')
	done_date = models.DateTimeField('date completed', default=datetime.datetime.now()+datetime.timedelta(days=7))
	#inelegant workaround to not having a completion date while entering task
	#ideally, is_done would be a check box that defaults to False, and
	#done_date would self-populate with timestamp of is_done becoming True
	#with opion to manually edit.
	notes = models.CharField(max_length=100000)


	def __unicode__(self):
		return self.task

	def is_done(self):
		return self.done_date<=timezone.now()
	is_done.admin_order_field='task'
	is_done.boolean=True
	is_done.short_description = 'Completed?'
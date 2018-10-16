import datetime
from django.contrib import admin
from .models import Logging

#try create own filter
class OwnFilterForDate(admin.SimpleListFilter):
	"""
	Class with own filter option.
	Human-readable title which will be displayed in the 
	right admin sidebar just above the filter options.
	"""
	title = 'За Датою: '
	parameter_name = 'date'


	def lookups(self, request, model_admin):
		"""
		Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
		"""
		return(
			('today', 'За останній день'),
			('twoday', 'За останні два дні'),
			('threeday', 'За останні тр дні')
			)

	def queryset(self, request, queryset):
		"""
		Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.

		"""
		currentdate = datetime.datetime.today()
		now = currentdate.combine(currentdate.date(), currentdate.min.time())
		delta = datetime.timedelta(days=1)
		if self.value() == 'today':
			return queryset.filter(\
				date__gte=now, \
				date__lte=(now + delta)\
				)
		if self.value() == 'twoday':
			return queryset.filter(\
				date__gte=now - delta, \
				date__lte=now + delta\
				)
		if self.value() == 'threeday':
			return queryset.filter(\
				date__gte=now - delta*2, \
				date__lte=now + delta\
				) 

# Register your models here.
class LoggingAdmin(admin.ModelAdmin):
    list_display = ['ip', 'referrer', 'date',]
    list_filter = [OwnFilterForDate, ]


admin.site.register(Logging, LoggingAdmin)


from django.contrib import admin

# Register your models here.
from journal.models import Entry, Skill


admin.site.register(Skill)
admin.site.register(Entry)

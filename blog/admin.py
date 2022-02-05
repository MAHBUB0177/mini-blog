from django.contrib import admin

# Register your models here.
from.models import*
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
  list_display=("id","title","Desc")
admin.site.register(Document)
admin.site.register(Student)


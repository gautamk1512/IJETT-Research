from django.contrib import admin
from .models import Paper, CoAuthor, ArchiveIssue, ArchivePaper, LatestUpdate

# Register your models here.
admin.site.register(Paper)
admin.site.register(CoAuthor)
admin.site.register(ArchiveIssue)
admin.site.register(ArchivePaper)

@admin.register(LatestUpdate)
class LatestUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.site_header = "IJART – International Journal of Advanced Research in Technology Admin"
admin.site.site_title = "IJART Journal Admin Portal"
admin.site.index_title = "Welcome to the IJART Journal Administration Panel"
admin.site.site_url = "/"

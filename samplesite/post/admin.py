from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'content', 'time_of_creation', 
		            'publication_time', 'last_update', 'image')
	list_display_links = ('title', 'content')
	search_fields = ('title', 'content')
	ordering = ['-publication_time']


admin.site.register(Post, PostAdmin)

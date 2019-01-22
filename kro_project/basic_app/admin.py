from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
	list_filter = ('category', 'title', 'date')
	search_fields = ['title']
	date_hierarchy = 'date'
admin.site.register(Post, PostAdmin)	



#admin.site.register(Category)
#admin.site.register(Post)

#Jak widać, importujemy (dołączamy) model Post, który zdefiniowałyśmy w poprzednim rozdziale. Aby nasz model był widoczny w panelu admina, musimy go zarejestrować za pomocą polecenia admin.site.register(Post).


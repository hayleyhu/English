from django.contrib import admin
from .models import Post
from .models import Table
from .models import Member

admin.site.register(Post)
admin.site.register(Table)
admin.site.register(Member)


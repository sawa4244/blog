from django.contrib import admin
from .models import Post
from myblog.models import myblog, comments


class article_Inline(admin.StackedInline):
    model = comments
    extra = 2 # кол-во дефолтных комментов для ввода


class article_admin(admin.ModelAdmin):
    fields = ['article_text', 'article_date', 'article_title'] # высвечивается для админа
    inlines = [article_Inline]
    list_filter = ['article_date']    # фильтрация статей


admin.site.register(Post)
admin.site.register(myblog, article_admin)

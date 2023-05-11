from django.contrib import admin
from .models import Post,Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','content')
    #list_edit = ('content',)
    list_filter = ('created_at',)
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다'
    inlines = [CommentInline]



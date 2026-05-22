from django.contrib import admin
from .models import Course, Student, Comment
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.site_header="Fn40"
admin.site.site_title="fn40"
admin.site.login_template="admin/login.html"
admin.site.logout_template="admin/logout.html"

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2
    readonly_fields = ('user',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone_number', 'get_image')
    list_display_links = ('address',)
    inlines = [CommentInline]

    def get_image(self, student):
        if student.image:
            return mark_safe(f' <img src="{student.image.url}">')
        else:
            return '-'
    get_image.short_description = 'Rasm'

    @admin.display(boolean=True)
    def my_test_funk(self, obj):
        return True


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at')
    list_display_links = ('name',)
    list_filter = ('created_at',)
    list_editable = ('price',)
    search_fields = ('name', 'price')
    # fields = (
    # ('name', 'price'),
    # ('description',),
    # )
    fieldsets = [
        (
            None,
            {'fields':['name', 'price']}
        ),
        (
            'tavsif',
            {
                'fields':['description'],
                'classes':['collapse'],
                'description':'Bu yerda tavsiflar yoziladi'
            }
        )
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)

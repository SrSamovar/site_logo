from django.contrib import admin

from .models import Teacher, Child, ChildClub, Club


class ChildClubInline(admin.TabularInline):
    model = ChildClub
    extra = 0


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'first_name', 'last_name', 'work_experience', 'work_position',]
    list_filter = ['surname', 'work_position']
    inlines = [ChildClubInline]


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'first_name', 'last_name', 'age']
    list_filter = ['surname', 'age']


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description', 'price']
    list_filter = ['name']



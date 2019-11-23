import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource

class GlobalSettings:
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'

class BaseSettings:
    enable_themes = True
    use_bootswatch = True

class CourseAdmin:
    list_display = ['desc', 'name', 'detail', 'degree', 'learn_times', 'students']
    search_fields = ['desc', 'name', 'detail', 'degree', 'students']
    list_filter = ['desc', 'name', 'teacher__name', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ['degree', 'desc']

class LessonAdmin:
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin:
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin:
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
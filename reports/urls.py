from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'add-report/',
        views.add_report,
        name='add_report'
    ),

    path(
        'reports/',
        views.report_list,
        name='report_list'
    ),

    path(
        'edit-report/<int:report_id>/',
        views.edit_report,
        name='edit_report'
    ),

    path(
        'delete-report/<int:report_id>/',
        views.delete_report,
        name='delete_report'
    ),
    path(
    'logout/',
    views.logout_view,
    name='logout'
),

]
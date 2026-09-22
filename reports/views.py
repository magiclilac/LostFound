from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReportForm
from .models import Report


def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            if user.is_superuser:

                login(request, user)

                return redirect('dashboard')

            form.add_error(
                None,
                'Only the authorized Admin can login.'
            )

    else:

        form = AuthenticationForm()

    return render(
        request,
        'reports/login.html',
        {'form': form}
    )


@login_required
def dashboard(request):

    total_reports = Report.objects.count()

    lost_items = Report.objects.filter(
        report_type='Lost'
    ).count()

    found_items = Report.objects.filter(
        report_type='Found'
    ).count()

    open_items = Report.objects.filter(
        status='Open'
    ).count()

    returned_items = Report.objects.filter(
        status='Returned'
    ).count()

    context = {
        'total_reports': total_reports,
        'lost_items': lost_items,
        'found_items': found_items,
        'open_items': open_items,
        'returned_items': returned_items,
    }

    return render(
        request,
        'reports/dashboard.html',
        context
    )


@login_required
def add_report(request):

    if request.method == 'POST':

        form = ReportForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('report_list')

    else:

        form = ReportForm()

    return render(
        request,
        'reports/add_report.html',
        {'form': form}
    )


@login_required
def report_list(request):

    reports = Report.objects.all().order_by('-created_at')

    return render(
        request,
        'reports/report_list.html',
        {'reports': reports}
    )


@login_required
def edit_report(request, report_id):

    report = get_object_or_404(
        Report,
        id=report_id
    )

    if request.method == 'POST':

        form = ReportForm(
            request.POST,
            instance=report
        )

        if form.is_valid():

            form.save()

            return redirect('report_list')

    else:

        form = ReportForm(
            instance=report
        )

    return render(
        request,
        'reports/edit_report.html',
        {'form': form, 'report': report}
    )


@login_required
def delete_report(request, report_id):

    report = get_object_or_404(
        Report,
        id=report_id
    )

    if request.method == 'POST':

        report.delete()

        return redirect('report_list')

    return render(
        request,
        'reports/delete_report.html',
        {'report': report}
    )
def logout_view(request):

    logout(request)

    return redirect('login')
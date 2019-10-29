# -*- coding: utf-8 -*-

from datetime import datetime
from http import HTTPStatus

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateView
from django.views.generic.base import View

from django_comments.models import Comment

from tcms.core.utils import clean_request
from tcms.management.models import Priority, Tag
from tcms.testcases.models import TestCasePlan, TestCaseStatus, BugSystem
from tcms.testcases.views import get_selected_testcases
from tcms.testplans.models import TestPlan
from tcms.testruns.data import TestExecutionDataMixin
from tcms.testruns.forms import NewRunForm, SearchRunForm, BaseRunForm
from tcms.testruns.models import TestRun, TestExecution, TestExecutionStatus
from tcms.core.contrib.linkreference.models import LinkReference


User = get_user_model()  # pylint: disable=invalid-name


@method_decorator(permission_required('testruns.add_testrun'), name='dispatch')
class CreateTestRunView(View):
    """Display the create test run page."""

    template_name = 'testruns/mutable.html'
    http_method_names = ['post']

    def post(self, request):
        # If from_plan does not exist will redirect to plans for select a plan
        plan_id = request.POST.get('from_plan')
        if not plan_id:
            messages.add_message(request,
                                 messages.ERROR,
                                 _('Creating a TestRun requires a TestPlan, select one'))
            return HttpResponseRedirect(reverse('plans-search'))

        if not request.POST.get('case'):
            messages.add_message(request,
                                 messages.ERROR,
                                 _('Creating a TestRun requires at least one TestCase'))
            return HttpResponseRedirect(reverse('test_plan_url_short', args=[plan_id]))

        # Ready to write cases to test plan
        test_cases = get_selected_testcases(request)
        test_plan = TestPlan.objects.get(plan_id=plan_id)

        # note: ordered by case_id for test_show_create_new_run_page()
        tcs_values = test_cases.select_related('author',
                                               'case_status',
                                               'category',
                                               'priority').order_by('case_id')

        if request.POST.get('POSTING_TO_CREATE'):
            form = NewRunForm(request.POST)
            form.populate(product_id=test_plan.product_id)

            if form.is_valid():
                # Process the data in form.cleaned_data
                default_tester = form.cleaned_data['default_tester']

                test_run = TestRun.objects.create(
                    product_version=test_plan.product_version,
                    stop_date=None,
                    summary=form.cleaned_data.get('summary'),
                    notes=form.cleaned_data.get('notes'),
                    plan=test_plan,
                    build=form.cleaned_data['build'],
                    manager=form.cleaned_data['manager'],
                    default_tester=default_tester,
                )

                loop = 1
                for case in form.cleaned_data['case']:
                    try:
                        tcp = TestCasePlan.objects.get(plan=test_plan, case=case)
                        sortkey = tcp.sortkey
                    except ObjectDoesNotExist:
                        sortkey = loop * 10

                    test_run.add_case_run(case=case, sortkey=sortkey,
                                          assignee=default_tester)
                    loop += 1

                return HttpResponseRedirect(
                    reverse('testruns-get', args=[test_run.run_id, ])
                )

        else:
            form = NewRunForm(initial={
                'summary': 'Test run for %s' % test_plan.name,
                'manager': test_plan.author.email,
                'default_tester': request.user.email,
                'notes': '',
            })
            form.populate(product_id=test_plan.product_id)

        context_data = {
            'test_plan': test_plan,
            'test_cases': tcs_values,
            'form': form,
        }
        return render(request, self.template_name, context_data)


class SearchTestRunView(TemplateView):  # pylint: disable=missing-permission-required

    template_name = 'testruns/search.html'

    def get_context_data(self, **kwargs):
        form = SearchRunForm(self.request.GET)
        form.populate(product_id=self.request.GET.get('product'))

        return {
            'form': form,
        }


def _open_run_get_executions(request, run):  # pylint: disable=missing-permission-required
    """Prepare for executions list in a TestRun page

    This is an internal method. Do not call this directly.
    """

    executions = run.case_run.select_related(
        'run', 'case'
    ).only('run__run_id',
           'run__plan',
           'status',
           'assignee',
           'tested_by',
           'case_text_version',
           'sortkey',
           'case__summary',
           'case__is_automated',
           'case__priority',
           'case__category__name'
           )

    # Continue to search the executionss with conditions
    # 4. executions preparing for render executions table
    executions = executions.filter(**clean_request(request))
    order_by = request.GET.get('order_by')
    if order_by:
        return executions.order_by(order_by)

    return executions.order_by('sortkey', 'pk')


def open_run_get_comments_subtotal(case_run_ids):
    content_type = ContentType.objects.get_for_model(TestExecution)
    query_set = Comment.objects.filter(
        content_type=content_type,
        site_id=settings.SITE_ID,
        object_pk__in=case_run_ids,
        is_removed=False).values('object_pk').annotate(comment_count=Count('pk')).order_by(
            'object_pk')

    result = ((int(row['object_pk']), row['comment_count']) for row in query_set)
    return dict(result)


def open_run_get_users(case_runs):
    tester_ids = set()
    assignee_ids = set()
    for case_run in case_runs:
        if case_run.tested_by_id:
            tester_ids.add(case_run.tested_by_id)
        if case_run.assignee_id:
            assignee_ids.add(case_run.assignee_id)
    testers = User.objects.filter(
        pk__in=tester_ids).values_list('pk', 'username')
    assignees = User.objects.filter(
        pk__in=assignee_ids).values_list('pk', 'username')
    return (dict(testers.iterator()), dict(assignees.iterator()))


class GetTestRunView(TemplateView):  # pylint: disable=missing-permission-required
    """Display testrun's details"""

    template_name = 'run/get.html'

    def get_context_data(self, **kwargs):
        # Get the test run
        try:
            # 1. get test run itself
            test_run = TestRun.objects.select_related().get(run_id=kwargs['run_id'])
        except ObjectDoesNotExist:
            raise Http404

        # Get the test executions that belong to the run
        # 2. get test run's all executions
        test_executions = _open_run_get_executions(self.request, test_run)

        status = TestExecutionStatus.objects.only('pk', 'name').order_by('pk')

        # Count the status
        # 3. calculate number of executions of each status
        status_stats_result = test_run.stats_executions_status(status)

        # Get the test execution bugs summary
        # 6. get the number of bugs of this run
        execution_bugs_count = test_run.get_bug_count()

        return {
            'test_run': test_run,
            'executions': _walk_executions(test_executions),
            'executions_count': len(test_executions),
            'status_stats': status_stats_result,
            'execution_bugs_count': execution_bugs_count,
            'test_status': status,
            'priorities': Priority.objects.filter(is_active=True),
            'case_own_tags': _get_tags(test_executions),
            'bug_trackers': BugSystem.objects.all(),
        }


def _get_tags(test_executions):
    """Get tag list of testcases"""

    # Get the list of testcases belong to the run
    test_cases = []
    for test_execution in test_executions:
        test_cases.append(test_execution.case_id)

    tags = Tag.objects.filter(case__in=test_cases).values_list('name', flat=True)
    tags = list(set(tags))
    tags.sort()

    return tags


def _walk_executions(test_executions):
    """Walking executions for helping rendering executions table"""

    priorities = dict(Priority.objects.values_list('pk', 'value'))
    testers, assignees = open_run_get_users(test_executions)
    execution_pks = []
    for execution in test_executions:
        execution_pks.append(execution.pk)
    comments_subtotal = open_run_get_comments_subtotal(execution_pks)
    status = TestExecutionStatus.get_names()

    for execution in test_executions:
        yield (execution,
               testers.get(execution.tested_by_id, None),
               assignees.get(execution.assignee_id, None),
               priorities.get(execution.case.priority_id),
               status[execution.status_id],
               comments_subtotal.get(execution.pk, 0),
               LinkReference.objects.filter(is_defect=True,
                                            execution=execution.pk).count())


@permission_required('testruns.change_testrun')
def edit(request, run_id):
    """Edit test plan view"""

    try:
        test_run = TestRun.objects.select_related().get(run_id=run_id)
    except ObjectDoesNotExist:
        raise Http404

    # If the form is submitted
    if request.method == "POST":
        form = BaseRunForm(request.POST)
        form.populate(product_id=test_run.plan.product_id)

        # FIXME: Error handler
        if form.is_valid():
            test_run.summary = form.cleaned_data['summary']
            # Permission hack
            if test_run.manager == request.user or test_run.plan.author == request.user:
                test_run.manager = form.cleaned_data['manager']
            test_run.default_tester = form.cleaned_data['default_tester']
            test_run.build = form.cleaned_data['build']
            test_run.product_version = test_run.plan.product_version
            test_run.notes = form.cleaned_data['notes']
            test_run.save()

            return HttpResponseRedirect(reverse('testruns-get', args=[run_id, ]))
    else:
        # Generate a blank form
        form = BaseRunForm(initial={
            'summary': test_run.summary,
            'manager': test_run.manager.email,
            'default_tester': (test_run.default_tester and
                               test_run.default_tester.email or None),
            'version': test_run.product_version_id,
            'build': test_run.build_id,
            'notes': test_run.notes,
        })
        form.populate(test_run.plan.product_id)

    context_data = {
        'test_run': test_run,
        'test_plan': test_run.plan,
        'form': form,
    }
    return render(request, 'testruns/mutable.html', context_data)


class TestRunReportView(TemplateView,  # pylint: disable=missing-permission-required
                        TestExecutionDataMixin):
    """Test Run report"""

    template_name = 'run/report.html'

    def get_context_data(self, **kwargs):
        """Generate report for specific TestRun

        There are four data source to generate this report.
        1. TestRun
        2. Test executions included in the TestRun
        3. Comments associated with each test execution
        4. Statistics
        5. bugs
        """
        run = TestRun.objects.select_related('manager', 'plan').get(pk=kwargs['run_id'])

        case_runs = TestExecution.objects.filter(
            run=run
        ).select_related(
            'status', 'case', 'tested_by'
        ).only(
            'close_date',
            'status__name',
            'case__category__name',
            'case__summary', 'case__is_automated',
            'tested_by__username'
        )
        mode_stats = self.stats_mode_executions(case_runs)
        summary_stats = self.get_summary_stats(case_runs)

        comments = self.get_execution_comments(run.pk)
        for case_run in case_runs:
            case_run.user_comments = comments.get(case_run.pk, [])

        context = super().get_context_data(**kwargs)
        context.update({
            'test_run': run,
            'executions': case_runs,
            'executions_count': len(case_runs),
            'mode_stats': mode_stats,
            'summary_stats': summary_stats,
        })

        return context


@method_decorator(permission_required('testruns.add_testrun'), name='dispatch')
class CloneTestRunView(View):
    """Clone cases from filter caserun"""

    template_name = 'testruns/mutable.html'
    http_method_names = ['post']

    def post(self, request, run_id):
        test_run = get_object_or_404(TestRun, run_id=run_id)
        confirmed_case_status = TestCaseStatus.get_confirmed()
        disabled_cases = 0

        if request.POST.get('case_run'):
            test_cases = []
            for test_case_run in test_run.case_run.filter(pk__in=request.POST.getlist('case_run')):
                if test_case_run.case.case_status == confirmed_case_status:
                    test_cases.append(test_case_run.case)
                else:
                    disabled_cases += 1
        else:
            test_cases = None

        if not test_cases:
            messages.add_message(request,
                                 messages.ERROR,
                                 _('At least one TestCase is required'))
            return HttpResponseRedirect(reverse('testruns-get', args=[run_id]))

        form = NewRunForm(initial={
            'summary': _('Clone of ') + test_run.summary,
            'notes': test_run.notes,
            'manager': test_run.manager,
            'build': test_run.build_id,
            'default_tester': test_run.default_tester,
        })
        form.populate(product_id=test_run.plan.product_id)

        context_data = {
            'is_cloning': True,
            'disabled_cases': disabled_cases,
            'test_plan': test_run.plan,
            'test_cases': test_cases,
            'form': form,
        }
        return render(request, self.template_name, context_data)


@method_decorator(permission_required('testruns.change_testrun'), name='dispatch')
class ChangeTestRunStatusView(View):
    """Change test run finished or running"""

    http_method_names = ['get']

    def get(self, request, run_id):
        test_run = get_object_or_404(TestRun, run_id=run_id)

        test_run.update_completion_status(request.GET.get('finished') == '1')
        test_run.save()

        return HttpResponseRedirect(reverse('testruns-get', args=[run_id, ]))


@method_decorator(permission_required('testruns.add_testexecution'), name='dispatch')
class AddCasesToRunView(View):
    """Add cases to a TestRun"""

    def post(self, request, run_id):
        # Selected cases' ids to add to run
        test_cases_ids = request.POST.getlist('case')
        if not test_cases_ids:
            # user clicked Update button without selecting new Test Cases
            # to be dded to TestRun
            messages.add_message(request,
                                 messages.ERROR,
                                 _('At least one TestCase is required'))
            return HttpResponseRedirect(reverse('add-cases-to-run', args=[run_id]))

        try:
            test_cases_ids = list(map(int, test_cases_ids))
        except (ValueError, TypeError):
            # this will happen only on malicious requests
            messages.add_message(request,
                                 messages.ERROR,
                                 _('TestCase ID is not a valid integer'))
            return HttpResponseRedirect(reverse('add-cases-to-run', args=[run_id]))

        try:
            test_run = TestRun.objects.select_related('plan').only('plan__plan_id').get(
                run_id=run_id)
        except ObjectDoesNotExist:
            raise Http404

        executions_ids = test_run.case_run.values_list('case', flat=True)

        # avoid add cases that are already in current run with pk run_id
        test_cases_ids = set(test_cases_ids) - set(executions_ids)

        test_plan = test_run.plan
        test_cases = test_run.plan.case.filter(case_status__name='CONFIRMED').select_related(
            'default_tester').only('default_tester_id').filter(
                case_id__in=test_cases_ids)

        if request.POST.get('_use_plan_sortkey'):
            test_case_pks = (test_case.pk for test_case in test_cases)
            query_set = TestCasePlan.objects.filter(
                plan=test_plan, case__in=test_case_pks).values('case', 'sortkey')
            sort_keys_in_plan = dict((row['case'], row['sortkey']) for row in query_set.iterator())
            for test_case in test_cases:
                sort_key = sort_keys_in_plan.get(test_case.pk, 0)
                test_run.add_case_run(case=test_case, sortkey=sort_key)
        else:
            for test_case in test_cases:
                test_run.add_case_run(case=test_case)

        return HttpResponseRedirect(reverse('testruns-get',
                                            args=[test_run.run_id, ]))

    def get(self, request, run_id):
        # information about TestRun, used in the page header
        test_run = TestRun.objects.select_related(
            'plan', 'manager', 'build'
        ).only(
            'plan', 'plan__name',
            'manager__email', 'build__name'
        ).get(run_id=run_id)

        # select all CONFIRMED cases from the TestPlan that is a parent
        # of this particular TestRun
        rows = TestCasePlan.objects.values(
            'case',
            'case__create_date', 'case__summary',
            'case__category__name',
            'case__priority__value',
            'case__author__username'
        ).filter(
            plan_id=test_run.plan,
            case__case_status=TestCaseStatus.objects.filter(name='CONFIRMED').first().pk
        ).order_by('case')  # order b/c of PostgreSQL

        # also grab a list of all TestCase IDs which are already present in the
        # current TestRun so we can mark them as disabled and not allow them to
        # be selected
        executions = TestExecution.objects.filter(run=run_id).values_list('case', flat=True)

        data = {
            'test_run': test_run,
            'confirmed_cases': rows,
            'confirmed_cases_count': rows.count(),
            'executions_count': len(executions),
            'exist_case_run_ids': executions,
        }

        return render(request, 'run/assign_case.html', data)


# todo: this view should be removed in favor of API
@method_decorator(permission_required('testruns.change_testrun'), name='dispatch')
class ManageTestRunCC(View):
    """Add or remove cc from a test run"""

    template_name = 'run/get_cc.html'
    http_method_names = ['get']

    def get(self, request, run_id):
        test_run = get_object_or_404(TestRun, run_id=run_id)
        action = request.GET.get('do')
        username_or_email = request.GET.get('user')
        context_data = {'test_run': test_run, 'is_ajax': True}

        try:
            user = User.objects.get(
                Q(username=username_or_email) |
                Q(email=username_or_email)
            )
            context_data['message'] = ''
        except ObjectDoesNotExist:
            context_data['message'] = _('The user you typed does not exist in database')
            return render(request, self.template_name, context_data)

        if action == 'add':
            test_run.add_cc(user=user)
        elif action == 'remove':
            test_run.remove_cc(user=user)

        return render(request, self.template_name, context_data)


@method_decorator(permission_required('testruns.change_testexecution'), name='dispatch')
class UpdateCaseRunTextView(View):
    """Update the IDLE cases to newest text"""

    http_method_names = ['post']

    def post(self, request, run_id):
        test_run = get_object_or_404(TestRun, run_id=run_id)

        if request.POST.get('case_run'):
            executions = test_run.case_run.filter(pk__in=request.POST.getlist('case_run'))
        else:
            executions = test_run.case_run.all()

        executions = executions.filter(status__name='IDLE')

        for execution in executions:
            latest_version = execution.case.history.latest().history_id
            if execution.case_text_version != latest_version:
                info = "%s: %s -> %s" % (
                    execution.case.summary,
                    execution.case_text_version,
                    latest_version
                )
                messages.add_message(request, messages.SUCCESS, info)

                execution.case_text_version = latest_version
                execution.save()

        return HttpResponseRedirect(reverse('testruns-get', args=[run_id]))


def get_caseruns_of_runs(runs, kwargs=None):
    """
    Filtering argument -
        priority
        tester
        plan tag
    """

    if kwargs is None:
        kwargs = {}
    plan_tag = kwargs.get('plan_tag', None)
    if plan_tag:
        runs = runs.filter(plan__tag__name=plan_tag)
    caseruns = TestExecution.objects.filter(run__in=runs)
    priority = kwargs.get('priority', None)
    if priority:
        caseruns = caseruns.filter(case__priority__pk=priority)
    tester = kwargs.get('tester', None)
    if not tester:
        caseruns = caseruns.filter(tested_by=None)
    if tester:
        caseruns = caseruns.filter(tested_by__pk=tester)
    status = kwargs.get('status', None)
    if status:
        caseruns = caseruns.filter(status__name__iexact=status)
    return caseruns


@method_decorator(permission_required('testruns.change_testexecution'), name='dispatch')
class UpdateAssigneeView(View):
    """Updates TestExecution.assignee. Called from the front-end."""

    http_method_names = ['post']

    def post(self, request):
        assignee = request.POST.get('assignee')
        try:
            user = User.objects.get(username=assignee)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=assignee)
            except User.DoesNotExist:
                return JsonResponse({'rc': 1,
                                     'response': _('User %s not found!') % assignee},
                                    status=HTTPStatus.NOT_FOUND)

        object_ids = request.POST.getlist('ids[]')

        for caserun_pk in object_ids:
            execution = get_object_or_404(TestExecution, pk=int(caserun_pk))
            execution.assignee = user
            execution.save()

        return JsonResponse({'rc': 0, 'response': 'ok'})


@method_decorator(permission_required('testruns.change_testexecution'), name='dispatch')
class UpdateCaseRunStatusView(View):
    """Updates TestExecution.status_id. Called from the front-end."""

    http_method_names = ['post']

    def post(self, request):
        status_id = int(request.POST.get('status_id'))
        object_ids = request.POST.getlist('object_pk[]')

        for caserun_pk in object_ids:
            execution = get_object_or_404(TestExecution, pk=int(caserun_pk))
            execution.status_id = status_id
            execution.tested_by = request.user
            execution.close_date = datetime.now()
            execution.save()

        return JsonResponse({'rc': 0, 'response': 'ok'})

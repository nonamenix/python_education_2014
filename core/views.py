import json
from django.http import HttpResponse
from django.utils import translation
from .forms import DeveloperForm, UserForm
from .models import Developer, User


def create_api_user(request):
    translation.activate('en')
    _user_form = DeveloperForm(data=request.GET)

    context = {}
    if _user_form.is_valid():
        user = _user_form.save()
        context.update({
            'username': user.username,
            'code': user.code
        })
    else:
        errors = dict(_user_form.errors)
        context.update({'errors': errors})
    translation.deactivate()
    return HttpResponse(content=json.dumps(context), content_type='application/json')


def create_user(request):
    translation.activate('en')
    _user_form = UserForm(data=request.GET)
    try:
        _code = dict(request.GET.iteritems()).pop('code')
    except KeyError:
        return HttpResponse(
            content=json.dumps(
                {'errors': ['You should take developer code from /developer/create/?username=YOURNAME', ]}),
            content_type='application/json')

    context = {}
    if _user_form.is_valid():
        created_by = Developer.objects.get(code=_code).pk
        user = _user_form.save(commit=False)
        user.created_by_id = created_by

        user.save()

        count = User.objects.filter(created_by=created_by).count()

        context.update({
            'username': user.username,
            'first_name': user.first_name,
            'second_name': user.second_name,
            'pk': user.pk,
            'created_at': user.created_at.strftime('%Y.%m.%d %H:%M:%S'),
            'count': count,
            'success': count >= 100
        })
    else:
        context.update({'errors': dict(_user_form.errors)})
    translation.deactivate()
    return HttpResponse(content=json.dumps(context), content_type='application/json')


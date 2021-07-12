from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Content


def index(request):
    context = dict()
    context['data'] = {}
    contents = Content.objects.all()
    for c in contents:
        context['data'][c.id] = c.content
    return render(request, 'index.html', context)


@csrf_exempt
@login_required
def update_text(request):
    cid = request.POST['cid']
    content = request.POST['content']

    m_content = Content.objects.filter(pk=cid).first()
    if m_content:
       m_content.content = content
       m_content.last_modified_by = request.user
    else:
        m_content = Content(id=cid, content=content)
        m_content.last_modified_by = request.user
    m_content.save()
    return JsonResponse({'status': 'ok'})

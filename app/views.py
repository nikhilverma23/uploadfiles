# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from uploadtext.app.models import Uploadtext
from uploadtext.app.forms import Documentform
from django.core.urlresolvers import reverse
import operator


def list(request):
    if request.method == 'POST':
        form = Documentform(request.POST, request.FILES)
        if form.is_valid():
            doc = Uploadtext(file=request.FILES['textfile'])
            doc.save()
            return HttpResponseRedirect(reverse('app.views.list'))
    else:
        form = Documentform()
        if Uploadtext.objects.all():
            documents = Uploadtext.objects.all()
            dic = {}
            words = [word for lines in documents[0].file.readlines()\
            for word in lines.split()]
            for word in words:
                num = 0
                for otherwords in words:
                    if word == otherwords:
                        num += 1
                    dic[word] = num
            dic = sorted(dic.iteritems(), key=operator.itemgetter(1),
            reverse=True)
            dic = dic[:5]
            documents[0].delete()
    return render_to_response('render.html',
                              locals(),
                              context_instance=RequestContext(request)
                             )

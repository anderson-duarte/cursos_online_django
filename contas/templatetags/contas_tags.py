from django import template
from cursos.models import Inscricao

register = template.Library()

@register.inclusion_tag('contas/registros.html')
def inscricoes(user):
    inscricoes1 = Inscricao.objects.filter(user=user)
    context = {'cursos':inscricoes1}
    return context
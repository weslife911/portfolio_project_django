from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf.pisa import pisaDocument

def html2pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    else:
        return None
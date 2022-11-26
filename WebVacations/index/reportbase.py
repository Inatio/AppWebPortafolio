import os
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate


from WebVacations.settings import BASE_DIR2


times_new_roman = os.path.join(BASE_DIR2,'WebVacations', 'static', 'fonts', 'times_new_roman.ttf')
pdfmetrics.registerFont(TTFont("tnr", times_new_roman))
times_new_roman_bold = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'times_new_roman_bold.ttf')
pdfmetrics.registerFont(TTFont("tnr_bold", times_new_roman_bold))
arial = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'arial.ttf')
pdfmetrics.registerFont(TTFont("arial", arial))
poppins_regular = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'poppins', 'poppins_regular.ttf')
pdfmetrics.registerFont(TTFont("poppins", poppins_regular))
poppins_bold = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'poppins', 'poppins_bold.ttf')
pdfmetrics.registerFont(TTFont("poppins_bold", poppins_bold))


tahoma = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'tahoma', 'tahoma.ttf')
pdfmetrics.registerFont(TTFont("tahoma", tahoma))
tahoma_bold = os.path.join(BASE_DIR2, 'WebVacations', 'static', 'fonts', 'tahoma', 'tahoma_bold.ttf')
pdfmetrics.registerFont(TTFont("tahoma_bold", tahoma_bold))


class BaseFormatReport:
    def __init__(self, *args, **kwargs):
        pagesize = letter
        pagesize_kwargs = kwargs.get('pagesize', None)
        landscape_kwargs = kwargs.get('landscape', False)
        if pagesize_kwargs:
            pagesize = pagesize_kwargs
        if landscape_kwargs:
            pagesize = landscape(pagesize)

        self.kwargs = kwargs
        self.buffer = BytesIO()
        self.Story = []
        self.estilos = getSampleStyleSheet()
        self.doc = SimpleDocTemplate(
            self.buffer,
            pagesize=pagesize,
        )

    def _file_name(self):
        return u'archivo.pdf'

    def generate_pdf(self, build=True):
        """
            Construir pdf
        :return:
        """
        if build:
            self.doc.filename = self._nombre_archivo()
        else:
            self.doc.title = self._nombre_archivo()

        self.doc.build(self.Story)

    def pdf_response(self):
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] =\
        #     u'attachment; filename="{}.pdf'.\
        #         format(self._file_name())
        self.generate_pdf(build=False)
        response.write(self.buffer.getvalue())
        self.buffer.close()
        return response

    def pdf_to_bytes(self):
        self.generate_pdf(build=False)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf

    def pdf_to_email(self, close_buffer=True):
        """
            with_close debe venir en False en el caso de que haya un metodo
            posterior que cierre el buffer. Por ejemplo, que se genere este
            método y despues se genere el método de pdf_response que ese cierra
            el buffer

        """
        self.generate_pdf(build=False)
        pdf = self.buffer.getvalue()
        if close_buffer:
            self.buffer.close()

        return pdf


    def get_last_x_y(self, data):
        """
            Método para obtener la última
            cordenada de x , y de una data de tabla
        """
        last_x = len(data[0])-1
        last_y = len(data)-1

        return (last_x, last_y,)

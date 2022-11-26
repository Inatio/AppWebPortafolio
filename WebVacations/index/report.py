import os
from django.utils import timezone
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter, landscape
from django.template.defaultfilters import date as _date
from django.contrib.humanize.templatetags.humanize import intcomma
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from django.utils.translation import gettext_lazy as _
from django.contrib.humanize.templatetags.humanize import intcomma


from index.reportbase import BaseFormatReport


TITLE1 = ParagraphStyle(
    name='Title1',
    textTransform='uppercase',
    fontName='tahoma_bold',
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
    spaceAfter=0,
    spaceShrinkage=8
)

TEXT_LEFT_TABLE = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma',
    fontSize=9,
    leading=12,
    spaceBefore=0,
    alignment=TA_LEFT
)

TEXT_RIGHT_TABLE = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma',
    fontSize=9,
    leading=12,
    spaceBefore=0,
    alignment=TA_RIGHT
)
TEXT_RIGHT_TABLE_BOLD = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma_bold',
    fontSize=8,
    leading=12,
    spaceBefore=0,
    alignment=TA_RIGHT
)
TEXT_LEFT_TABLE_BOLD = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma_bold',
    fontSize=8,
    leading=12,
    spaceBefore=0,
    alignment=TA_LEFT
)
TITLE_RIGHT_TABLE_BOLD = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma_bold',
    fontSize=8,
    leading=12,
    spaceBefore=0,
    alignment=TA_RIGHT
)
TITLE_CENTER_TABLE_BOLD = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma_bold',
    fontSize=13,
    leading=13,
    spaceBefore=10,
    alignment=TA_CENTER
)
TITLE_LEFT_TABLE_BOLD = ParagraphStyle(
    name='TextRightTable',
    fontName='tahoma_bold',
    fontSize=9,
    leading=12,
    spaceBefore=0,
    alignment=TA_LEFT
)

TEXT_CENTER_TABLE = ParagraphStyle(
    name='TextCenterTable',
    fontName='tahoma',
    fontSize=8,
    leading=12,
    spaceBefore=6,
    alignment=TA_CENTER
)

class ReservaPDF(BaseFormatReport):
    MAX_Y = 279*mm
    MAX_X = 216*mm
    CONTEXT = None

    def _file_name(self):
        name = u'reserva_cliente'
        return name

    def generate_pdf(self, build=True):
        self.CONTEXT = self.kwargs.get('reserva', None)
        if build:
            self.doc.filename = self._file_name()
        else:
            self.doc.title = self._file_name()

        self.doc.topMargin = 50*mm
        _onPage = self._page_header

        # self._table()
        self._body()
        self._body1()
        self._body2()
        self.doc.build(self.Story,
                    onFirstPage=_onPage,
                    onLaterPages=_onPage)

    def _page_header(self, canvas, doc):
        canvas.saveState()
        # self._print_desc_company(canvas, doc, 255*mm)
        self._print_actual_date(canvas, doc, 262*mm)
        self._print_title_doc(canvas, doc, 238*mm)
        # self._print_footer(canvas, doc, 10.5*mm)

        canvas.restoreState()

    def _print_num_folio(self, canvas, doc, y):
        start_folio = self.kwargs.get('start_folio')
        page = doc.page
        if start_folio is not None:
            page = page+start_folio-1
        numPag = str(f'N° Folio :  {page}')
        canvas.setFont('tahoma', 10)
        canvas.drawString(175*mm, y, numPag)
        return canvas, doc

    # FECHA Y NUMERO DE PAGINA EN ENCABEZADO
    def _print_actual_date(self, canvas, doc, y):
        pag_number = doc.page
        cd = timezone.now()
        data_table = []
        style_table = [('FONT', (0, 0), (-1, -1), 'tahoma', 8),]
        table_col_width = [9*mm, 3*mm, 25*mm]
        table_row_height = 2*[3*mm]
        data_table.append([
                'Fecha', ':', '%s/%s/%s'%(cd.day, cd.month, cd.year)
            ])
        data_table.append([
                'Página', ':', pag_number
            ])
        width = 40*mm
        height = 10*mm
        x = 178*mm
        
        f = Table(data_table,
                colWidths=table_col_width,
                rowHeights=table_row_height)
        f.wrapOn(canvas, width, height)
        f.setStyle(TableStyle(style_table))
        f.drawOn(canvas, x, y)
        return canvas, doc

    # ENCABEZADO CON DATOS DE LA EMPRESA
    def _print_desc_company(self, canvas, doc, y):
        company = self.kwargs.get('current_company', None)
        data_table = []
        style_table = [('FONT', (0, 0), (-1, -1), 'tahoma', 8),]
        table_col_width = [20*mm, 3*mm, 25*mm]
        table_row_height = 5*[3*mm]
        if company is not None:
            data_table.append([
                'RAZÓN SOCIAL', ':', _if_none(company.name, "").upper()[0:25]
            ])
            data_table.append([
                'R.U.T', ':', _if_none(company.rut, "").upper()[0:25]
            ])
            data_table.append([
                'DIRECCIÓN', ':', _if_none(company.address, "").upper()[0:25]
            ])
            data_table.append([
                'COMUNA', ':', _if_none(company.commune.name, "").upper()[0:25]
            ])
            data_table.append([
                'GIRO', ':', _if_none(company.commercial_business, "").upper()[0:25]
            ])

            width = 50*mm
            height = 15*mm
            x = 8*mm
            f = Table(data_table,
                    colWidths=table_col_width,
                    rowHeights=table_row_height)

            f.wrapOn(canvas, width, height)
            f.setStyle(TableStyle(style_table))

            canvas.setFont('tahoma', 8)
            f.drawOn(canvas, x, y)
        return canvas, doc


    # TITULO DE DOCUMENTO
    def _print_title_doc(self, canvas, doc, y):
        reserva = self.kwargs.get('reserva', None)
        canvas.setFillColor(HexColor('#00945e'))
        canvas.setFont('tahoma_bold', 16)
        text = f'Reserva: {reserva.departamento.nombre_dpto}'
        #text_width = stringWidth(text, 'tahoma_bold', 13)
        canvas.drawString(10*mm, y, text)
        canvas.setFillColor(HexColor('#000000'))
        return canvas, doc

    # CUERPO DE LA TABLA
    def _body(self):
        data_table = []
        style_table = []
        reserva = self.kwargs.get('reserva', None)

        # PARTE 1
        data_table.append([
            Paragraph(str(f'Datos '), TITLE_CENTER_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Correo:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.usuario.correo, "")), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Cliente:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.usuario.nombre, "")), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Días:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(f'{reserva.dias} Días', "")), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Departamento:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.departamento.nombre_dpto, "")), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Region:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.departamento.id_comuna.id_region, "")), TEXT_LEFT_TABLE),
            Paragraph(str("Comuna:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.departamento.id_comuna, "")), TEXT_LEFT_TABLE),
        ])
        data_table.append([
            Paragraph(str("Tour:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(_if_none(reserva.tour, "")), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])

        style_table.append(('VALIGN', (0, 0), (-1, -1), 'MIDDLE'))

        col_size = [40*mm, 70*mm, 47*mm, 39*mm]

        table = Table(
            data=data_table,
            colWidths=col_size,
            spaceBefore=15,
            spaceAfter=15,
        )
        table.setStyle(TableStyle(style_table))
        self.Story.append(table)

    def _body1(self):
        data_table = []
        style_table = []
        reserva = self.kwargs.get('reserva', None)
        valor_reserva = (reserva.dias * reserva.departamento.tarifa_diaria)
        valor_anticipo = (valor_reserva*0.30)
        valor_total_tour = (valor_anticipo+reserva.tour.valor)
        valo_total = (valor_reserva+reserva.tour.valor)

        data_table.append([
            Paragraph(str(f'Costos '), TITLE_CENTER_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str(f'Valor {reserva.tour.tipo_tour.descripcion}:'), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(reserva.tour.valor)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Valor Reserva Díario:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(reserva.departamento.tarifa_diaria)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str("Valor Anticipo Reserva:"), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(valor_anticipo)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str(f'Valor Reserva + {reserva.tour.tipo_tour.descripcion}:'), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(valor_total_tour)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str(f'Valor Reserva Total - {reserva.tour.tipo_tour.descripcion}:'), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(valor_reserva)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])
        data_table.append([
            Paragraph(str(f'Valor Reserva Total + {reserva.tour.tipo_tour.descripcion}:'), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(f'${intcomma(valo_total)}'), TEXT_LEFT_TABLE),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
            Paragraph(str(""), TITLE_LEFT_TABLE_BOLD),
        ])

        style_table.append(('VALIGN', (0, 0), (-1, -1), 'MIDDLE'))

        col_size = [40*mm, 70*mm, 47*mm, 39*mm]

        table = Table(
            data=data_table,
            colWidths=col_size,
            spaceBefore=20,
            spaceAfter=40,
        )
        table.setStyle(TableStyle(style_table))
        self.Story.append(table)

    def _body2(self):
        data_table = []
        style_table = []

        # PARTE 1
        data_table.append([
            Paragraph(str("Pagar el resto del valor una ves se realize la entrega de las llaves."), TEXT_LEFT_TABLE),
        ])
        data_table.append([
            Paragraph(str("Todo daño, ruido u molestias recibidas durante la estancia del cliente, se vera reflejado en un cobro adicional en su boleta."), TEXT_LEFT_TABLE),
        ])

        style_table.append(('VALIGN', (0, 0), (-1, -1), 'MIDDLE'))

        col_size = [196*mm]

        table = Table(
            data=data_table,
            colWidths=col_size,
            spaceBefore=20,
            spaceAfter=0,
        )
        table.setStyle(TableStyle(style_table))
        self.Story.append(table)


    #  # FOOTER
    # def _print_footer(self, canvas, doc, y):

    #     img_url = os.path.join(
    #         BASE_DIR, 'app', 'static',  'assets', 'img', 'brand',
    #             'logo_remu_report_footer.jpg')

    #     width = 48*mm
    #     height = 9*mm
    #     x = 10*mm
    #     canvas.drawImage(img_url, x, y, width, height)

    #     canvas.setFont('tahoma_bold', 9)
    #     canvas.drawString(181 * mm, y+3*mm,
    #                     'transtecnia.cl' )

    #     return canvas, doc


def _if_none(value, message_show):
    if value is None:
        return message_show
    else:
        return value

def clean_intcomma(value_with_intcomma):
    if value_with_intcomma == 0:
        return 0
    return int(value_with_intcomma.replace(".", ""))
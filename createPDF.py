fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")

from reportlab.platypus import Paragraph, Spacer, Table, Image

from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

report_title = Paragraph("My Fruit Basket", styles["h1"])

>>> report.build([report_title])

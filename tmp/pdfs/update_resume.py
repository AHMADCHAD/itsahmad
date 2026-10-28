from pathlib import Path
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject, TextStringObject
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, Color
source = Path(r'C:\Users\Ahmad\Downloads\Ahmad_Hassan_Resume_v3 (4).pdf')
out = Path('output/pdf/Ahmad_Hassan_Resume_SportsNova_Updated.pdf').resolve()
reader = PdfReader(str(source))
page = reader.pages[0]
stream = ContentStream(page.get_contents(), reader)
targets = ('Built SportsNova,', 'SportsNova - Court Booking App', 'Court booking app. Users pick a sports complex,', 'Laravel backend.', 'complex, court and time slot.', 'React Native \x01 Laravel \x01 REST API')
for i, (operands, operator) in enumerate(stream.operations):
    if operator == b'Tj' and operands and isinstance(operands[0], str):
        text = operands[0]
        if text == '2026' or any(text.startswith(t) for t in targets):
            operands[0] = TextStringObject('')
            for j in range(max(0, i-12), i):
                prev_operands, prev_operator = stream.operations[j]
                if prev_operator == b'Tj' and prev_operands and prev_operands[0] == '\x01':
                    prev_operands[0] = TextStringObject('')
page[NameObject('/Contents')] = stream
w, h = float(page.mediabox.width), float(page.mediabox.height)
mem = BytesIO(); c = canvas.Canvas(mem, pagesize=(w, h))
for top, bottom in [(244.0, 268.5), (554.0, 606.0)]:
    c.setFillColor(white); c.rect(36, h-bottom, w-72, bottom-top, stroke=0, fill=1)
ink = Color(0.13, 0.13, 0.13); c.setFillColor(ink); c.setFont('Helvetica', 8.6)
for baseline, text in [(h-255.7+1.5, 'Developing SportsNova, a React Native court booking app with Laravel. Players select a'), (h-267.0+1.5, 'sports complex, court and time slot in a 3-step booking flow.')]:
    c.circle(43.5, baseline+3.0, 1.05, stroke=0, fill=1); c.drawString(54.7, baseline, text)
c.setFont('Helvetica-Bold', 10.0); c.drawString(39.7, h-564.9+2.0, 'SportsNova - Court Booking App | In Development 2026')
c.setFont('Helvetica', 8.6)
c.drawString(39.7, h-577.1+1.5, 'React Native | Laravel | REST API')
for baseline, text in [(h-592.7+1.5, 'An in-development app for booking sports courts. Players choose a sports complex, court and time slot.'), (h-604.0+1.5, 'Being developed with React Native and a Laravel backend.')]:
    c.circle(43.5, baseline+3.0, 1.05, stroke=0, fill=1); c.drawString(54.7, baseline, text)
c.save(); mem.seek(0); page.merge_page(PdfReader(mem).pages[0])
writer=PdfWriter(); writer.append_pages_from_reader(reader); out.parent.mkdir(parents=True,exist_ok=True)
with out.open('wb') as f: writer.write(f)
print(out)

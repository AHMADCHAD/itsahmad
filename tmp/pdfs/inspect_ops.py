from pypdf import PdfReader
from pypdf.generic import ContentStream
p=PdfReader(r'C:\Users\Ahmad\Downloads\Ahmad_Hassan_Resume_v3 (4).pdf').pages[0]
cs=ContentStream(p.get_contents(), p.pdf)
for operands, op in cs.operations:
    if op in (b'BT',b'Tm',b'Td',b'Tj',b'TJ',b'Tf'):
        print(op,operands)

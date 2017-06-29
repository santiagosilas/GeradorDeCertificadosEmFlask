import os
from os.path import pardir
from docx import Document
from docx.shared import Pt

def create_certificate(template, curso, nomes):
    '''
    O template deve conter as palavras @nome e @curso
    '''
    print(template)
    if os.path.exists(template):
        document = Document(template)
        output_dir = os.path.join(os.path.split(template)[0], 'output')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for index, nome in enumerate(nomes):
            new_file = os.path.join(output_dir, '{0}.docx'.format(index))
            replace(document, '<curso>', curso.upper())
            replace(document, '<nome>', nome.upper())
            document.save(new_file)
    else:
        print('Template not found!')
    
def replace(document, search, replace):
        for paragraph in document.paragraphs:
            paragraph_text = paragraph.text
            if paragraph_text:
                if search in paragraph_text:
                    paragraph.text = paragraph_text.replace(search, replace)
                    font = paragraph.style.font
                    font.name = 'Arial'
                    font.size = Pt(18)

if __name__ == '__main__':
    path = 'C:\\temp\\template.docx'
    nomes = ['Fulano de Tal', "Maria Fulana"]
    curso = 'Curso de Corte e Costura'
    create_certificate(path, curso, nomes)
    print('done')
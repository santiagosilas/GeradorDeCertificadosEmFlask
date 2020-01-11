import os
from os.path import pardir
from docx import Document
from docx.shared import Pt

def create_certificate(template, nome, titulo):
    '''
    O template deve conter as palavras <nome> e <titulo>
    '''
    print(template)
    if os.path.exists(template):
        document = Document(template)
        output_dir = os.path.join(os.path.split(template)[0], 'output')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(nome, titulo)
        new_file = os.path.join(output_dir, '{0}.docx'.format(nome))
        replace(document, '<titulo>', titulo.upper())
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
    template = 'E:\\gdrive\\H-References\\H-References-Working\\EP_EXTENSAO\\2017\\PAPEX 2017\\2017-PROPYTHON\\2017-11-24 1 Encontro PyLadies\\declaracao.docx'
    pessoas = [
        ['Alice Feitosa Barbosa','PyLadies, Divas e ProPython'],
        ['Helen Abdala Rocha Ferreira','PyLadies, Divas e ProPython'],
        ['JOYCE QUINTINO ALVES', 'Chatterbots com Python'],
        ['JOSÉ WILLIAM VITORINO DE SOUZA', 'Introdução ao Tkinter'],
        ['IVYSON LUCAS DE LIMA SILVA', 'Introdução ao Kivy'],
        ['PEDRO MICHAEL DOS SANTOS SOARES', 'Python em 10 minutos']
        ]
    for nome, titulo in pessoas:
        create_certificate(template, nome, titulo)
    print('done')
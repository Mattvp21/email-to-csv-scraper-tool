import csv
import re
from requests_html import HTMLSession
import fitz
from reportlab.pdfgen.canvas import Canvas


print("███╗░░░███╗██╗░░░██╗██████╗░")
print("████╗░████║██║░░░██║██╔══██╗")
print("██╔████╔██║╚██╗░██╔╝██████╔╝")
print("██║╚██╔╝██║░╚████╔╝░██╔═══╝░")
print("██║░╚═╝░██║░░╚██╔╝░░██║░░░░░")

print('Welcome to Matts scrapper!!')
print('Select an option Below \n 1.Extract from a url \n 2. Extract from a PDF(Upload to the directory first)')
choice = int(input())
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    


def make_url_call():
    '''
    URL call
    '''
    url = input("Enter a webpage: ")
    try:
        session = HTMLSession()
        r = session.get(url)
        r.html.render()
        saveToFile(r)
    except ValueError:
        print('Womp womp')



def saveToFile(r):
    '''
    Saves to a CSV
    '''
    with open('emails.csv', 'w', encoding='UTF8') as csvfile:
        for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
            new_file = csv.writer(csvfile)
            new_file.writerow([re_match.group()])
            print(re_match.group())

def load_from_pdf():
    l = input("Enter your PDF: ")
    
    doc = fitz.open(l)
    for page in doc:
        text = page.get_text()
        x = re.search(EMAIL_REGEX, text)
        try:
            print(x.group())
        except AttributeError:
            break

if choice == 1:
    make_url_call()
elif choice == 2:
    load_from_pdf()
else:
    print('Not a valid choice')
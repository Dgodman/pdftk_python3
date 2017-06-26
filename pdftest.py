from PyPDF2 import PdfFileReader
import pypdftk


def printFields (_sFileName):
    # open pdf
    with open(_sFileName, 'rb') as pdfFileObj:
        # read pdf
        pdfReader = PdfFileReader(pdfFileObj)
        # get pdf fields
        fields = pdfReader.getFields()
        # print fields
        for key, value in fields.iteritems():
            print (key, value)


def updateNew (_sFilename, _sNewFilename, _data):
    pypdftk.fill_form(_sFilename, _data, _sNewFilename)


fields_old = {
    'First Name': 'Max',
    'Middle Name': 'Danger',
    'Last Name': 'Power',
}
fields_new = {
    'first_name': 'Max',
    'middle_name': 'Danger',
    'last_name': 'Power',
    'hospital_yes': 'Yes',
    'county': 'Wake',
    'lived30_yes': 'Yes',
    'election_type': 'Statewide General Election',
    'election_date': '11 / 11 / 16'
}

#printFields('absentee.pdf')
updateNew("absentee.pdf", "absentee_new.pdf", fields_new)
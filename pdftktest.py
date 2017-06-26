import pypdftk


fields = {
    'First Name': 'Max',
    'Middle Name': 'Danger',
    'Last Name': 'Powers'
}

generated_pdf = pypdftk.fill_form("absentee.pdf", fields, "absentee_new.pdf")
#out_pdf = pypdftk.concat(['/path/to/cover.pdf', generated_pdf])
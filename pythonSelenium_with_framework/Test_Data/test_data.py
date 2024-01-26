import openpyxl
book = openpyxl.load_workbook("C:\\Users\\Lenovo\\PycharmProjects\\pythonSelenium_with_framework\\Test_Data\\Excel_data.xlsx")    #importing excel file
sheet = book.active

class testData:

    page_data=[{'mobileName':'Samsung Note 8','entered_country_name':'ind','country_presence':'India'}]
    #page_data=[]
    #page_data = sheet.cell(row=1, column=2)
    #print(page_data.value)
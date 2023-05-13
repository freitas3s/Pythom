import os 
import win32com as client

excel = client.dispatch('excel.application')

for file in os.listdir(os.getcwd() + ""):
    filename, fileextension=os.path.splittext(file)
    wb=excel.workbooks.Open(os.getcwd()+"pasta dos arquivos xls"+ file)
    saida=os.getcwd()+ "pasta de saida" + filename
    wb.SaveAs(saida,51)
    wb.Close()
excel.Quit()
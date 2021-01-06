import ezsheets
ss = ezsheets.upload('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg') #uploads the google sheet

ss.downloadAsCSV() #downloads as a CSV file locally
ss.downloadAsExcel() #downloads as an excel sheet locally
ss.downloadAsPDF() #downloads as a PDF locally
ss.downloadAsODS() #downloads as a ODS file locally
ss.downloadAsHTML() #downloads as a HTML file locally
ss.downloadAsTSV() #downloads as a TSV file locally


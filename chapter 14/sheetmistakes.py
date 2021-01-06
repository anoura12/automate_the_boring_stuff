import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg') #get the required spreadsheet
sheet = ss[0] #extract the sheet from the spreadsheet

#iterate through the rows entire spreadsheet
for row in range(2,15002): 
    beans_per_jar = int(sheet[1,row])
    jar = int(sheet[2,row])
    total_beans  =int(sheet[3,row])

    #to check if the product of the first two cells is equal to the result in the third cell
    if(beans_per_jar * jar != total_beans):
        print("Incorrect row is - "+ str(row))





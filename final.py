#this program will track the user taking out the tools, track the tool count in each bin, and also create a report showing the current count of tools when requested.
#input should start with name so we can log the user. We can feed this into a running csv file and also track the date and time for the user 'logging in'
#the tools shouldn't need to change. I can pull some cutting tools from our current inventory to use as an example for this project so it feels real-world
#the report can use the pdf tool we used on the final week's project to output the tool inventory.  I'll need to figure out formatting so it looks good
#need to figure out how I want the user to interact with the project.  Will it just be 'enter number' then give a few options, or should I expect the user to give words?
#maybe it would be best to give the user word options, or a guide to tell what they can put in without getting errors?
#need to make a CSV log file, and a CSV part file




import csv
import sys
from datetime import datetime
from fpdf import FPDF

def main():

    user_login = input("Please enter your name to use system: ")
    userlogin(user_login)

    while user_request := input("Please choose between the following: \n 1: Create Report \n 2: Remove Tool \n 3: Restock Tool \n" ):
               if user_request not in ["1", "2", "3"]:
                   print("Invalid entry")
                   pass
               else:
                   break

    what_user_wants(user_request)

############################################################################### USER LOGS IN TO COMPUTER ###############################################
def userlogin(UL):
    login_time = datetime.now()
    if UL.lower() not in ["aaron", "brad", "steve"]:
        print("You do not have access to this system")
        sys.exit()

    with open('userlogin.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([UL, login_time])
############################################################################### USER LOGS IN TO COMPUTER ###############################################

############################################################################### WHAT DOES THE USER WANT? ###############################################
def what_user_wants(user_request):
    if user_request == "1":
         generate_report()
         print("Request Completed. Have a nice day!")
         sys.exit()

    if user_request == "2":
        remove_tool()
        print("Request Completed. Have a nice day!")
        sys.exit()

    if user_request == "3":
        restock_tool()
        print("Request Completed. Have a nice day!")
        sys.exit()


############################################################################### GENERATE REPORT ###############################################

def generate_report():
         #This section needs to output a PDF report of the tool list and quantity based on what's currently in the csv file called inventory.csv
    inventory = {}
    with open("inventory.csv", newline="") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            for row in reader:
                name = row["Part_Name"]
                qty = int(row["Quantity_On_Hand"])
                inventory[name] = qty


    # https://py-pdf.github.io/fpdf2/fpdf/index.html

    # class FPDF
    # (
    # orientation: str | PageOrientation = PageOrientation.PORTRAIT,
    # unit: str | float = 'mm',
    # format: str | tuple[float, float] = 'A4',
    # font_cache_dir: Literal['DEPRECATED'] = 'DEPRECATED',
    # *,
    # enforce_compliance: str | DocumentCompliance | None = None)
    #pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')


    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("helvetica", style="B", size = 48)
    pdf.set_text_color(128,0,0)
    pdf.cell(0, 10, "Inventory Report", align = "C")
    pdf.ln(25)
    pdf.set_font("helvetica", style= "i", size = 12)
    pdf.set_text_color(0)
    pdf.cell(90,10, "Part Name", 1, align = "C")
    pdf.cell(90,10, "Quantity on Hand", 1, new_x="LMARGIN", new_y="NEXT", align = "C")

    for name, qty in inventory.items():
        pdf.cell(90, 10, name, align = "C")
        pdf.cell(90, 10, str(qty), new_x="LMARGIN", new_y="NEXT", align = "C")

    pdf.output("inventory_report.pdf")


############################################################################### REMOVE TOOLS   - This section is working!! ###############################################

def remove_tool():
         #this section needs to ask the user which tool they want to take out, and how many of that tool they want to take out
          #then that number needs to be updated in the inventory csv file.  Need to ensure you can remove more tools than you have in inventory!

    inventory = {}
    inventory_list = []
    with open("inventory.csv", newline="") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            name = row["Part_Name"]
            qty = int(row["Quantity_On_Hand"])
            inventory[name] = qty
        inventory_list = list(inventory.keys())
    while remove_tool := input("Which tool would you like to remove? "):
        if remove_tool not in inventory_list:
            print(f"You can only enter one of these tool names: {inventory_list}")
            continue
        else:
            break
    while remove_qty := input("How many tools would you like to remove? "):
        try:
            remove_qty = int(remove_qty)  #if the quantiy is not a positive integer then we need to send them back through the while loop until they get it right
            if remove_qty < 1:
                print("You must enter a positive integer digit!")
                continue
            else:
                current_qty = inventory[remove_tool]
                if current_qty < remove_qty:
                    print("You are attempting to remove more tools than we have in storage")
                    continue
                else:
                    inventory[remove_tool] = current_qty - remove_qty                   ##### This is the line that takes the old inventory and marks it down by the requested amount
                    break
        except ValueError:
            print("You must enter a positive integer digit!")
            continue

       ### write back to the csv file  ####


    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for name, qty in inventory.items():
                writer.writerow([name, qty])

    with open('userlogin.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"User above has removed {remove_qty} of {remove_tool} to inventory."])



############################################################################### RESTOCK TOOLS - CURRENTLY WORKING!!! ###############################################

def restock_tool():
                            #this section needs to ask the user which tool they want to restock and how many parts they want to restock the inventory with.

    inventory = {}
    inventory_list = []
    with open("inventory.csv", newline="") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            name = row["Part_Name"]
            qty = int(row["Quantity_On_Hand"])
            inventory[name] = qty
        inventory_list = list(inventory.keys())
    while restock_tool := input("Which tool would you like to restock? "):
        if restock_tool not in inventory_list:
            print(f"You can only enter one of these tool names: {inventory_list}")
            continue
        else:
            break
    while restock_qty := input("How many tools would you like to restock? "):
        try:
            restock_qty = int(restock_qty)
            if restock_qty < 1:
                print("You must enter a positive integer digit!")
                continue
            else:
                break
        except ValueError:
            print("You must enter a positive integer digit!")
            continue
    ##### now we know the tool that we want to change, and how many we want to add to the quantity #####


    current_qty = inventory[restock_tool]
    inventory[restock_tool] = restock_qty + current_qty




    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for name, qty in inventory.items():
                writer.writerow([name, qty])

    with open('userlogin.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"User above has added {restock_qty} of {restock_tool} to inventory."])



if __name__ == "__main__":
    main()












############################################################### CODING NOTES #################################
#key dictionary functions:
#read a value: print(dictionaryname["name"]) will give Aaron
#change an existing value: dictionaryname["name"] = "Bob"  will then make the name key Bob
#add a new key and value: dictionaryname["fav_color"] = "Blue"  will make a new dict line item with fav_color the key and blue the value
#in csv files, the keys are the first row (headers) of the column and the values are the rows below
#so if you have a csv with headers and 20 lines below, you now have 20 dictionaries with the header being the keys for all
#in this file, you'd have (Name: tool 1, QTY: 25) as one dictionary and so on
#headers = reader.firstrow  this saves the column keys
#rows = list(reader)  this saves all rows into lists
# for row in rows:
#if row["name"] == "Aaron":
#    row["fav_color"] = "Blue"
#to write:
#with open("data.csv"... ) as file:
#   writer = csv.dictwriter(file, headers = headers)
#    writer.writeheader()
#   writer.writerows(rows)

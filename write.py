def generate_invoice(kitta, duration, customer, lands, phone_number):
    land = lands[kitta]
    price = land['price']
    total_amount = duration * price
    customer_filename = customer.lower().replace(" ", "_") + '_rent_invoice.txt'
    
    invoice_content = (
 "\n**********************************************************************\n"
       
     "******************* TechnoPropertyNepal  ****************************\n"
     "*******************  Ekantakuna, Lalitpur ***************************\n"
   
         "Invoice for: " + customer.upper() + "\n"
        "Phone Number: " + phone_number + "\n"
        "Land Kitta Number: " + kitta + "\n"
        "Duration (Months): " + str(duration) + "\n"
        "Monthly Price: NPR " + str(price) + "\n"
        "Total Rent Amount: NPR " + str(total_amount) + "\n"
        "*************************************************************\n"
        "Thank you for choosing TechnoPropertyNepal for your land rental needs!\n"
    )
    
    try:
        with open(customer_filename, 'a') as file:
            file.write(invoice_content)
        print(invoice_content)
    except IOError as e:
        print("Failed to write the invoice due to an error: ", e)

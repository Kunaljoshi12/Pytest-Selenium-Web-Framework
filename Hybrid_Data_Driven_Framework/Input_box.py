from Hybrid_Data_Driven_Framework.Read_Excel import Read_Execel
from Hybrid_Data_Driven_Framework.Database_1 import Read_Database
from Hybrid_Data_Driven_Framework.User_Input import User_input

a = int(input("Enter the number (1 for Excel, 2 for DB, 3 for User): "))

match a:
    case 1:
        value = Read_Execel()
        if value:
            print(f"Success! Processed Excel ID: {value}")
    case 2:
        # Pass the ID you want to search for in the database
        value =Read_Database(123)
        if value:
            print(f"Success! Processed Database ID: {value}")
    case 3:
        User_input()
    case _:
        print("Invalid input.")
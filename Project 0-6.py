import os

AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Rivian R1T", "Ram 1500"]

def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    
def createFile():
    if not os.path.isfile("allowedvehicleslist.txt"):
        with open("allowedvehicleslist.txt", "w") as db:
            db.write("\n".join(AllowedVehiclesList))
            
def loadVehicles():
    with open("allowedvehicleslist.txt", "r") as db:
        vehicles = db.read().splitlines()
    return vehicles

def saveVehicles(vehicles):
    with open("allowedvehicleslist.txt", "w") as db:
        db.write("\n".join(vehicles))

def printVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    vehicles = loadVehicles()
    for vehicle in vehicles:
        print(vehicle)
        
    
def searchVehicle():
    search = input("Please enter the full vehicle name: ")
    vehicles = loadVehicles()
    if search in vehicles:
        print(f"{search} is an authorized vehicle")
    else:
        print(f"{search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def addVehicle():
    newVehicle = input("Please Enter the full Vehicle name you would like to add: ")
    vehicles = loadVehicles()
    vehicles.append(newVehicle)
    saveVehicles(vehicles)
    print(f"You have added {newVehicle} as an authorized vehicle")
  
def removeVehicle():
    deletedVehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    confirm = input(f"Are you sure you want to remove {deletedVehicle} from the Authorized Vehicles list? ")
    if confirm.lower() in ["yes" , "y"]:
        vehicles = loadVehicles()
        if deletedVehicle in vehicles:
            vehicles.remove(deletedVehicle)
            saveVehicles(vehicles)
            print(f"You have REMOVED {deletedVehicle} as an authorized vehicle")
        elif confirm.lower() in ["no" or "n"]:
            main()

def main():
    createFile()
    while True: 
        menu()
        number = input()
        if number == "1":  
            printVehicles()
        elif number == "2":
            searchVehicle()
        elif number == "3":
            addVehicle()
        elif number == "4":
            removeVehicle()
        elif number == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
            
if __name__ == "__main__":
    main()
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}




    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') 
    #print(csvFile)
    lineCount = 0  
    for row in csvReader:
        #print(row)
        if lineCount == 0:
     #       print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:
            #print(row)
      #      print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
           # print(myInventoryList)
            lineCount += 1  
   # print(f'Processed {lineCount} lines.'
   
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
    
print(myInventoryList)

for elemento in myInventoryList:
    for key, value in elemento.items():
        print("{} : {}".format(key,value))
        print("-----")
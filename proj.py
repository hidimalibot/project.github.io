import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "zJIYgy3Mt52LFIwhyk9x5EjJiLO8ykXK"

class Conversion:

    def __init__(self):
        self.x = input("KM , YD or Miles format: ") # This is where user will choose their desire unit.
        self.Paths = ["Fastest Path","Shortest Path","Walking path"] # This is where the user will choose their paths.
        self.Avoids = ["Highways","Bridge","Tunnel", "Streets"]
        self.Choices()
    def main(self):
        if self.x == "km" or self.x == "KM" or self.x == "Km" or self.x == "kM":
            y = "km"
        elif self.x == "YD" or self.x == "yd" or self.x == "Yd" or self.x == "yD":
            y = "m"
        elif self.x == "miles" or self.x == "Miles" or self.x == "MILES" or self.x == "mi" or self.x == "Mi" or self.x == "mI" or self.x == "MI":
            y = "mi"
        self.y = y
        return self.y

    def Choices(self):
        print("Choose path do you want to take.\n")
        for i in range(len(self.Paths)):
            print("[" +str(i+1) + "] {}\n".format(self.Paths[i]))
        self.Path=int(input())
        print("Choose what you want to avoid\n")
        for i in range(len(self.Avoids)):
            print("[" +str(i+1) + "] {}\n".format(self.Avoids[i]))
        self.Avoid=int(input())
        return self.Path,self.Avoid

while True:
    z = Conversion()
    orig = input("Source City:")
    if orig == "quit" or orig == "q":
        break
    dest = input("Your Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Arrival Time:   " + (json_data["route"]["formattedTime"]))
        print("-----------------Distance in different units!-----------------")
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Miles: " + str(json_data["route"]["distance"])) #We add Miles conversion of Km
        print("Yards: " + str("{:.2f}".format((json_data["route"]["distance"])*1760))) #We add yards conversion of Km
        print("-----------------Fuel Used in different units-----------------")
        print("Fuel Used(ltr):      " + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
        print("Fuel Used(Imperial Gal):      " + str("{:.2f}".format((json_data["route"]["distance"])*0.8327))) #We add Galon conversion of Liters
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    elif json_status == 402:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("********************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

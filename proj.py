import urllib.parse
import requests
from flask import Flask, render_template, request

app = Flask(__name)

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "zJIYgy3Mt52LFIwhyk9x5EjJiLO8ykXK"  # Replace with your MapQuest API key

class Conversion:
    def __init__(self):
        self.x = ""
        self.Paths = ["Fastest Path", "Shortest Path", "Walking path"]
        self.Avoids = ["Highways", "Bridge", "Tunnel", "Streets"]
        self.Path = None
        self.Avoid = None

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
        
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_directions", methods=["POST"])
def get_directions():
    z = Conversion()
    orig = request.form["source"]
    dest = request.form["destination"]

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()
    # Your processing logic here
    return render_template("directions.html", data=json_data)

if __name__ == "__main__":
    app.run(debug=True)

import urllib.request
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    print (theJSON["results"]["collection1"][0]["Course"])

    for i in theJSON["results"]["collection1"]:
        print(i["Course"] + " " + i["Title"])

def main():

    urlData = "https://www.kimonolabs.com/api/7rf253we?apikey=4bb788e9e56732f39c8c9802c45b2110"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print (webUrl.getcode())

    if (webUrl.getcode() == 200):
        print ('OK')
        data = webUrl.read()
        data = data.decode("utf-8")
        # print out our customized results
        printResults(data)
    else:
        print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))


if __name__ == "__main__":
    main()

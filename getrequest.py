import requests as req

URL = "http://127.0.0.1:5000/handle/api/items/barcode="
print("De forskjellige strekkodene er : 25949455, og : 2395329")
while True:
    userinput = input('Please enter a barcode: ')

    #Trengs ikke
    #result = ''
    #if len(userinput) >= 13:
    #    for x in range(0,13):
    #        result +=userinput[x]
    #        print(x, userinput[x])
    #else: result = userinput

    if userinput == 'quit':
        break

    resp = req.get(URL+userinput)

    print(resp.url)
    print(resp.text)
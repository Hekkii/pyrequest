import requests as req

URL = "http://127.0.0.1:3000/api/barcode/"
while True:
    userinput = input('Please enter a barcode, rpi')

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
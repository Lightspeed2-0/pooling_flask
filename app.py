from flask import Flask
from pincode import cordinatesDistance,getCordinates,getPaths

app = Flask(__name__)

clientReq = {
  "Weight": 101,
  "Volume": 123,
  "srcPincode": 605602,
  "desPincode": 600063,
}
Order = [
    {
        "remWeight": 1010,
        "remVolume": 123,
        "srcPincode": 620001,
        "desPincode": 600044,
    }
]

Routes = []
poolArr = []

@app.route('/')
def pool() :
    clientCoordinates = getCordinates(str(clientReq["srcPincode"]),str(clientReq["desPincode"]))
    for i in range(len(Order)) :
        if clientReq["Weight"] <= Order[i]["remWeight"] and clientReq["Volume"] <= Order[i]["remVolume"] : 
            Routes = getPaths(str(Order[i]['srcPincode']),str(Order[i]['desPincode']))
            sourcePos = -1
            print(clientCoordinates)
            print('-----------------')
            for j in range(len(Routes)) :
                # print('hi')
                if cordinatesDistance(Routes[j][1],Routes[j][0],clientCoordinates['src'][0],clientCoordinates['src'][0]) <= 20 :
                    sourcePos = i
                if cordinatesDistance(Routes[j][1],Routes[j][0],clientCoordinates['des'][0],clientCoordinates['des'][0]) <= 20 :
                    if sourcePos == -1 :
                        break
                    else :
                        poolArr[i] = Order[i]
                        break
    print(poolArr)
    return 'Ok'



    


if __name__ == '__main__' :
    app.run(debug=True)
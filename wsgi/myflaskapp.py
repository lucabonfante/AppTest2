from flask import Flask

from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
from json import dumps
import pymongo
import os
from bson import objectid
from bson import json_util
from flask import request


#from flask.ext.cors import CORS


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

#CORS(app)
conn = pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
db = conn[os.environ['OPENSHIFT_APP_NAME']]
positions=db['positions']


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/js/<nomeFileJs>")
def jsLoad(nomeFileJs):
    return send_from_directory('js', nomeFileJs)

@app.route("/css/<nomeFileCss>")
def cssLoad(nomeFileCss):
    return send_from_directory('css', nomeFileCss)

@app.route("/insertPosition/", methods = ["POST"])
def insertPosition():
    
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    date = request.json['date']
    
    coordinate = {"latitude" : latitude, "longitude" : longitude, "date":date}
    
    positions.insert(coordinate)
    dictTest = {}
    cursor = positions.find()
    for document in cursor:
        dictTest['latitude']=document['latitude']
        dictTest['longitude']=document['longitude']
        dictTest['date']=document['date']
    return jsonify(dictTest)

@app.route("/readPositions/", methods = ["POST"])
def readPositions():
    risultato="<p>"
    for coordinate in positions:
        latitudine = positions[coordinate]["latitude"]
        longitudine = positions[coordinate]["longitude"]
        data = positions[coordinate]["date"]
        risultato += '  <div class=""> \
                            <table style="width:90%"> \
                                <tr> \
                                    <td><b>Latitudine:&nbsp;&nbsp;&nbsp;</b></td> \
                                    <td><b>Longitudine:&nbsp;&nbsp;&nbsp;</b></td> \
                                    <td><b>Data:</b></td> \
                                    <td><a href="#" class="x" onclick="APP.eliminaPosition();">x</a></td> \
                                </tr> \
                                <tr> \
                                    <td>' + latitudine + '</td> \
                                    <td>' + longitudine + '</td> \
                                    <td>' + data + '</td> \
                                </tr> \
                            </table> \
                        </div> '
    risultato += "</p>"
    return risultato

@app.route("/cleanPositions/", methods = ["POST"])
def cleanPositions():
#    date = request.json[pos]
#    positions[date] = {}
    return ""
    
if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True, port=8000)
    #65013
    
    #\'' + coordinate + '\'
from flask import Flask, jsonify,request
app =Flask(__name__) 
  
@app.route('/', methods = ['GET']) 
def ReturnJSON(): 
    if(request.method == 'GET'): 
        data = { 
            "id" : 1, 
            "Name" : "helloo", 
        } 
        return jsonify(data) 
  
if __name__=='__main__': 
    app.run(debug=True)
from flask import Flask, request 
app = Flask(__name__)

@app.route('/alarm', methods = ['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        print('received alarm!')
        return "alarm received", 200
    elif request.method == 'GET':
        print('received alarm!')
        return "alarm received", 200        
if __name__ == '__main__':
    app.run(debug = True)
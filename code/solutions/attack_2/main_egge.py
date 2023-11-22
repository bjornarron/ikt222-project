from flask import Flask, request

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    print("Data received:", data)
    # You can add code here to save the data to a file or database
    return 'Data captured', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

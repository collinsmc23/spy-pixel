from flask import Flask, send_file, request
import requests as requestss
import datetime
import urllib.request

app = Flask(__name__)
@app.route('/image')

def my_spy_pixel():
    filename = "pixel.png"
    
    # Log the request information
    #user_agent = request.get('http://httpbin.org/headers')
    user_agent = request.headers.get('User-Agent')

    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S")
    response = requestss.get('https://checkip.amazonaws.com/')
    get_ip = response.text
    
    # - Lookup Geolocation of IP Address - 
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ get_ip) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")

    log_entry = f"Timestamp: {timestamp}\n, User Agent: {user_agent}\n, IP Address: {data}\n"
    
    with open('spy_pixel_logs.txt', 'a') as f:
        f.write(log_entry)
    
    # Serve a transparent pixel image
    return send_file(filename, mimetype="image/png")

if __name__ == '__main__':
    app.run()

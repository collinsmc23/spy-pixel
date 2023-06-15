![spy.gif](SPY)
# 🔍 Email Spy Pixel
*A basic tracking pixel to track email opens.*

## Overview
Spy pixels, also commonly referred to as web beacons, are small artifacts implemented in applications to gather user information, which could include the User-Agent string, IP address, and if an email is opened etc. A basic method to collect this information is through the use of a 1x1 pixel with an embedded URL through a transparent PNG, GIF, JPG.

This project uses Python Flask to serve a static web page with a `pixel.png` included in the `.../image` directory. When a user opens an email with the embedded spy pixel, the User-Agent string, timestamp, and IP Address are logged to the `spy_pixel_logs.txt` file.

## Deploy

To deploy this web application, create a basic server using a VPS / cloud provider of choice. Used Amazon EC2 Ubuntu 20.04 LTS in this deployment.

The following services need to be installed:
- apache2
- libapach2-mod-wsgi-py3
- python-pip
- python 3.8+




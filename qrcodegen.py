import os
import qrcode

link = input("Enter the URL to generate the QRCode: ")

img = qrcode.make(link)

if "myqrcode.png" in os.listdir():
    counter = 0
    file_name = "myqrcode - Copy.png"
    while file_name in os.listdir():
        counter += 1
        file_name = "myqrcode - Copy (" + str(counter) + ").png"
    img.save(os.getcwd() + "/" + file_name)
else:
    img.save(os.getcwd() + "/myqrcode.png")

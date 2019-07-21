from PIL import Image
import base64

image = open('python.png', 'rb') #open binary file in read mode
image_read = image.read() 
image_64_encode = base64.encodestring(image_read) #encode using base64
print(image_64_encode) #display encoded value


image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('new.png', 'wb') #create new file
image_result.write(image_64_decode) #decode using base64

import os

print(os.listdir('/home/lewington/.ssh'))

with open('/home/lewington/.ssh/desktop-windows.pem') as f:
	print(f.read())
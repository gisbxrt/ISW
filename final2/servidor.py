import sys, os, socket

#ip = "localhost"
#puerto = 16011
direc =("localhost",16011)


# crear socket
servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# realizamos bind a la dirección del server
servsocket.bind(direc)
# ponemos en escucha, inicialmente cola=1, recomendado <5
servsocket.listen(5)

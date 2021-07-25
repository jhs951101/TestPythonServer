from socket import *
import _thread

# -*- coding: UTF-8 -*-

def execute(connectionSocket):
     try:
          request = ''
          response = ''
          orderinfo = []
          available = True
          
          print('A client has accessed!')
          print('')

          while available:
               request = connectionSocket.recv(1024)
               request = request.decode('UTF-8')

               if request is None:
                    continue

               orderinfo = request.split()

               if orderinfo[0] == 'order1':
                    response = 'order1-response'
               elif orderinfo[0] == 'order2':
                    response = 'order2-response'
               elif orderinfo[0] == 'exit':
                    response = orderinfo[0]
                    available = False

               connectionSocket.send(response.encode('UTF-8'))
          
     except Exception as e:
          print('')

     print('A client has exited...')
     print('')

     connectionSocket.close()
     return 0

# main

try:
     portNumber = 8889
     IPAddress = ''
     serverSocket = socket(AF_INET, SOCK_STREAM)
     serverSocket.bind((IPAddress, portNumber))
     serverSocket.listen(1)
     print('A server has been started!')
     print('Port Number: ', portNumber)

     while True:
          connectionSocket, addr = serverSocket.accept()
          _thread.start_new_thread(execute, (connectionSocket,))

except Exception as e:
     print('Error: ', e)

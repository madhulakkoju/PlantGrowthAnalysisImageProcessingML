# Importing required Modules
import random
from random import randint
# Module random imported
import socket, select
# Socket and select modules imported
from time import gmtime, strftime
#gmttime and strftime imported
import VotingClassifier as vote
# Voting Classifier Module is imported
from file1 import FeatureExtract
# FeatureExtract method takes the Image path as input and returns a list consisting of Features.
from DataSupport import *
# DataSupport module is imported to handle all Datahandling purposes
voteClassifier = vote.model(x_train,y_train) # Creating a Vote Classifier model
print("SERVER")
imgcounter = 1  #imgcounter keeps track of the images to be added to buffer for improving the dataset
basename = "bufferImages\\execute"
#A Base Name is used as a prefix to the Image to store into the BufferImages
HOST = '127.0.0.1'
PORT = 6666 # Defining the Host and Port address of the present server process 
connected_clients_sockets = [] # connected_clients_sockets contains the socket address of all the connected clients.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)
print("START")
connected_clients_sockets.append(server_socket)
# Server needs to call itself sometimes. so the server socket is added ... a
# also this helps in avoiding redundancy in socket addresses
while True:
    #print("Currently connected Client Sockets ",connected_clients_sockets) 
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])
    # Checking if any Clients are trying to access the Server.
    print("Connect Request ..")
    for sock in read_sockets:  # iterating over the clients which are sensed and accepting their requests. 
        if sock == server_socket:
            sockfd, client_address = server_socket.accept()
            # Accepting the client request.
            connected_clients_sockets.append(sockfd)
            # adding the accepted clients to the list 
        else:
            try:
                myfile = open(basename+str(imgcounter)+".jpg", 'wb')
                #opening a temporary writeable image file 
                #print("Receiving Data From Client")
                data = sock.recv(40960000)
                #print(data)
                #receiving the data in the form of bytes.
                myfile.write(data)
                #writing the bytestream data into the image.
                myfile.close() #commiting the Image 
                #print("Received the Image ")
                print("Processing")
                try:
                    pred_output = vote.predict( voteClassifier,[FeatureExtract(basename+ str(imgcounter) + ".jpg" )] )
                    # Predicting the Output to the given Image using the Vote Classifier
                    imgcounter = imgcounter + 1
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    # If any exceptions occur in between, we need to show that.
                    print (message)
                print(pred_output," is the Predicted Server Output")
                sock.send( pred_output[0][:-1].encode() ) #Sending the output to Client
                sock.shutdown() #Terminate the Socket to the Client connected
            except:
                sock.close()
                #Terminate the Socket to the Client connected
                connected_clients_sockets.remove(sock)
                continue
server_socket.close() # Shutting down the server process

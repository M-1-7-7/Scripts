# Initial inspection

1. Does the URL have a `?page=<whatever>` at the end?
   a. Yes then continue
   b. No then stop

# attempt LFI firstly
 
1. cat a file every user should have access to
  a. `<url>/?page=../../../../../../../../../../../etc/passwd`

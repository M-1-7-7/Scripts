# How to modify file extentions

**other extentions to try that may be valid**

- Look at the image bellow, you hay see other comonly accepted extentions accepted
  
![Screenshot 2023-08-30 at 9 26 51 am](https://github.com/M-1-7-7/Scripts/assets/108218328/bbd1ec36-8409-49ea-8cab-88e9aef49464)

**change File extention**

- this involves the file extention to attempt to trick the server, not always effective

**Use burpsuite**

- this will trick the server to thinking it is receiving a `.jpg`
  
![Screenshot 2023-08-30 at 9 56 35 am](https://github.com/M-1-7-7/Scripts/assets/108218328/add05a5c-8961-4288-b075-687f381c0e82)

**Embed PHP into JPG**

- use this small python script to create the payload, ensure you are using a WHITE JPG

```
#!/bin/python3
hideme = open('<file.jpg>','rb').read()
hideme += open('<file.php>'.'rb').read()
open('hideme.php3','wb').write(hideme)
```

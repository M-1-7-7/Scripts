$path = 'C:\Users\User\Desktop\Output\Temp\ImportantFile.txt'
Copy-Item -Path $path –Destination ([io.path]::ChangeExtension($path, '.zip'))
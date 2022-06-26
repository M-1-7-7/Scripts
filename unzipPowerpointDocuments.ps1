cd C:\Users\User\Desktop\output\all_powerpoint_docs
$unzipedArray = New-Object System.Collections.ArrayList

Dir *.ptx* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

#unzip documents
Get-ChildItem C:\Users\User\Desktop\output\all_powerpoint_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ($_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $unzipedArray.Add($destination) | out null
}


#
#   get the file for the Powerpoints from Tam to modifie lines 20 and 21
#

foreach ($i in $unzipedArray)
{
    cd C:\Users\User\Desktop\output\all_word_docs
    $directoy = $i + '\word\document.xml' 
    $a = Get-Content -path $directoy
   
    if ($a -like "*string1*" -or $a -like "*string2*" )
    {
       $DestinationLocation =  'C:\Users\User\Desktop\output\docs_of_interest'
       $file = $i + ".zip"
       $file
       Write-Host "accpting"   
       Copy-Item -path $file -Destination $DestinationLocation -Recurse
    }
    cd C:\Users\User\Desktop\output\docs_of_interest
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "ppt") }
}

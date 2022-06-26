cd C:\Users\User\Desktop\output\all_excel_docs

#an array containg a list of unziped docs so we can access the contents
$unzipedArray = New-Object System.Collections.ArrayList

#convering .xls to a .zip file 
Dir *.xls* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

#unzipping a .zip and stopring the files into the array for reference 
Get-ChildItem C:\Users\User\Desktop\output\all_excel_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ($_.BaseName)
    $unzipedArray.Add($destination) | out null
}


#loop through array and into the "word\document.xml" file
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
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "xls") }
}

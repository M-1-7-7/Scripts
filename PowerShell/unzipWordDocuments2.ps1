cd C:\Users\User\Desktop\output\all_word_docs
$unzipedArray = New-Object System.Collections.ArrayList
#turn word documents into zip documents
Dir *.doc* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }
#unzip documents
Get-ChildItem C:\Users\User\Desktop\output\all_word_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ($_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $unzipedArray.Add($destination) | out null
}

#identify all unziped folders and put fullname into array
#loop through array and into the "word\document.xml" file

foreach ($i in $unzipedArray)
{
    cd C:\Users\User\Desktop\output\all_word_docs
    $directoy = $i + '\word\document.xml' 
    $a = Get-Content -path $directoy
    if ($a -like "*a*")
    {
       $DestinationLocation =  'C:\Users\User\Desktop\output\docs_of_interest'
       $file = $i + ".zip"
       $file
       Write-Host "accpting"   
       Copy-Item -path $file -Destination $DestinationLocation -Recurse
    }
    cd C:\Users\User\Desktop\output\docs_of_interest
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "docx") }
}
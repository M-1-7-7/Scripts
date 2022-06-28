# Move to all_powerpoint_docs Directory
cd C:\Users\User\Desktop\output\all_word_docs

# New Array Names of our new zip files
$doc_array = New-Object System.Collections.ArrayList
# Modify extention of word documents zip
Dir *.doc* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

#unzip documents
Get-ChildItem C:\Users\User\Desktop\output\all_word_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ($_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $doc_array.Add($destination) | Out-Null
}

<#
# Identify all unziped folders and put fullname into array
# Loop through array and into the "word\document.xml" file
# Check for classification keywords

foreach ($i in $unzipedArray)
{
    cd C:\Users\User\Desktop\output\all_word_docs
    $directoy = $i + '\word\document.xml' 
    $a = Get-Content -path $directoy
    if ($a -like "*a*")
    {
       $DestinationLocation =  'C:\Users\User\Desktop\output\Positive_results'
       $file = $i + ".zip"
       $file
       Write-Host "accpting"   
       Copy-Item -path $file -Destination $DestinationLocation -Recurse
    }
    cd C:\Users\User\Desktop\output\Positive_results
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "docx") }
}
#>


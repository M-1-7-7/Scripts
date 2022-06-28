# Move to all_word_Docs Directory
cd C:\Users\User\Desktop\Output\all_word_docs

# Return all .doc files and then modify extention to .zip
Dir *.doc* | Rename-Item -NewName { [io.path]::ChangeExtension($_.name, "zip") }

# Unzip any zip files
Get-ChildItem C:\Users\User\Desktop\Output\all_word_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ("Unziped - " + $_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
}

# Check for classification keywords
$a = Get-content -Path "C:\Users\User\Desktop\Output\all_powerpoint_docs\Unziped - Test_1\ppt\slides\slide1.xml"
if ($a -like "*Something*"){
    Write-Host "True"
}
else {
    Write-Host "False"
}
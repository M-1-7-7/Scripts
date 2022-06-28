# Move to all_excel_docs Directory
cd C:\Users\User\Desktop\output\all_excel_docs

# New Array
$unzipped_array = New-Object System.Collections.ArrayList

# Return all . files and then modify extention to .zip
Dir *.xls* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

# Unzip any zip files
Get-ChildItem C:\Users\User\Desktop\Output\all_excel_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ("Unziped - " + $_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $unzipped_array.Add($destination)
}

# Check for classification keywords
foreach ($i in $unzipped_array){
    $directory = $i + 'ppt\slides\slide1.xml'
    $a = Get-content -Path $directory
    if ($a -like "*Something*"){
        Write-Host "True"
    }
    else {
        Write-Host "False"
    }
}



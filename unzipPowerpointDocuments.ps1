# Move to all_powerpoint_docs Directory
cd C:\Users\User\Desktop\output\all_powerpoint_docs

# New Array Names of our new zip files
$unzipped_array = New-Object System.Collections.ArrayList

# Return all .ppt files and then modify extention to .zip
Dir *.ppt* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

# Unzip any zip files
Get-ChildItem C:\Users\User\Desktop\Output\all_powerpoint_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ("Unziped - " + $_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $unzipped_array.Add($destination) | Out-Null
}

# Check for classification keywords
$unzipped_array

foreach ($i in $unzipped_array){
    $directory = $i + '\ppt\slides\slide1.xml'
    $a = Get-content -Path $directory
    $b = Get-ChildItem C:\Users\User\Desktop\Output\all_powerpoint_docs -Filter *.zip
    $fileName = $i + ".zip"
    if ($a -like "*Boo!*"){
        Write-Host "Alert: Data Spill in " $fileName
        Copy-Item -Path $b.FullName -Destination "C:\Users\User\Desktop\Output\positive_results"
    }
    else {
        Write-Host "No classification found in " $fileName
    }
    cd "C:\Users\User\Desktop\Output\positive_results"
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "pptx") }
}
# Move to all_powerpoint_docs Directory
cd C:\Users\User\Desktop\output\all_excel_docs

# New Array Names of our new zip files
$xls_array = New-Object System.Collections.ArrayList

# Return all . files and then modify extention to .zip
Dir *.xls* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

# Unzip any zip files
Get-ChildItem C:\Users\User\Desktop\Output\all_excel_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ("Unziped - " + $_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
    $xls_array.Add($destination)
}

<#
# Identify all unziped folders and put fullname into array
# Loop through array and into the "xl\worksheets\slide1.xml" file
# Check for classification keywords

foreach ($i in $unzipped_array){
    $directory = $i + 'xl\worksheets\slide1.xml'
    $a = Get-content -Path $directory
    $b = Get-ChildItem C:\Users\User\Desktop\Output\all_excel_docs -Filter *.zip
    $fileName = $i + ".zip"
    if ($a -like "*Boo!*"){
        Write-Host "Alert: Data Spill in " $fileName
        Copy-Item -Path $b.FullName -Destination "C:\Users\User\Desktop\Output\positive_results"
    }
    else {
        Write-Host "No classification found in " $fileName
    }
    cd "C:\Users\User\Desktop\Output\positive_results"
    Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "xlsx") }
}
#>
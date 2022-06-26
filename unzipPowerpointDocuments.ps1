cd C:\Users\User\Desktop\output\all_powerpoint_docs
Dir *.ptx* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }
$counter = 0
Get-ChildItem C:\Users\User\Desktop\output\all_powerpoint_docs -Filter *.zip | foreach {
    $destination = Join-Path $_.DirectoryName ("Unziped - " + $counter++ + $_.BaseName)
    Expand-Archive $_.FullName -DestinationPath $destination
}

$pdf = Get-ChildItem 'C:\Users\User\*' -Recurse -Filter *.pdf
Copy-Item -Path $pdf.FullName -Destination "C:\Users\User\Documents\Output\PDF"

$doc = Get-ChildItem 'C:\Users\User\*' -Recurse -Filter *.doc
Copy-Item -Path $doc.FullName -Destination "C:\Users\User\Documents\Output\DOC"

$ppt = Get-ChildItem 'C:\Users\User\*' -Recurse -Filter *.ppt
Copy-Item -Path $ppt.FullName -Destination "C:\Users\User\Documents\Output\PPT"

$xls = Get-ChildItem 'C:\Users\User\*' -Recurse -Filter *.xls
Copy-Item -Path $xls.FullName -Destination "C:\Users\User\Documents\Output\XLS"
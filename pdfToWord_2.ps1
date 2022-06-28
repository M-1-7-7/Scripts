$filePath = "C:\Temp\MyPdfDocument.pdf"
    $wd = New-Object -ComObject Word.Application
$wd.Visible = $true
$txt = $wd.Documents.Open(
    $filePath,
    $false,
    $false,
    $false)

$wd.Documents[1].SaveAs("C:\Temp\MyPdfDocument.docx")
$wd.Documents[1].Close()
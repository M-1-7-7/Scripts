$filePath = "C:\Users\User\Desktop\Output\all_pdf_docs"
    $wd = New-Object -ComObject Word.Application
$wd.Visible = $true

$txt = $wd.Documents.Open(
    $filePath,
    $false,
    $false,
    $false)

$wd.Documents[1].SaveAs("C:\Users\User\Desktop\Output\all_pdf_docs")
$wd.Documents[1].Close()
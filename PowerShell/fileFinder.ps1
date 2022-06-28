#Arrays and Filters for file types
$PDFfile = Get-Childitem C:\Users\ -recurse -filter "*.pdf" 
$PDFarray = New-Object System.Collections.ArrayList

$WORDfile = Get-Childitem C:\Users\ -recurse -filter '*.doc*' 
$WORDarray = New-Object System.Collections.ArrayList

$POWERPOINTfile = Get-Childitem C:\Users\ -recurse -filter '*.ppt*'
$POWERPOINTarray = New-Object System.Collections.ArrayList

$EXCELfile = Get-Childitem C:\Users\ -recurse -filter '*.xls*'
$EXCELarray = New-Object System.Collections.ArrayList

mkdir C:\Users\User\Desktop\Output | Out-Null
New-Item  C:\Users\User\Desktop\Output\NotAcceptedPdfName.txt| Out-Null
mkdir C:\Users\User\Desktop\Output\all_pdf_docs| Out-Null
New-Item C:\Users\User\Desktop\Output\NotAcceptedWord.txt| Out-Null
mkdir C:\Users\User\Desktop\Output\all_word_docs| Out-Null
New-Item C:\Users\User\Desktop\Output\NotAcceptedPowerpoint.txt| Out-Null
mkdir  C:\Users\User\Desktop\Output\all_powerpoint_docs| Out-Null
New-Item  C:\Users\User\Desktop\Output\NotAcceptedExcel.txt| Out-Null
mkdir  C:\Users\User\Desktop\Output\all_excel_docs| Out-Null
mkdir C:\Users\User\Desktop\Output\positive_results | Out-Null

#Loop to sort PDFs
foreach ($PDFitem in $PDFfile)
{
    $PDFarray.Add([pscustomobject]@{
        #ADD FILE PROPERTIES HERE TO DISPLAY MORE
        "Path" = $PDFitem.FullName}) | Out-Null
}

Foreach ($PDFstring in $PDFarray)
{
    if ($PDFstring -like "*``]*" -or $PDFstring -like "*``[*" ){
        Add-Content C:\Users\User\Desktop\Output\NotAcceptedPdfName.txt $PDFstring.Path
    }
    else{
        Copy-Item -Path $PDFfile.FullName -Destination C:\Users\User\Desktop\Output\all_pdf_docs
    }
}

#Loop to sort Word
foreach ($WORDitem in $WORDfile)
{
    $WORDarray.Add([pscustomobject]@{
        "Path" = $WORDitem.FullName}) |Out-Null

}

Foreach ($WORDstring in $WORDfile)
{
    if ($WORDstring -like "*``]*" -or $WORDstring -like "*``[*" ){
        $WORDstring
        Write-Host "TRUE"
        
        Add-Content C:\Users\User\Desktop\output\NotAcceptedWord.txt $WORDstring.Path
    }
    else{
        
        Copy-Item -Path $WORDfile.FullName -Destination C:\Users\User\Desktop\Output\all_word_docs
    }
}

#Loop to sort Power Point
foreach ($POWERPOINTitem in $POWERPOINTfile)
{
    $POWERPOINTarray.Add([pscustomobject]@{
        "Path" = $POWERPOINTitem.FullName}) |Out-Null
}

Foreach ($POWERPOINTstring in $POWERPOINTfile)
{
    if ($POWERPOINTstring -like "*``]*" -or $POWERPOINTstring -like "*``[*" ){    
        Add-Content C:\Users\User\Desktop\output\NotAcceptedPowerpoint.txt $string.Path
    }
    else{
        
        Copy-Item -Path $POWERPOINTfile.FullName -Destination C:\Users\User\Desktop\Output\all_powerpoint_docs
    }
}

#
#Loop to sort Excel
foreach ($EXCELitem in $EXCELfile)
{
    $EXCELarray.Add([pscustomobject]@{
        "Path" = $EXCELitem.FullName}) |Out-Null
}

Foreach ($EXCELstring in $EXCELfile)
{
    if ($EXCELstring -like "*``]*" -or $EXCELstring -like "*``[*" ){
        Add-Content C:\Users\User\Desktop\output\NotAcceptedExcel.txt $string.Path
    }
    else{
        Copy-Item -Path $EXCELfile.FullName -Destination C:\Users\User\Desktop\Output\all_excel_docs
    }
}
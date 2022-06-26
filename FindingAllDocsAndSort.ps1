#Arrays and Filters for file types
$PDFfile = Get-Childitem C:\Users\ -recurse -filter "*.pdf" 
$PDFarray = New-Object System.Collections.ArrayList

$WORDfile = Get-Childitem C:\Users\ -recurse -filter '*.doc*' 
$WORDarray = New-Object System.Collections.ArrayList

$POWERPOINTfile = Get-Childitem C:\Users\ -recurse -filter '*.ppt*'
$POWERPOINTarray = New-Object System.Collections.ArrayList

$EXCELfile = Get-Childitem C:\Users\ -recurse -filter '*.xls*'
$EXCELarray = New-Object System.Collections.ArrayList

#making directories for files 
#replace "User" with the name of the user you want to work in
mkdir C:\Users\User\Desktop\output
New-Item  C:\Users\User\Desktop\output\NotAcceptedPdfName.txt
mkdir C:\Users\User\Desktop\output\all_pdf_docs
New-Item C:\Users\User\Desktop\output\NotAcceptedWord.txt
mkdir C:\Users\User\Desktop\output\all_word_docs
New-Item C:\Users\User\Desktop\output\NotAcceptedPowerpoint.txt
mkdir  C:\Users\User\Desktop\output\all_powerpoint_docs
New-Item  C:\Users\User\Desktop\output\NotAcceptedExcel.txt
mkdir  C:\Users\User\Desktop\output\all_excel_docs

mkdir  C:\Users\User\Desktop\output\docs_of_interest

#Loop to sort PDFs
foreach ($PDFitem in $PDFfile)
{
    $PDFarray.Add([pscustomobject]@{
        "Path" = $PDFitem.FullName}) |Out-Null

}


Foreach ($PDFstring in $PDFarray)
{
    if ($PDFstring -like "*``]*" -or $PDFstring -like "*``[*" ){
        $PDFstring
        Write-Host "TRUE"
        
        Add-Content C:\Users\User\Desktop\output\NotAcceptedPdfName.txt $PDFstring.Path
    }
    else{
        Copy-Item -Path $PDFfile.FullName -Destination C:\Users\User\Desktop\output\all_pdf_docs
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
        
        Copy-Item -Path $WORDfile.FullName -Destination C:\Users\User\Desktop\output\all_word_docs
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
        $POWERPOINTstring
        Write-Host "TRUE"
        
        Add-Content C:\Users\User\Desktop\output\NotAcceptedPowerpoint.txt $string.Path
    }
    else{
        
        Copy-Item -Path $POWERPOINTfile.FullName -Destination C:\Users\User\Desktop\output\all_powerpoint_docs
    }
}

#Loop to sort Excel
foreach ($EXCELitem in $EXCELfile)
{
    $EXCELarray.Add([pscustomobject]@{
        "Path" = $EXCELitem.FullName}) |Out-Null

}

Foreach ($EXCELstring in $EXCELfile)
{
    if ($EXCELstring -like "*``]*" -or $EXCELstring -like "*``[*" ){
        $EXCELstring
        Write-Host "TRUE"
        
        Add-Content C:\Users\User\Desktop\output\NotAcceptedExcel.txt $string.Path
    }
    else{
        Copy-Item -Path $EXCELfile.FullName -Destination C:\Users\User\Desktop\output\all_excel_docs
    }
}

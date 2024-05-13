


#Variables for target directories
$ScriptLocation = Get-Location
$TargetDirectory = "C:\Users\abb58612\" # Point this at the file path you want the scan to start at
$EvidenceDirectory = "C:\Users\abb58612\Desktop\" # Point this at the directory you want to store your evidence
$Dirty_Words_file = $ScriptLocation + "Dirty_Words.txt" # This should point to the directory you are storing the Dirty Words text file, by default the same dir as this script
$OutDir = $EvidenceDirectory + "Output\" # where the results will be stored
$PosResultsDir = "C:\Users\abb58612\Desktop\output\Positive_results\" # where positive matches to the dirty words will be stored

#Create Arrays and Filters for file types
function Create-Arrays {
    "Create Arrays: Start"
    $PDFfile = Get-Childitem $TargetDirectory -recurse -filter "*.pdf" 
    $PDFarray = New-Object System.Collections.ArrayList

    $WORDfile = Get-Childitem $TargetDirectory -recurse -filter '*.doc*' 
    $WORDarray = New-Object System.Collections.ArrayList

    $POWERPOINTfile = Get-Childitem $TargetDirectory -recurse -filter '*.ppt*'
    $POWERPOINTarray = New-Object System.Collections.ArrayList

    $EXCELfile = Get-Childitem $TargetDirectory -recurse -filter '*.xls*'
    $EXCELarray = New-Object System.Collections.ArrayList

    $TXTfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.txt'
    $TXTarray = New-Object System.Collections.ArrayList

    $JPEGfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.jpeg'
    $JPEGarray = New-Object System.Collections.ArrayList

    $PNGfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.png'
    $PNGarray = New-Object System.Collections.ArrayList

    $BMPfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.bmp'
    $BMParray = New-Object System.Collections.ArrayList

    $TIFFfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.tiff'
    $TIFFarray = New-Object System.Collections.ArrayList

    $MP3file = Get-ChildItem $TargetDirectory -Recurse -Filter '*.mp3'
    $MP3array = New-Object System.Collections.ArrayList

    $MP4file = Get-ChildItem $TargetDirectory -Recurse -Filter '*.mp4'
    $MP4array = New-Object System.Collections.ArrayList

    $AVIfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.avi'
    $AVIarray = New-Object System.Collections.ArrayList

    $MOVfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.mov'
    $MOVarray = New-Object System.Collections.ArrayList

    $MSGfile = Get-ChildItem $TargetDirectory -Recurse -Filter '*.msg'
    $MSGarray = New-Object System.Collections.ArrayList
    "Create Arrays: Done"
    Find-Files
}

#Create Direcories and files to store evidence
function Create-Dirs {
    "Create Dirs: Start"
    if (Test-Path -Path $OutDir) {
        "Path exists"
    } 
    else{
                    
    mkdir $OutDir | Out-Null
    cd $OutDir
    New-Item  NotAcceptedJPEGName.txt| Out-Null
    mkdir all_jpeg | Out-Null
    New-Item  NotAcceptedPNGName.txt| Out-Null
    mkdir all_png | Out-Null
    New-Item  NotAcceptedBMPName.txt| Out-Null
    mkdir all_bmp | Out-Null
    New-Item  NotAcceptedTIFFName.txt| Out-Null
    mkdir all_tiff | Out-Null
    New-Item  NotAcceptedMP4Name.txt| Out-Null
    mkdir all_mp4 | Out-Null
    New-Item  NotAcceptedMP3Name.txt| Out-Null
    mkdir all_mp3 | Out-Null
    New-Item  NotAcceptedAVIName.txt| Out-Null
    mkdir all_avi | Out-Null
    New-Item  NotAcceptedMSGName.txt| Out-Null
    mkdir all_msg | Out-Null
    New-Item  NotAcceptedMOVName.txt| Out-Null
    mkdir all_mov | Out-Null
    New-Item  NotAcceptedTXTName.txt| Out-Null
    mkdir all_txt | Out-Null
    New-Item  NotAcceptedPdfName.txt| Out-Null
    mkdir all_pdf_docs| Out-Null
    New-Item NotAcceptedWord.txt| Out-Null
    mkdir all_word_docs| Out-Null
    New-Item NotAcceptedPowerpoint.txt| Out-Null
    mkdir all_powerpoint_docs| Out-Null
    New-Item NotAcceptedExcel.txt| Out-Null
    mkdir all_excel_docs| Out-Null
    mkdir positive_results | Out-Null
    }
    "Create Dirs: Done"
    Create-Arrays
}

#Start Finding Files
function Find-Files 
{
    "Find Files: Start"
    #Loop to sort JPEG Files
    foreach ($JPEGitem in $JPEGfile)
    {
        $JPEGarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $JPEGitem.FullName}) | Out-Null
    }

    Foreach ($JPEGstring in $JPEGarray)
    {
        if ($JPEGstring -like "*``]*" -or $JPEGstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedJPEGName.txt"
            Add-Content $Dest $JPEGstring.Path
        }
        else{
            $Dest = $OutDir + "all_jpeg"
            Copy-Item -Path $JPEGfile.FullName -Destination $Dest
        }
    }
    "DONE: Jpeg"
    #Loop to sort png Files
    foreach ($PNGitem in $PNGfile)
    {
        $PNGarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $PNGitem.FullName}) | Out-Null
    }

    Foreach ($PNGstring in $PNGarray)
    {
        if ($PNGstring -like "*``]*" -or $PNGstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedPNGName.txt"
            Add-Content $Dest $PNGstring.Path
        }
        else{
            $Dest = $OutDir + "all_png"
            Copy-Item -Path $PNGfile.FullName -Destination $Dest
        }
    }
    "DONE: png"
    #Loop to sort BMP Files
    foreach ($BMPitem in $BMPfile)
    {
        $BMParray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $BMPitem.FullName}) | Out-Null
    }

    Foreach ($BMPstring in $BMParray)
    {
        if ($BMPstring -like "*``]*" -or $BMPstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedBMPName.txt"
            Add-Content $Dest $BMPstring.Path
        }
        else{
            $Dest = $OutDir + "all_bmp"
            Copy-Item -Path $BMPfile.FullName -Destination $Dest
        }
    }
    "DONE: bmp"
    #Loop to sort TIFF Files
    foreach ($TIFFitem in $TIFFfile)
    {
        $TIFFarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $TIFFitem.FullName}) | Out-Null
    }

    Foreach ($TIFFstring in $TIFFarray)
    {
        if ($TIFFstring -like "*``]*" -or $TIFFstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedTIFFName.txt"
            Add-Content $Dest $TIFFstring.Path
        }
        else{
            $Dest = $OutDir + "all_tiff"
            Copy-Item -Path $TIFFfile.FullName -Destination $Dest
        }
    }
    "DONE: tiff"
    #Loop to sort MP4 Files
    foreach ($MP4item in $MP4file)
    {
        $MP4array.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $MP4item.FullName}) | Out-Null
    }

    Foreach ($MP4string in $MP4array)
    {
        if ($MP4string -like "*``]*" -or $MP4string -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedMP4Name.txt"
            Add-Content $Dest $MP4string.Path
        }
        else{
            $Dest = $OutDir + "all_mp4"
            Copy-Item -Path $MP4file.FullName -Destination $Dest
        }
    }
    "DONE: mp4"
    #Loop to sort MP3 Files
    foreach ($MP3item in $MP3file)
    {
        $MP3array.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $MP3item.FullName}) | Out-Null
    }

    Foreach ($MP3string in $MP3array)
    {
        if ($MP3string -like "*``]*" -or $MP3string -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedMP3Name.txt"
            Add-Content $Dest $MP3string.Path
        }
        else{
            $Dest = $OutDir + "all_mp3"
            Copy-Item -Path $MP3file.FullName -Destination $Dest
        }
    }
    "DONE: mp3"
    #Loop to sort AVI Files
    foreach ($AVIitem in $AVIfile)
    {
        $AVIarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $AVIitem.FullName}) | Out-Null
    }

    Foreach ($AVIstring in $AVIarray)
    {
        if ($AVIstring -like "*``]*" -or $AVIstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedAVIName.txt"
            Add-Content $Dest $AVIstring.Path
        }
        else{
            $Dest = $OutDir + "all_avi"
            Copy-Item -Path $AVIfile.FullName -Destination $Dest
        }
    }
    "DONE: avi"
    #Loop to sort MSG Files
    foreach ($MSGitem in $MSGfile)
    {
        $MSGarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $MSGitem.FullName}) | Out-Null
    }

    Foreach ($MSGstring in $MSGarray)
    {
        if ($MSGstring -like "*``]*" -or $MSGstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedMSGName.txt"
            Add-Content $Dest $MSGstring.Path
        }
        else{
            $Dest = $OutDir + "all_msg"
            Copy-Item -Path $MSGfile.FullName -Destination $Dest
        }
    }
    "DONE: msg"
    #Loop to sort MOV Files
    foreach ($MOVitem in $MOVfile)
    {
        $MOVarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $MOVitem.FullName}) | Out-Null
    }

    Foreach ($MOVstring in $MOVarray)
    {
        if ($MOVstring -like "*``]*" -or $MOVstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedMOVName.txt"
            Add-Content $Dest $MOVstring.Path
        }
        else{
            $Dest = $OutDir + "all_mov"
            Copy-Item -Path $MOVfile.FullName -Destination $Dest
        }
    }
    "DONE: mov"
    #Loop to sort TXT Docs
    foreach ($TXTitem in $TXTfile)
    {
        $TXTarray.Add([pscustomobject]@{
            #ADD FILE PROPERTIES HERE TO DISPLAY MORE
            "Path" = $TXTitem.FullName}) | Out-Null
    }

    Foreach ($TXTstring in $TXTarray)
    {
        if ($TXTstring -like "*``]*" -or $TXTstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedTXTName.txt"
            Add-Content $Dest $TXTstring.Path
        }
        else{
            $Dest = $OutDir + "all_txt"
            Copy-Item -Path $TXTfile.FullName -Destination $Dest
        }
    }
    "DONE: txt"
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
            $Dest = $OutDir + "NotAcceptedPDFName.txt"
            Add-Content $Dest $PDFstring.Path
        }
        else{
            $Dest = $OutDir + "all_pdf"
            Copy-Item -Path $PDFfile.FullName -Destination $Dest
        }
    }
    "DONE: pdf"
    #Loop to sort Word
    foreach ($WORDitem in $WORDfile)
    {
        $WORDarray.Add([pscustomobject]@{
            "Path" = $WORDitem.FullName}) |Out-Null
    }

    Foreach ($WORDstring in $WORDfile)
    {
        if ($WORDstring -like "*``]*" -or $WORDstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedWord.txt"
            Add-Content $Dest $WORDstring.Path
        }
        else{
            $Dest = $OutDir + "all_word_docs"
            Copy-Item -Path $WORDfile.FullName -Destination $Dest
        }
    }
    "DONE: word"
    #Loop to sort Power Point
    foreach ($POWERPOINTitem in $POWERPOINTfile)
    {
        $POWERPOINTarray.Add([pscustomobject]@{
            "Path" = $POWERPOINTitem.FullName}) |Out-Null
    }

    Foreach ($POWERPOINTstring in $POWERPOINTfile)
    {
        if ($POWERPOINTstring -like "*``]*" -or $POWERPOINTstring -like "*``[*" ){    
            $Dest = $OutDir + "NotAcceptedPowepointName.txt"
            Add-Content $Dest $POWERPOINTstring.Path
        }
        else{
            $Dest = $OutDir + "all_powerpoint_docs"
            Copy-Item -Path $POWERPOINTfile.FullName -Destination $Dest
        }
    }
    "DONE: pptx"
    #Loop to sort Excel
    foreach ($EXCELitem in $EXCELfile)
    {
        $EXCELarray.Add([pscustomobject]@{
            "Path" = $EXCELitem.FullName}) |Out-Null
    }

    Foreach ($EXCELstring in $EXCELfile)
    {
        if ($EXCELstring -like "*``]*" -or $EXCELstring -like "*``[*" ){
            $Dest = $OutDir + "NotAcceptedExcel.txt"
            Add-Content $Dest $EXCELstring.Path
        }
        else{
            $Dest = $OutDir + "all_excel_docs"
            Copy-Item -Path $EXCELfile.FullName -Destination $Dest
        }
    }
    "DONE: excel"
    "Find Files: End"
    Analyse-Word-Docs
}

#Analys Word Docs
Function Analyse-Word-Docs 
{
    "Start: Analyse-Word-Docs"
    #Move to all_word_docs Directory
    $Word_Dir = $OutDir + "all_word_docs"
    cd $Word_Dir

    # New Array Names of our new zip files
    $doc_array = New-Object System.Collections.ArrayList
    # Modify extention of word documents zip
    Dir *.doc* | rename-item -newname { [io.path]::ChangeExtension($_.name, "zip") }

    #unzip documents
    Get-ChildItem $Word_Dir -Filter *.zip | foreach {
        $destination = Join-Path $_.DirectoryName ($_.BaseName)
        Expand-Archive $_.FullName -DestinationPath $destination
        $doc_array.Add($destination) | Out-Null
    }

    # Identify all unziped folders and put fullname into array
    # Loop through array and into the "word\document.xml" file
    # Check for classification keywords

    foreach ($i in $doc_array)
    {
        cd $Word_Dir
        $directoy = $i + '\word\document.xml' 
        $a = Get-Content -path $directoy
        foreach($line in Get-Content $Dirty_Words_file) {
            if ($a -like $line)
            {
                $file = $i + ".zip"
                Write-Host "accpting"
                Copy-Item -path $file -Destination $PosResultsDir -Recurse
            }
            cd $PosResultsDir
            Dir *.zip* | rename-item -newname { [io.path]::ChangeExtension($_.name, "docx") }
        }
        
    }
    "Done: Analyse-Word-Docs"
}

Create-Dirs

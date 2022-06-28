$Word = NEW-OBJECT –COMOBJECT WORD.APPLICATION  
# Acquire a list of DOCX files in a folder
$Files = GET-CHILDITEM -include *.pdf -exclude *_converted.pdf -recurse -path 'C:\Users\User\Downloads\malicious-pdf-analysis-ebook' # 'G:\bookz\lang\vba' # 'G:\bookz\office\access' # 
  
Foreach ($File in $Files) {
    try{
        write-host "Trying  " $File.fullname 
        # open a Word document, filename from the directory
        $Doc1=$Word.Documents.Open($File.fullname)
        write-host "Opening " $File.fullname ". RESULT=" + $?
        # Swap out PDF with DOCX in the Filename
        $Name=($File.Fullname).replace("pdf",“docx”) # $Name=($Doc1.Fullname).replace("pdf",“docx”)
        # Save this File as a PDF in Word 2010/2013 - hm, and 2016 fails? 
        $Doc1.saveas([ref] $Name, [ref] 16) # see WdSaveFormat enumeration : 16 is word default, 
    }
    catch 
    { 
        $ErrorMessage = $_.Exception.Message
        $FailedItem = $_.Exception.ItemName
        write-host "Caught error saving " $FailedItem ". Msg: " $ErrorMessage
    } 
    finally {
        $Doc1.close()
        [GC]::Collect() # watch me trying a number of things to get this to work with Word 2016... <img draggable="false" role="img" class="emoji" alt="🙂" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f642.svg">
        move-item -path $file.FullName -destination ($file.Directory.ToString() + "\" + $file.BaseName + "_converted" + $file.Extension)
    }
}
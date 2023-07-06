################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# Date: 05/2023
#
# 
# For Support and Sales Please Contact K&P Computer!
#
# E-Mail: hds@kpc.de
#
# 24/7 Helpdesk-Support:
# International: +800 4479 3300
# Germany: +49 6122 7071 330
# Austria: +43 1 525 1833
#
# Web Germany: https://www.kpc.de
# Web Austria: https://www.kpc.at
# Web International: https://www.kpc.de/en
#
################################################################################################################

$pshost = get-host
$pswindow = $pshost.ui.rawui

$newsize = $pswindow.buffersize
$newsize.height = 300
$newsize.width = 150
$pswindow.buffersize = $newsize


try
{
    $UpdateSession = New-Object -ComObject Microsoft.Update.Session
    $UpdateSearcher = $UpdateSession.CreateupdateSearcher()
    $Updates = @($UpdateSearcher.Search("IsHidden=0 and IsInstalled=0").Updates)

    if ($Updates -and $Updates.count -gt 0)
    {

        $Mandatorycount=0
        $Mandatoryupdates=""
        $Optionalcount=0
        $Optionalupdates=""
        $Criticalcount=0
        $Criticalupdates=""
        $Importantcount=0
        $Importantupdates=""
        $Lowcount=0
        $Lowupdates=""
        $Moderatecount=0
        $Moderateupdates=""
        $Unspecifiedcount=0
        $Unspecifiedupdates=""
    
        foreach ($Update in $Updates)
        {
            if ($Update.IsMandatory -eq 1)
            {
                $Mandatoryupdates = $Mandatoryupdates + $Update.Title + "XXXNEWLINEXXX"
                $Mandatorycount++
            }
            if ($Update.IsMandatory -eq 0)
            {
                $Optionalupdates = $Optionalupdates + $Update.Title + "XXXNEWLINEXXX"
                $Optionalcount++
            }
            if ($Update.MsrcSeverity -eq "Critical")
            {
                $Criticalupdates = $Criticalupdates + $Update.Title + "XXXNEWLINEXXX"
                $Criticalcount++
            }
            if ($Update.MsrcSeverity -eq "Important")
            {
                $Importantupdates = $Importantupdates + $Update.Title + "XXXNEWLINEXXX"
                $Importantcount++
            }
            if ($Update.MsrcSeverity -eq "Low")
            {
                $Lowupdates = $Lowupdates + $Update.Title + "XXXNEWLINEXXX"
                $Lowcount++
            }
            if ($Update.MsrcSeverity -eq "Moderate")
            {
                $Moderateupdates = $Moderateupdates + $Update.Title  + "XXXNEWLINEXXX"
                $Moderatecount++
            }
            if ($Update.MsrcSeverity -eq $null)
            {
                $Unspecifiedupdates = $Unspecifiedupdates + $Update.Title + "XXXNEWLINEXXX"
                $Unspecifiedcount++
            }
        }
    $output = "<<<windows_updates_kpc:sep(15)>>>`n"
    $output = "$output" + "$Mandatorycount" + "`t" + "$Optionalcount" + "`t" + "$Criticalcount" + "`t" + "$Importantcount" + "`t" + "$Lowcount" + "`t" + "$Moderatecount" + "`t" + "$Unspecifiedcount" + "`t" + "$Mandatoryupdates" + "`t" + "$Optionalupdates" + "`t" + "$Criticalupdates" + "`t" + "$Importantupdates" + "`t" + "$Lowupdates" + "`t" + "$Moderateupdates" + "`t" + "$Unspecifiedupdates"
    write-host $output

}

}
catch
{
$errMsg = $_.Exception.Message
$errItem = $_.Exception.ItemName
Write-Error "Totally unexpected and unhandled error occured:`n Item: $errItem`n Error Message: $errMsg"
Break
}

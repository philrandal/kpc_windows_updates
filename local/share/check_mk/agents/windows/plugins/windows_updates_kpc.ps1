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

if ($Updates -and $Updates.count -gt 0){

$Mandatorycount=0
$Optionalcount=0
$Criticalcount=0
$Importantcount=0
$Lowcount=0
$Moderatecount=0
$Unspecifiedcount=0

foreach ($Update in $Updates)
    {
    
        $jobName = $Update.Title
        $jobID = $Update.IsMandatory
        $lastResult = $Update.IsHidden
        $lastState = $Update.IsInstalled
        $MsrcSeverity = $Update.MsrcSeverity

        if ($Update.IsMandatory -eq 1){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Mandatorycount++
        }
        if ($Update.IsMandatory -eq 0){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Optionalcount++
        }
        if ($Update.MsrcSeverity -eq "Critical"){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Criticalcount++
        }
        if ($Update.MsrcSeverity -eq "Important"){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Importantcount++
        }
        if ($Update.MsrcSeverity -eq "Low"){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Lowcount++
        }
        if ($Update.MsrcSeverity -eq "Moderate"){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Moderatecount++
        }
        if ($Update.MsrcSeverity -eq $null){
        write-host "$jobName|$jobID|$lastResult|$lastState|$MsrcSeverity"
        $Unspecifiedcount++
        }
    }
write-host $Mandatorycount
write-host $Optionalcount
write-host $Criticalcount
write-host $Importantcount
write-host $Lowcount
write-host $Moderatecount
write-host $Unspecifiedcount


    #$Updates | Select Title, IsMandatory, IsHidden, IsInstalled
    #$Updates | Select-Object Title, MsrcSeverity, IsHidden
}
else { Write-Output "No updates found. Exiting..." }

}
catch
{
$errMsg = $_.Exception.Message
$errItem = $_.Exception.ItemName
Write-Error "Totally unexpected and unhandled error occured:`n Item: $errItem`n Error Message: $errMsg"
Break
}

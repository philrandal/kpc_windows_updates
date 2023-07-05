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

if ($Updates.Updates -and $Updates.Updates.count -gt 0){
    $count=$Updates.Updates.count
    $Updates | Select Title, IsMandatory
    #$Updates | Select-Object Title, MsrcSeverity
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

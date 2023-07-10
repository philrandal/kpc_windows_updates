# KPC Windows Update Check for CheckMK
<p align="center"><img src="https://user-images.githubusercontent.com/5358267/235710289-c05aa5bb-3394-4c94-8ce0-1f0ef5382d00.png"></p>
<p align="center">#Powered by K&P Computer - www.kpc.de</o>

----------------------

### Available .mkp Package Releases: ###

https://github.com/matthias1232/kpc_windows_updates/releases


----------------------

### Windows Update Checks for CheckMK ###
 
This Package contains a new PowerShell Check to Check the System for new Available Windows Updates

Features:
- Checking for available Windows Updates with a Powershell Script
- Individual WARN/CRIT Level settings for each type of Updates (Mandatory, Critical, Important, Moderate, Low, Unspecified Severity)
- Showing all available Updates in Detailed Summary
- Check for Windows Update History. Shows the last time when this System installed an Windows Update and also the List of the last 50 installed updates in the summary details.
- Warn/Crit level Settings if the System did not install any update during the last X days.
- Included in Agent Rules for Agent bakery




### Added default Agent execution Settings for the Windows Agent Plugin (Agent Bakery): ###
- Default cache interval of 3 Hours
- Default asynchronous execution
- Default execution timeout of 600 Seconds

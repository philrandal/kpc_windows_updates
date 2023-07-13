# KPC Windows Update Check for CheckMK
<p align="center"><img src="https://user-images.githubusercontent.com/5358267/235710289-c05aa5bb-3394-4c94-8ce0-1f0ef5382d00.png"></p>
<p align="center">#Powered by K&P Computer - www.kpc.de</o>

----------------------

### Available .mkp Package Releases: ###

https://github.com/matthias1232/kpc_windows_updates/releases


----------------------

### Windows Update Checks for CheckMK ###
 
Features:
- Checking for available Windows Updates sorted by Severity
- Individual WARN/CRIT Level settings for each type of Updates (Mandatory, Critical, Important, Moderate, Low, Unspecified Severity)
- Pending Reboot Check after Update Installation with WARN/CRIT Level Settings
- CRIT Error if Update Search does not work for a while (Windows update not activated, WSUS Problem etc..)
- Showing all available Updates in Detailed Summary
- Check for Windows Update History. Shows the last time when this System installed an Windows Update and also the List of up to the last 80 installed updates in the summary details. (Intelligence Updates are excepted)
- Warn/Crit level Settings if the System did not install any update during the last X days.
- Included in Agent Rules for Agent bakery
- No VBS Scripts anymore, only Powershell will be used
- Tested with Windows 2012R2/2016/2019/2022





### Added default Agent execution Settings for the Windows Agent Plugin (Agent Bakery): ###
- Default cache interval of 3 Hours
- Default asynchronous execution
- Default execution timeout of 600 Seconds

### Screenshots: ###
![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/5449b5a2-e922-4119-9cd0-b6750c4e63f6)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/653887ce-c538-47f2-a3e8-61ba2479311d)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/87e17756-65ab-42c3-8a55-2b8b1bad6e07)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/fba740aa-c991-482c-a2e6-40239b28d9ff)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/710a6994-1470-4e76-93fb-4f514d611bdb)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/4cefbcb2-cbbb-4708-ac9d-6c40481794c0)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/8bccc33c-a0dc-48be-a43e-0ed66a04c71c)




# KPC Windows Update Check for CheckMK
<p align="center"><img src="https://user-images.githubusercontent.com/5358267/235710289-c05aa5bb-3394-4c94-8ce0-1f0ef5382d00.png"></p>
<p align="center">#Powered by K&P Computer - www.kpc.de</o>

----------------------

### Available .mkp Package Releases: ###

https://github.com/matthias1232/kpc_windows_updates/releases


----------------------

### Windows Update Checks for CheckMK ###
 
Features:
- Check for available Windows Updates (Important and Optional)
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
![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/7db9b335-8148-446c-9e39-f31342dd78ca)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/4e69c19d-3b33-4fcf-8f66-0c65c0e4443c)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/e098c9b3-31c9-4b01-b693-0e75c2cddd2d)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/4cefbcb2-cbbb-4708-ac9d-6c40481794c0)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/1c48c17a-be81-4b97-a597-69d6b1543447)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/8bccc33c-a0dc-48be-a43e-0ed66a04c71c)




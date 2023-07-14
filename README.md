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
- Default execution timeout of 1 hour (long time needet for some older systems sometimes)

### Screenshots: ###
![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/9d1e0e3f-61fc-49e9-a527-72ca23fbd15f)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/fdd7d13a-c29b-4835-aa7d-9610f7b6403c)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/e098c9b3-31c9-4b01-b693-0e75c2cddd2d)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/4cefbcb2-cbbb-4708-ac9d-6c40481794c0)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/041ee4e7-39d1-4639-bdd1-0c66a38c1b35)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/8bccc33c-a0dc-48be-a43e-0ed66a04c71c)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/9b979558-cc79-493b-b4b0-3f3867bd1e4a)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/d626ee0e-5c96-465a-baa2-f2ed869ec210)






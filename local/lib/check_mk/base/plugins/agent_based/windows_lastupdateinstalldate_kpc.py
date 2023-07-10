#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# Copyright (C) 2023 K&P Computer Service- und Vertriebs-GmbH - License: GNU General Public License v2
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



#<<<windows_lastupdateinstalldate_kpc:sep(9):cached(1688714200,3600)>>>
#1688584264 07/05/2023 19:11:04 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3675.0)XXXNEWLINEXXX07/04/2023 19:11:08 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3559.0)XXXNEWLINEXXX07/03/2023 19:02:09 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3451.0)XXXNEWLINEXXX07/03/2023 18:32:29 2023-06 Cumulative Update for Microsoft server operating system version 21H2 for x64-based Systems (KB5027225)XXXNEWLINEXXX07/03/2023 18:12:22 2023-06 Cumulative Update for Microsoft server operating system version 21H2 for x64-based Systems (KB5027225)XXXNEWLINEXXX07/03/2023 18:10:46 2023-06 Cumulative Update for .NET Framework 3.5, 4.8 and 4.8.1 for Microsoft server operating system version 21H2 for x64 (KB5027544)XXXNEWLINEXXX07/03/2023 18:10:18 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3440.0)XXXNEWLINEXXX07/03/2023 18:10:09 2022-08 Security Update for Microsoft server operating system version 21H2 for x64-based Systems (KB5012170)XXXNEWLINEXXX07/03/2023 18:09:43 XXXNEWLINEXXX


support = "For Support and Sales Please Contact K&P Computer! \n \n E-Mail: hds@kpc.de \n \n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"


from .agent_based_api.v1 import *
import pprint
from datetime import datetime, timedelta


def discover_windows_lastupdateinstalldate_kpc(section):
    for jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdatelist in section:  
        yield Service(item=jobname_windows_lastupdateinstalldate_kpc)


def check_windows_lastupdateinstalldate_kpc(item, section):

    for line in section:
        if len(line) < 3:
            continue  # Skip incomplete lines

        jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdatelist = line[
            :3
        ]

        if (lastupdatelist == "-"):
            lastupdatelist = ""

        lastupdateinstalldate  = int(lastupdateinstalldate)
        lastupdateinstalldate = datetime.utcfromtimestamp(lastupdateinstalldate).strftime('%Y-%m-%d %H:%M:%S')

        lastupdatelist = lastupdatelist .replace("XXXNEWLINEXXX", "\n")
        lastupdatelist = "\n \n" + lastupdatelist + "\n \n \n" + support
        if jobname_windows_lastupdateinstalldate_kpc != item:
            continue  # Skip not matching lines


        state = State.OK
        summarytext= "Last installation of Windows Updates: " + lastupdateinstalldate
        summarydetails = "Update History:" + lastupdatelist + support

        yield Result(
             state=state,
             summary=f"{summarytext}",
             details = summarydetails )

register.check_plugin(
    name = "windows_lastupdateinstalldate_kpc",
    service_name = "KPC %s",
    discovery_function = discover_windows_lastupdateinstalldate_kpc,
    check_function = check_windows_lastupdateinstalldate_kpc,
)

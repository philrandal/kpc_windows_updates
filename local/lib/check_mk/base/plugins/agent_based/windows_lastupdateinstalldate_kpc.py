#!/usr/bin/env python3
# -*- coding: cp437 -*-
# Copyright (C) 2023 K&P Computer Service- und Vertriebs-GmbH - License: GNU General Public License v2
################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# Date: 07/2023
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


#<<<windows_lastupdateinstalldate_kpc:sep(9):encoding(cp437)>>>
#Windows Update History	07/09/2023 19:11:05	1	07/09/2023 19:11:05 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.4052.0)XXXNEWLINEXXX07/08/2023 19:14:01 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3953.0)

support = "For Support and Sales Please Contact K&P Computer! \n \n E-Mail: hds@kpc.de \n \n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"


from .agent_based_api.v1 import *
import pprint
from datetime import datetime, timedelta


def discover_windows_lastupdateinstalldate_kpc(section):
    for jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdatelist in section:  
        yield Service(item=jobname_windows_lastupdateinstalldate_kpc)


def check_windows_lastupdateinstalldate_kpc(item, params, section):

    warn = params["warning_lower"][0]
    crit = params["warning_lower"][1]

    for line in section:
        if len(line) < 3:
            continue  # Skip incomplete lines

        jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdatelist = line[
            :3
        ]

        if (lastupdatelist == "-"):
            lastupdatelist = ""

        now = datetime.now()
        lastupdateinstalldate_convert = datetime.datetime.fromtimestamp(round(lastupdateinstalldate / 1000))
        datedifference = datetime.now() - lastupdateinstalldate_convert
        datedifference_days = int(datedifference.days)


        lastupdateinstalldate  = int(lastupdateinstalldate)
        lastupdateinstalldate = datetime.utcfromtimestamp(lastupdateinstalldate).strftime('%Y-%m-%d %H:%M:%S')

        lastupdatelist = lastupdatelist .replace("XXXNEWLINEXXX", "\n")
        lastupdatelist = "\n \n" + lastupdatelist + "\n \n \n" + support
        if jobname_windows_lastupdateinstalldate_kpc != item:
            continue  # Skip not matching lines


        state = State.OK
        summarytext= "Last installation of Windows Updates: " + lastupdateinstalldate + " (" + datedifference_days + " days ago)"
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
    check_default_parameters={'warning_lower' : (30,50)},
    check_ruleset_name="windows_updates_kpc_windows_lastupdateinstalldate",
)

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

#<<<windows_updates_kpc:sep(9):encoding(cp437)>>>
#Windows Updates	0	5	0	0	0	0	5	-	Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.4146.0)XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXX	-		-	-	Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.4146.0)XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXXINTEL - System - 1/1/1970 12:00:00 AM - 10.1.1.42XXXNEWLINEXXX

from .agent_based_api.v1 import *
import pprint
from datetime import datetime, timedelta


def discover_windows_updates_kpc(section):
    for jobname_windows_updates_kpc, Mandatorycount, Optionalcount, Criticalcount, Importantcount, Moderatecount, Lowcount, Unspecifiedcount, Mandatoryupdates, Optionalupdates, Criticalupdates, Importantupdates, Lowupdates, Moderateupdates, Unspecifiedupdates in section:  
        yield Service(item=jobname_windows_updates_kpc)


def check_windows_updates_kpc(item, params, section):

    mandatorywarn = params["warning_lower"][0]
    mandatorycrit = params["warning_lower"][1]
    criticalwarn = params["warning_lower"][2]
    criticalcrit = params["warning_lower"][3]
    importantwarn = params["warning_lower"][4]
    importantcrit = params["warning_lower"][5]
    moderatewarn = params["warning_lower"][6]
    moderatecrit = params["warning_lower"][7]
    lowwarn = params["warning_lower"][8]
    lowcrit = params["warning_lower"][9]
    unspecifiedwarn = params["warning_lower"][10]
    unspecifiedcrit = params["warning_lower"][11]


    for line in section:
        if len(line) < 15:
            continue  # Skip incomplete lines

        jobname_windows_updates_kpc, Mandatorycount, Optionalcount, Criticalcount, Importantcount, Moderatecount, Lowcount, Unspecifiedcount, Mandatoryupdates, Optionalupdates, Criticalupdates, Importantupdates, Lowupdates, Moderateupdates, Unspecifiedupdates = line[
            :15
        ]

        if (Mandatoryupdates  == "-"):
            Mandatoryupdates = ""
        if (Criticalupdates  == "-"):
            Criticalupdates = ""
        if (Importantupdates  == "-"):
            Importantupdates = ""
        if (Moderateupdates  == "-"):
            Moderateupdates = ""
        if (Lowupdates  == "-"):
            Lowupdates = ""
        if (Unspecifiedupdates  == "-"):
            Unspecifiedupdates = ""

        updatelist ="\n \n "

        if (Mandatoryupdates != ""):
             Mandatoryupdates = Mandatoryupdates.replace("XXXNEWLINEXXX", "\n")
             Mandatoryupdates = "Mandatory Updates: \n \n" + Mandatoryupdates + "\n \n \n"

        if (Criticalupdates != ""):
             Criticalupdates = Criticalupdates.replace("XXXNEWLINEXXX", "\n")
             Criticalupdates = "Critical Severity: \n \n" + Criticalupdates + "\n \n \n"

        if (Importantupdates != ""):
             Importantupdates = Importantupdates.replace("XXXNEWLINEXXX", "\n")
             Importantupdates = "Important Severity: \n \n" + Importantupdates + "\n \n \n"

        if (Moderateupdates != ""):
             Moderateupdates = Moderateupdates.replace("XXXNEWLINEXXX", "\n")
             Moderateupdates  = "Moderate Severity: \n \n" + Moderateupdates + "\n \n \n"

        if (Lowupdates != ""):
             Lowupdates = Lowupdates.replace("XXXNEWLINEXXX", "\n")
             Lowupdates = "Low Severity: \n \n" + Lowupdates + "\n \n \n"

        if (Unspecifiedupdates != ""):
             Unspecifiedupdates = Unspecifiedupdates.replace("XXXNEWLINEXXX", "\n")
             Unspecifiedupdates = "Unspecified Severity: \n \n" + Unspecifiedupdates

        support = "\n \n \n For Support and Sales Please Contact K&P Computer! \n \n E-Mail: hds@kpc.de \n \n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"


        if jobname_windows_updates_kpc != item:
            continue  # Skip not matching lines

        state = ""
        statemandatory = " (OK)"
        statecritical = " (OK)"
        stateimportant = " (OK)"
        statemoderate = " (OK)"
        statelow = " (OK)"
        stateunspecified = " (OK)"


        if int(Mandatorycount) >= int(mandatorywarn):
             statemandatory = " (WARN)"
        if int(Mandatorycount) >= int(mandatorycrit):
             statemandatory = " (CRIT)"
        if int(Criticalcount) >= int(criticalwarn):
             statecritical = " (WARN)"
        if int(Criticalcount) >= int(criticalcrit):
             statecritical = " (CRIT)"
        if int(Importantcount) >= int(importantwarn):
             stateimportant = " (WARN)"
        if int(Importantcount) >= int(importantcrit):
             stateimportant = " (CRIT)"
        if int(Moderatecount) >= int(moderatewarn):
             statemoderate = " (WARN)"
        if int(Moderatecount) >= int(moderatecrit):
             statemoderate = " (CRIT)"
        if int(Lowcount) >= int(lowwarn):
             statelow = " (WARN)"
        if int(Lowcount) >= lowcrit:
             statelow = " (CRIT)"
        if int(Unspecifiedcount) >= int(unspecifiedwarn):
             stateunspecified = " (WARN)"
        if int(Unspecifiedcount) >= int(unspecifiedcrit):
             stateunspecified = " (CRIT)"


        if int(Mandatorycount) >= int(mandatorywarn) and state != State.CRIT:
             state = State.WARN
        if int(Mandatorycount) >= int(mandatorycrit):
             state = State.CRIT
        if int(Criticalcount) >= int(criticalwarn) and state != State.CRIT:
             state = State.WARN
        if int(Criticalcount) >= int(criticalcrit):
             state = State.CRIT
        if int(Importantcount) >= int(importantwarn) and state != State.CRIT:
             state = State.WARN
        if int(Importantcount) >= int(importantcrit):
             state = State.CRIT
        if int(Moderatecount) >= int(moderatewarn) and state != State.CRIT:
             state = State.WARN
        if int(Moderatecount) >= int(moderatecrit):
             state = State.CRIT
        if int(Lowcount) >= int(lowwarn) and state != State.CRIT:
             state = State.WARN
        if int(Lowcount) >= lowcrit:
             state = State.CRIT
        if int(Unspecifiedcount) >= int(unspecifiedwarn) and state != State.CRIT:
             state = State.WARN
        if int(Unspecifiedcount) >= int(unspecifiedcrit):
             state = State.CRIT
        if state != State.WARN and state != State.CRIT:
             state = State.OK


        summarytext= "Mandatory: " + Mandatorycount + statemandatory + ", Critical: " + Criticalcount + statecritical + ", Important: " + Importantcount + stateimportant + ", Moderate: " + Moderatecount + statemoderate + ", Low: " + Lowcount + statelow + ", Unspecified: " + Unspecifiedcount + stateunspecified 
        summarydetails = updatelist + Mandatoryupdates + Criticalupdates + Importantupdates + Moderateupdates + Lowupdates + Unspecifiedupdates + support

        yield Result(
             state=state,
             summary=f"{summarytext}",
             details = summarydetails )

register.check_plugin(
    name = "windows_updates_kpc",
    service_name = "KPC %s",
    discovery_function = discover_windows_updates_kpc,
    check_function = check_windows_updates_kpc,
    check_default_parameters={'warning_lower' : (1,2,1,2,1,2,1,2,1,2,1,2)},
    check_ruleset_name="windows_updates_kpc_windows_updates",
)

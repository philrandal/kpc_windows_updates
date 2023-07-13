#!/usr/bin/env python3
# Copyright (C) 2023 K&P Computer Service- und Vertriebs-GmbH - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Matthias Binder m.binder@kpc.de, July 2023
#
################################################################################################################
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
    for jobname_windows_updates_kpc, Mandatorycount, important1count, Optionalcount, Criticalcount, Importantcount, Moderatecount, Lowcount, Unspecifiedcount, rebootrequired, rebootrequiredsince, rebootrequiredsincehours, updatesearcherror, Mandatoryupdates, important1updates, Optionalupdates, Criticalupdates, Importantupdates, Lowupdates, Moderateupdates, Unspecifiedupdates in section:  
        yield Service(item=jobname_windows_updates_kpc)


def check_windows_updates_kpc(item, params, section):
    
    important1warn = params["levels_important1"][0]
    important1crit = params["levels_important1"][1]
    important1enabled = params["levels_important1"][2]
    optionalwarn = params["levels_optional"][0]
    optionalcrit = params["levels_optional"][1]
    optionalenabled = params["levels_optional"][2]    
    mandatorywarn = params["levels_mandatory"][0]
    mandatorycrit = params["levels_mandatory"][1]
    mandatoryenabled = params["levels_mandatory"][2]
    criticalwarn = params["levels_critical"][0]
    criticalcrit = params["levels_critical"][1]
    criticalenabled = params["levels_critical"][2]
    importantwarn = params["levels_important"][0]
    importantcrit = params["levels_important"][1]
    importantenabled = params["levels_important"][2]
    moderatewarn = params["levels_moderate"][0]
    moderatecrit = params["levels_moderate"][1]
    moderateenabled = params["levels_moderate"][2]
    lowwarn = params["levels_low"][0]
    lowcrit = params["levels_low"][1]
    lowenabled = params["levels_low"][2]
    unspecifiedwarn = params["levels_unspecified"][0]
    unspecifiedcrit = params["levels_unspecified"][1]
    unspecifiedenabled = params["levels_unspecified"][2]
    pendingrebootwarn = params["levels_pendingreboot"][0]
    pendingrebootcrit = params["levels_pendingreboot"][1]
    pendingrebootenabled = params["levels_pendingreboot"][2]


    for line in section:
        if len(line) < 21:
            continue  # Skip incomplete lines

        jobname_windows_updates_kpc, Mandatorycount, important1count, Optionalcount, Criticalcount, Importantcount, Moderatecount, Lowcount, Unspecifiedcount, rebootrequired, rebootrequiredsince, rebootrequiredsincehours, updatesearcherror, Mandatoryupdates, important1updates, Optionalupdates, Criticalupdates, Importantupdates, Lowupdates, Moderateupdates, Unspecifiedupdates = line[
            :21
        ]
        if (important1updates  == "-"):
            important1updates = ""        
        if (Optionalupdates  == "-"):
            Optionalupdates = ""
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
        
        if (important1updates != ""):
             important1updates = important1updates.replace("XXXNEWLINEXXX", "\n")
             important1updates = "Important Updates: \n \n" + important1updates + "\n \n \n"
            
        if (Optionalupdates != ""):
             Optionalupdates = Optionalupdates.replace("XXXNEWLINEXXX", "\n")
             Optionalupdates = "Optional Updates: \n \n" + Optionalupdates + "\n \n \n"    
            
        if (Mandatoryupdates != ""):
             Mandatoryupdates = Mandatoryupdates.replace("XXXNEWLINEXXX", "\n")
             Mandatoryupdates = "Mandatory Severity: \n \n" + Mandatoryupdates + "\n \n \n"

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
        stateimportant1 = " (OK)"   
        stateoptional = " (OK)"
        statemandatory = " (OK)"
        statecritical = " (OK)"
        stateimportant = " (OK)"
        statemoderate = " (OK)"
        statelow = " (OK)"
        stateunspecified = " (OK)"
        statependingreboot = " (OK)"

        if int(important1count) >= int(important1warn):
             stateimportant1 = " (WARN)"
        if int(important1count) >= int(important1crit):
             stateimportant1 = " (CRIT)"
        if int(Optionalcount) >= int(optionalwarn):
             stateoptional = " (WARN)"
        if int(Optionalcount) >= int(optionalcrit):
             stateoptional = " (CRIT)"
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
        if int(rebootrequiredsincehours) > 0:
             statependingreboot = " (OK, since " + rebootrequiredsincehours + " hours)"
        if int(rebootrequiredsincehours) >= int(pendingrebootwarn):
             statependingreboot = " (WARN, since " + rebootrequiredsincehours + " hours)"
        if int(rebootrequiredsincehours) >= int(pendingrebootcrit):
             statependingreboot = " (CRIT, since " + rebootrequiredsincehours + " hours)"

        
        if int(important1count) >= int(important1warn) and state != State.CRIT and important1enabled == 'Enabled':
             state = State.WARN
        if int(important1count) >= int(important1crit) and important1enabled == 'Enabled':
             state = State.CRIT
        if int(Optionalcount) >= int(optionalwarn) and state != State.CRIT and optionalenabled == 'Enabled':
             state = State.WARN
        if int(Optionalcount) >= int(optionalcrit) and optionalenabled == 'Enabled':
             state = State.CRIT
        if int(Mandatorycount) >= int(mandatorywarn) and state != State.CRIT and mandatoryenabled == 'Enabled':
             state = State.WARN
        if int(Mandatorycount) >= int(mandatorycrit) and mandatoryenabled == 'Enabled':
             state = State.CRIT
        if int(Criticalcount) >= int(criticalwarn) and state != State.CRIT and criticalenabled == 'Enabled':
             state = State.WARN
        if int(Criticalcount) >= int(criticalcrit) and criticalenabled == 'Enabled':
             state = State.CRIT
        if int(Importantcount) >= int(importantwarn) and state != State.CRIT and importantenabled == 'Enabled':
             state = State.WARN
        if int(Importantcount) >= int(importantcrit) and importantenabled == 'Enabled':
             state = State.CRIT
        if int(Moderatecount) >= int(moderatewarn) and state != State.CRIT and moderatenabled == 'Enabled':
             state = State.WARN
        if int(Moderatecount) >= int(moderatecrit) and moderatenabled == 'Enabled':
             state = State.CRIT
        if int(Lowcount) >= int(lowwarn) and state != State.CRIT and lowenabled == 'Enabled':
             state = State.WARN
        if int(Lowcount) >= lowcrit and lowenabled == 'Enabled':
             state = State.CRIT
        if int(Unspecifiedcount) >= int(unspecifiedwarn) and state != State.CRIT and unspecifiedenabled == 'Enabled':
             state = State.WARN
        if int(Unspecifiedcount) >= int(unspecifiedcrit) and unspecifiedenabled == 'Enabled':
             state = State.CRIT
        if int(rebootrequiredsincehours) >= int(pendingrebootwarn) and state != State.CRIT and pendingrebootenabled == 'Enabled':
             state = State.WARN
        if int(rebootrequiredsincehours) >= int(pendingrebootcrit) and pendingrebootenabled == 'Enabled':
             state = State.CRIT
        if state != State.WARN and state != State.CRIT:
             state = State.OK

        
         
        
        if important1enabled == 'Disabled':
             stateimportant1 = " (OK)"   
        if optionalenabled == 'Disabled':
             stateoptional = " (OK)"
        if mandatoryenabled == 'Disabled':
             statemandatory = " (OK)"
        if criticalenabled == 'Disabled':
             statecritical = " (OK)"
        if importantenabled == 'Disabled':
             stateimportant = " (OK)"
        if moderateenabled == 'Disabled':
             statemoderate = " (OK)"
        if lowenabled == 'Disabled':
             statelow = " (OK)"
        if unspecifiedenabled == 'Disabled':
             stateunspecified = " (OK)"
        if pendingrebootenabled == 'Disabled':
             statependingreboot = " (OK)"
        if pendingrebootenabled == 'Disabled' and int(rebootrequiredsincehours) > 0:
             statependingreboot = " (OK, since " + rebootrequiredsincehours + " hours)"



        summarytext= "Important Updates: " + important1count + stateimportant1 + ", Optional Updates: " + Optionalcount + stateoptional + ", Mandatory Severity: " + Mandatorycount + statemandatory + ", Critical Severity: " + Criticalcount + statecritical + ", Important Severity: " + Importantcount + stateimportant + ", Moderate Severity: " + Moderatecount + statemoderate + ", Low Severity: " + Lowcount + statelow + ", Unspecified Severity: " + Unspecifiedcount + stateunspecified + ", Pending reboot: " + rebootrequired + statependingreboot
        summarydetails = updatelist + important1updates + Optionalupdates + Mandatoryupdates + Criticalupdates + Importantupdates + Moderateupdates + Lowupdates + Unspecifiedupdates + support

        if (updatesearcherror != "0"):
            state=State.CRIT
            summarytext= str(updatesearcherror)
            summarydetails = " "

        
        yield Result(
             state=state,
             summary=f"{summarytext}",
             details = summarydetails )

register.check_plugin(
    name = "windows_updates_kpc",
    service_name = "KPC %s",
    discovery_function = discover_windows_updates_kpc,
    check_function = check_windows_updates_kpc,
    check_default_parameters={'levels_important1' : (1,1,'Enabled'),'levels_optional' : (1,99,'Enabled'),'levels_mandatory' : (1,1,'Disabled'),'levels_critical' : (1,1,'Disabled'),'levels_important' : (1,6,'Disabled'),'levels_moderate' : (1,10,'Disabled'),'levels_low' : (1,99,'Disabled'),'levels_unspecified' : (1,99,'Disabled'),'levels_pendingreboot' : (48,96,'Enabled')},
    check_ruleset_name="windows_updates_kpc_windows_updates",
)

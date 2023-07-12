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

from cmk.gui.i18n import _

# import required to register agent
from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
    CheckParameterRulespecWithoutItem,
    RulespecGroupCheckParametersApplications
)

from cmk.gui.valuespec import (
    FixedValue,
    TextInput,
    Age,
    ListOfStrings,
    DropdownChoice, 
)

# import structure where special agent will be registered
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms



 
def _parameter_valuespec_windows_updates_kpc_windows_updates():
    return Dictionary(
        elements=[
            ("warning_lower", Tuple(
                title=_("Levels for Windows Updates"),
                elements=[
                    Integer(title=_("Mandatory Severity Warning"), default_value=1),
                    Integer(title=_("Mandatory Severity Critical"), default_value=2),
                    Integer(title=_("Critical Severity Warning"), default_value=1),
                    Integer(title=_("Critical Severity Critical"), default_value=2),
                    Integer(title=_("Important Severity Warning"), default_value=1),
                    Integer(title=_("Important Severity Critical"), default_value=2),
                    Integer(title=_("Moderate Severity Warning"), default_value=1),
                    Integer(title=_("Moderate Severity Critical"), default_value=2),
                    Integer(title=_("Low Severity Warning"), default_value=1),
                    Integer(title=_("Low Severity Critical"), default_value=2),
                    Integer(title=_("Unspecified Severity Warning"), default_value=1),
                    Integer(title=_("Unspecified Severity Critical"), default_value=2),
                ],
            )),
        ],
    )
   
        
rulespec_registry.register(
CheckParameterRulespecWithoutItem(
check_group_name="windows_updates_kpc_windows_updates",
group=RulespecGroupCheckParametersApplications,
parameter_valuespec=_parameter_valuespec_windows_updates_kpc_windows_updates,
title=lambda: _("Windows Updates (KPC)"),
))

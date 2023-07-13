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

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
   HostRulespec,
   rulespec_registry,
)
from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import RulespecGroupMonitoringAgentsAgentPlugins
from cmk.gui.valuespec import (
   Age,
   Dictionary,
   TextAscii,
   DropdownChoice,
)

def _valuespec_windows_updates_kpc():
    return DropdownChoice(
        title=_('Windows Updates KPC'),
        help=_('This will deploy the agent plugin <tt>windows_updates_kpc.ps1</tt> '
               'for checking for available Windows Updates'),
        choices=[
            (True, _('Deploy plugin for Windows Updates (KPC)')),
            (None, _('Do not deploy plugin for Windows Updates (KPC)')),
        ],
    )


rulespec_registry.register(
   HostRulespec(
      group=RulespecGroupMonitoringAgentsAgentPlugins,
      name="agent_config:windows_updates_kpc",
      valuespec=_valuespec_windows_updates_kpc,
   ))

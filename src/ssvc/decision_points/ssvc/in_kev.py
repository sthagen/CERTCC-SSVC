#!/usr/bin/env python
"""
Provides a decision point representing whether a vulnerability is in the CISA Known Exploited Vulnerabilities (KEV) list.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

YES = DecisionPointValue(
    name="Yes",
    key="Y",
    description="Vulnerability is listed in KEV.",
)

NO = DecisionPointValue(
    name="No",
    key="N",
    description="Vulnerability is not listed in KEV.",
)

IN_KEV_1 = SsvcDecisionPoint(
    name="In KEV",
    description="Denotes whether a vulnerability is in the CISA Known Exploited Vulnerabilities (KEV) list.",
    key="KEV",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)

VERSIONS = (IN_KEV_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

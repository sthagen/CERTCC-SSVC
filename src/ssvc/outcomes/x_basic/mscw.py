#!/usr/bin/env python
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University
"""
Provides the MSCW (Must, Should, Could, Won't) outcome group for the `x_basic` namespace
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

_WONT = DecisionPointValue(name="Won't", key="W", description="Won't")

_COULD = DecisionPointValue(name="Could", key="C", description="Could")

_SHOULD = DecisionPointValue(name="Should", key="S", description="Should")

_MUST = DecisionPointValue(name="Must", key="M", description="Must")

MSCW = DecisionPoint(
    name="MoSCoW",
    key="MSCW",
    description="The MoSCoW (Must, Should, Could, Won't) outcome group.",
    version="1.0.0",
    namespace="x_basic",
    values=(
        _WONT,
        _COULD,
        _SHOULD,
        _MUST,
    ),
)
"""
The MoSCoW outcome group.
"""

VERSIONS = (MSCW,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

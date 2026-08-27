"""TEMP TEST FIXTURE — ENG-1615 / earthly/lunar-lib#293.

Planted deliberately so CodeQL produces a finding at a path owned by exactly one
component (services/merchant-web). The monorepo SAST fan-out must route it to
merchant-web ONLY — not to payments-api, settlement-job or platform/helm.

The sink below is a genuine CodeQL `py/command-line-injection` hit: an argv value
interpolated straight into a shell command. DELETE THIS FILE once verified.
"""

import os
import sys


def build_report(tag):
    # Untrusted argv flows into a shell command.
    os.system("git log --oneline " + tag)


if __name__ == "__main__":
    build_report(sys.argv[1])

"""TEMP TEST FIXTURE — ENG-1615 / earthly/lunar-lib#293.

Planted deliberately so CodeQL produces a finding at a path owned by exactly one
component (services/merchant-web). The monorepo SAST fan-out must route it to
merchant-web ONLY — not to payments-api, settlement-job or platform/helm.

The sink is a genuine CodeQL `py/command-line-injection` hit with a REMOTE
source (a Flask request parameter), so it fires under the default "remote"
threat model. DELETE THIS FILE once the fan-out is verified.
"""

import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/release-report")
def release_report():
    # Remote request parameter flows straight into a shell command.
    tag = request.args["tag"]
    os.system("git log --oneline " + tag)
    return "ok"

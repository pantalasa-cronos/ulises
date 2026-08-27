"""TEMP TEST FIXTURE — ENG-1615 / earthly/lunar-lib#293.

Lives at a repo path NO subcomponent claims. Its finding must stay on the ROOT
component and reach none of the four services — the other half of the
attribution proof. DELETE THIS FILE once verified.
"""

import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/audit")
def audit():
    path = request.args["path"]
    os.system("ls -la " + path)
    return "ok"

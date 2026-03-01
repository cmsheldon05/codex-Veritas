#!/bin/bash
set -euo pipefail
cd "$HOME/codex.Veritas"
exec python3 run_server.py

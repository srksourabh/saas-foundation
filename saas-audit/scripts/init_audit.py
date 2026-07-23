#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path
DOMAINS=["01-discovery","02-authentication","03-rbac-tenancy","04-functional","05-ui-ux","06-accessibility","07-security","08-api-database","09-infrastructure-cicd","10-performance-reliability","11-privacy","12-retest","13-other"]
def slugify(v:str)->str:
    s=re.sub(r"[^a-z0-9]+","-",v.lower()).strip("-")
    if not s: raise ValueError("Application name must contain letters or numbers")
    return s
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--app",required=True); p.add_argument("--output",default="saas-audit-output"); p.add_argument("--environment",default="unknown"); a=p.parse_args()
    root=Path(a.output).resolve()
    for x in [root/"reports",root/"data",root/"logs"]: x.mkdir(parents=True,exist_ok=True)
    for d in DOMAINS: (root/"evidence"/d).mkdir(parents=True,exist_ok=True)
    now=datetime.now(timezone.utc).isoformat()
    (root/"manifest.json").write_text(json.dumps({"application":a.app,"slug":slugify(a.app),"environment":a.environment,"created_at":now,"credentials_stored":False,"artifacts":[]},indent=2),encoding="utf-8")
    for f in ["coverage.json","evidence-index.json","findings.json","test-data.json"]: (root/"data"/f).write_text("[]\n",encoding="utf-8")
    (root/"logs"/"execution-log.md").write_text(f"# SaaS Audit Execution Log\n\n- Created: {now}\n- Application: {a.app}\n- Environment: {a.environment}\n\n",encoding="utf-8")
    (root/"logs"/"limitations.md").write_text("# Audit Limitations\n\n",encoding="utf-8")
    print(root); return 0
if __name__=="__main__": raise SystemExit(main())

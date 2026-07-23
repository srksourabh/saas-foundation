#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
MAP={"Critical":"P0","High":"P1","Medium":"P2","Low":"P3","Informational":"P4"}
REQ={"id","title","status","domain","severity","priority","environment","description","expected","actual","reproduction","risk","evidence","remediation","retest"}
def check(x,i):
 e=[]; p=f"finding[{i}]"
 if not isinstance(x,dict): return [f"{p}: must be object"]
 m=REQ-x.keys()
 if m:e.append(f"{p}: missing {', '.join(sorted(m))}")
 if not re.fullmatch(r"[A-Z]+-[0-9]{3,}",str(x.get('id',''))):e.append(f"{p}.id invalid")
 s=x.get('severity')
 if s not in MAP:e.append(f"{p}.severity invalid")
 elif x.get('priority')!=MAP[s]:e.append(f"{p}.priority expected {MAP[s]}")
 if not isinstance(x.get('reproduction'),list) or not x.get('reproduction'):e.append(f"{p}.reproduction required")
 r=x.get('risk',{})
 for k in ['likelihood','technical_impact','business_impact','user_impact','exploitability','detectability']:
  if not isinstance(r.get(k),int) or not 1<=r[k]<=5:e.append(f"{p}.risk.{k} must be 1..5")
 if all(isinstance(r.get(k),int) for k in ['likelihood','technical_impact','business_impact','user_impact']):
  z=r['likelihood']*max(r['technical_impact'],r['business_impact'],r['user_impact'])
  if r.get('score')!=z:e.append(f"{p}.risk.score expected {z}")
 if x.get('retest',{}).get('status') not in {'NOT_RETESTED','PASS','FAIL','BLOCKED'}:e.append(f"{p}.retest.status invalid")
 return e
def main():
 p=argparse.ArgumentParser();p.add_argument('path');a=p.parse_args()
 try:d=json.loads(Path(a.path).read_text(encoding='utf-8'))
 except Exception as ex:print(f"ERROR: {ex}");return 2
 if not isinstance(d,list):print('ERROR: root must be array');return 2
 es=[q for i,x in enumerate(d) for q in check(x,i)]
 if es:
  print('\n'.join('ERROR: '+q for q in es));return 1
 print(f"OK: {len(d)} findings validated");return 0
if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations
import argparse,html,json,shutil,subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
SEVS=['Critical','High','Medium','Low','Informational']
def esc(v):return html.escape(str(v if v is not None else ''))
def browser():
 for n in ['chromium','chromium-browser','google-chrome','google-chrome-stable','msedge','microsoft-edge']:
  p=shutil.which(n)
  if p:return p
 return None
def main():
 p=argparse.ArgumentParser();p.add_argument('--findings',required=True);p.add_argument('--output',required=True);p.add_argument('--app',required=True);p.add_argument('--environment',default='unknown');p.add_argument('--verdict',default='UNDETERMINED');p.add_argument('--score',default='N/A');p.add_argument('--pdf');a=p.parse_args()
 fs=json.loads(Path(a.findings).read_text(encoding='utf-8'));c=Counter(x.get('severity','Unknown') for x in fs)
 rows=''.join(f"<tr><td>{esc(x.get('id'))}</td><td>{esc(x.get('severity'))}</td><td>{esc(x.get('title'))}</td><td>{esc(x.get('status'))}</td><td>{esc(x.get('remediation',{}).get('permanent_solution'))}</td></tr>" for x in fs)
 counts=' '.join(f"{s}: {c[s]}" for s in SEVS)
 doc=f'''<!doctype html><meta charset="utf-8"><title>{esc(a.app)} audit</title><style>@page{{size:A4;margin:18mm}}body{{font-family:Arial;color:#152536;line-height:1.45;max-width:1100px;margin:auto;padding:24px}}h1,h2{{color:#0b3558}}table{{width:100%;border-collapse:collapse}}th,td{{border:1px solid #ccd6df;padding:8px;vertical-align:top}}.cover{{padding:70px 0;border-bottom:4px solid #0b3558}}</style><div class="cover"><h1>{esc(a.app)} — Holistic SaaS Audit</h1><p>Environment: {esc(a.environment)}</p><p>Date: {esc(datetime.now().isoformat(timespec='seconds'))}</p><h2>Verdict: {esc(a.verdict)}</h2></div><h2>Executive summary</h2><p>Score: {esc(a.score)} | Total: {len(fs)} | {esc(counts)}</p><h2>Findings</h2><table><tr><th>ID</th><th>Severity</th><th>Title</th><th>Status</th><th>Solution</th></tr>{rows}</table><h2>Required completion</h2><p>Add scope, limitations, methodology, architecture, coverage, RBAC and tenant matrices, screenshots, charts, roadmap, retest and residual risk before final delivery.</p>'''
 out=Path(a.output).resolve();out.parent.mkdir(parents=True,exist_ok=True);out.write_text(doc,encoding='utf-8');print(f'HTML: {out}')
 if a.pdf:
  b=browser();pdf=Path(a.pdf).resolve();pdf.parent.mkdir(parents=True,exist_ok=True)
  if b:
   r=subprocess.run([b,'--headless','--disable-gpu',f'--print-to-pdf={pdf}',out.as_uri()],capture_output=True,text=True)
   print(f'PDF: {pdf}' if r.returncode==0 and pdf.exists() else 'PDF generation failed; HTML is available.')
  else:print('No headless browser found; print the HTML to PDF.')
 return 0
if __name__=='__main__':raise SystemExit(main())

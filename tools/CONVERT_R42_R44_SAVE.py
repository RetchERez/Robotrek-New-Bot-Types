"""Explicit R42-R44 Dark Signal battery-save conversion; never edits the input.

Usage: python CONVERT_R42_R44_SAVE.py old.srm new_R45.srm
Only for known R42-R44 saves. Native/unknown-format saves need no conversion.
"""
from pathlib import Path
import argparse,hashlib,json
NAMES={'UNKNOWN':0,'INFILTRATOR':1,'HUNTER':2,'JUGGERNAUT':3}
SHA=lambda b:hashlib.sha256(b).hexdigest()
def checksum(data):
 add=xor=0x3652
 for i in range(0,len(data),2):
  n=int.from_bytes(data[i:i+2],'little');add=(add+n)&65535;xor^=n
 return add.to_bytes(2,'little')+xor.to_bytes(2,'little')
def convert(source,*,overrides=None,keep_third_programs=False):
 if len(source)!=8192:raise ValueError('Expected an 8192-byte native battery save, not a savestate or ROM.')
 out=bytearray(source);rows=[];overrides=overrides or {}
 for mirror in (0,0x1000):
  for slot in range(3):
   start=mirror+0x100+slot*0x500
   data=source[start:start+0x4fa]
   if checksum(data)!=source[start+0x4fa:start+0x4fe]:continue
   old=data[0x2e0:0x2e6];new=data[0x2fa:0x300]
   if any(new):
    ids=[int.from_bytes(new[i:i+2],'little') for i in (0,2,4)]
    if any(v>3 for v in ids):raise ValueError(f'Log{slot+1} has unrecognized new-format metadata; no output written.')
    rows.append(dict(log=slot+1,mirror=hex(mirror),already_new_format=True,classes=ids));continue
   ids=overrides.get(slot+1,[int.from_bytes(old[i:i+2],'little') for i in (0,2,4)])
   if len(ids)!=3 or any(v not in range(4) for v in ids):
    raise ValueError(f'Log{slot+1} old class data was overwritten by RUN programs. Supply --slot-classes {slot+1}:CLASS1,CLASS2,CLASS3 using the original classes; UNKNOWN is0.')
   typed=[v for v in ids if v]
   if len(set(typed))!=len(typed):raise ValueError(f'Log{slot+1} has duplicate classes; specify its original physical robot classes with --slot-classes.')
   before_programs=bytes(out[start+0x2aa:start+0x2f2])
   # Old class words occupied robot3 skills3/4; transient coefficients occupied5/6.
   # Their original contents cannot be reconstructed from an affected save.
   original_names=bytes(out[start+0x24a:start+0x28a])
   if not keep_third_programs:
    out[start+0x2e0:start+0x2ec]=bytes(12)
    out[start+0x24a:start+0x28a]=bytes(64)
   out[start+0x2fa:start+0x300]=b''.join(v.to_bytes(2,'little') for v in ids)
   out[start+0x4fa:start+0x4fe]=checksum(out[start:start+0x4fa])
   rows.append(dict(log=slot+1,mirror=hex(mirror),classes=ids,manual_classes=slot+1 in overrides,
    robot3_programs_3_to_6_cleared=not keep_third_programs,original_all_robot_program_bytes=before_programs.hex(),original_affected_skill_name_bytes=original_names.hex(),
    changed_offsets=[hex(i) for i in range(start,start+0x4fe) if out[i]!=source[i]]))
 if not rows:raise ValueError('No checksum-valid native logs found. Input is unchanged; no conversion is possible.')
 return bytes(out),dict(source_sha256=SHA(source),output_sha256=SHA(out),logs=rows,
  warning='Old versions overlapped thirdrobot skills3-6. Their prior contents may already be lost. Default conversion clears those four skills and their names; reprogram them in-game. Other programs/names/stats/items/story are retained. Original bytes are recorded here.',
  keep_third_programs=keep_third_programs)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('input',type=Path);p.add_argument('output',type=Path)
 p.add_argument('--slot-classes',action='append',default=[],help='For damaged old class data: LOG:INFILTRATOR,HUNTER,JUGGERNAUT in physical robot order. Use UNKNOWN for untyped/unowned.')
 p.add_argument('--keep-third-programs',action='store_true',help='Preserve old skills3-6 exactly instead of clearing possibly-corrupt programs. Inspect/reprogram them yourself.')
 a=p.parse_args();overrides={}
 if a.input.resolve()==a.output.resolve() or a.output.exists() or a.output.with_suffix(a.output.suffix+'.conversion.json').exists():p.error('Choose a new output filename. The original and existing files are never overwritten.')
 for value in a.slot_classes:
  log,names=value.split(':',1);log=int(log)
  if log not in (1,2,3):p.error('Log number must be1,2 or3.')
  try:overrides[log]=[NAMES[n.strip().upper()] for n in names.split(',')]
  except KeyError:p.error('Class names: UNKNOWN, INFILTRATOR, HUNTER, JUGGERNAUT.')
 try:converted,report=convert(a.input.read_bytes(),overrides=overrides,keep_third_programs=a.keep_third_programs)
 except ValueError as e:p.error(str(e))
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(converted)
 report.update(input=str(a.input.resolve()),output=str(a.output.resolve()))
 a.output.with_suffix(a.output.suffix+'.conversion.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))

from json import loads as procout
from subprocess import check_output as shell
from num2words import num2words as n2w
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml as xml
import yaml,toml,json,pprint,os
def nl(s):
    return s+"\n"
if not os.path.isdir("/app/output"):
    os.mkdir("/app/output")
quiet=False
div="-"*75
f=open("/app/input.txt","r+")
tl=f.read().split("\n")
f.close()
bl=[]
ul=[]
count=0
for t in tl:
    count=count+1
    print(f"loading token {count}...")
    if " --user" not in t:
        cmd=f"python3 /app/bot.py {t}"
        bl.append(procout(shell(cmd,shell=True,text=True).replace("\n","")))
    if " --user" in t:
        t=t.replace(" --user","")
        cmd=f"python3 /app/user.py {t}"
        ul.append(procout(shell(cmd,shell=True,text=True).replace("\n","")))
print("processing data...")
d={}
count=0
if len(bl)>0:
    bd={}
    for i in bl:
        count=count+1
        bd.update({n2w(count):i})
    d.update({"bots":bd})
count=0
if len(ul)>0:
    ud={}
    for i in ul:
        count=count+1
        ud.update({n2w(count):i})
    d.update({"users":ud})
with open("/app/output/output.toml","w+") as f:
    tr=toml.dumps(d)
    toml.dump(d,f)
with open("/app/output/output.yml","w+") as f:
    yr=yaml.dump(d)
    yaml.dump(d,f)
with open("/app/output/output.json","w+") as f:
    jr=json.dumps(d,indent=2)
    json.dump(d,f,indent=2)
with open("/app/output/output.py","w+") as f:
    pr=pprint.pformat(d,indent=2,sort_dicts=False)
    pr="dat="+pr
    f.write(pr)
with open("/app/output/output.xml","w+") as f:
    xr=parseString(xml(d)).toprettyxml()
    f.write(xr)
if not quiet:
    jr=nl(jr)
    pr=nl(pr)
    rl=[tr,yr,jr,pr,xr]
    for r in rl:
        print(div+"\n\n"+r)
    print(div)
if quiet:
    print("Done!!!")
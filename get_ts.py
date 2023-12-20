import json

lst = """
dub-ts
par1-ts
pdx-ts
lon2-ts
mel1-ts
bos1-ts
sjc2-ts
tor1-ts
cmn1-ts
ams1-ts
txl1-ts
hyd1-ts
nyc3-ts
sea1-ts
muc2-ts
ind1-ts
ind4-ts
bos2-ts
erf-ts
muc2-sic-ts
lon2-sic-ts
sfo3-ts
nte-ts
tlv2-ts
fra3-tsv-a
fra3-tsv-b
vac2-ts
phx3-tsv-a
phx3-tsv-b
blr1-ts
eze1-ts
atl1-ts
dfw2-ts
tlv3-ts
bom1-tsv-a
bom1-tsv-b
mel2-ts
sfo5-ts
clt1-ts
eze2-ts
tlv4-ts
pao3-ts
sna1-ts
den3-ts
DEL1-TS
hnd1-tsv-a
hnd1-tsv-b
sin1-ts
BOS3-TS
syd1-tsv-a
syd1-tsv-b
tok5-ts
sea3-tsv-a
sea3-tsv-b
hyd2-ts
blr2-ts
ash-tsv-a
ash-tsv-b
gsoc-ts
dub3a-ts
sea6-ts
iad7-ts
CHI8-TS
iad6-ts
lab-ts2
syd4-ts
aus1-ts
gru1-ts
sfo8-ts
sea7-ts
mad1-ts
"""
lst = lst.split("\n")

data = {}
servers = []

try:

    for s in lst:
        if len(s):
            servers.append({"name": s, "lines": []})
    data["ts"] = servers
    json_object = json.dumps(data, indent=4)
    with open("dc_list.json", "w") as outfile:
        outfile.write(json_object)

except Exception as e:
    print(str(s))

import json

lst = """
    "ash-tsv-b-oob" = "172.16.0.18"
    "ash-tsv-a-oob" = "172.16.0.76"
    "bom1-tsv-a-oob" = "172.16.0.63"
    "bom1-tsv-b-oob" = "172.16.0.64"
    "fra3-tsv-a-oob" = "172.16.0.57"
    "fra3-tsv-b-oob" = "172.16.0.58"
    "hnd1-tsv-a-oob" = "172.16.0.89"
    "hnd1-tsv-b-oob" = "172.16.0.90"
    "phx3-tsv-a-oob" = "172.16.0.39"
    "phx3-tsv-b-oob" = "172.16.0.40"
    "sea3-tsv-b-oob" = "172.16.0.100"
    "sea3-tsv-a-oob" = "172.16.0.101"
    "syd1-tsv-a-oob" = "172.16.0.102"
    "syd1-tsv-b-oob" = "172.16.0.103"
    "sfo8-ts-oob" = "172.16.0.4"
    "sfo3-ts-oob" = "172.16.0.11"
    "sea1-ts-oob" = "172.16.0.13"
    "dub2-ts-oob" = "172.16.0.15"
    "atl1-ts-oob" = "172.16.0.19"
    "bos1-ts-oob" = "172.16.0.20"
    "chi-ts-oob" = "172.16.0.21"
    "den1-ts-oob" = "172.16.0.23"
    "nyc3-ts-oob" = "172.16.0.25"
    "sfo5-ts-oob" = "172.16.0.26"
    "pdx-ts-oob" = "172.16.0.27"
    "mor1-ts-oob" = "172.16.0.30"
    "sin1-ts-oob" = "172.16.0.31"
    "sfo3-ts-oob" = "172.16.0.33"
    "eze2-ts-oob" = "172.16.0.34"
    "vac2-ts-oob" = "172.16.0.35"
    "nte-ts-oob" = "172.16.0.36"
    "tlv2-ts-oob" = "172.16.0.37"
    "syd-ts-oob" = "172.16.0.38"
    "lon2-ts-oob" = "172.16.0.42"
    "ams1-ts-oob" = "172.16.0.43"
    "sfo8-ts-oob" = "172.16.0.46"
    "blr1-ts-oob" = "172.16.0.48"
    "sjc2-ts-oob" = "172.16.0.50"
    "dub-ts-oob" = "172.16.0.51"
    "dfw2-ts-oob" = "172.16.0.52"
    "blr1-ts-oob" = "172.16.0.53"
    "eze1-ts-oob" = "172.16.0.54"
    "muc2-ts-oob" = "172.16.0.55"
    "erf-ts-oob" = "172.16.0.56"
    "cmn1-ts-oob" = "172.16.0.60"
    "tlv3-ts-oob" = "172.16.0.61"
    "txl1-ts-oob" = "172.16.0.66"
    "par1-ts-oob" = "172.16.0.67"
    "muc2-sic-ts-oob" = "172.16.0.68"
    "lon2-sic-ts-oob" = "172.16.0.69"
    "mel2-ts-oob" = "172.16.0.70"
    "hyd1-ts-oob" = "172.16.0.74"
    "mel1-ts-oob" = "172.16.0.75"
    "clt1-ts-oob" = "172.16.0.77"
    "pao3-ts-oob" = "172.16.0.79"
    "sna1-ts-oob" = "172.16.0.80"
    "den3-ts-oob" = "172.16.0.81"
    "blr2-ts-oob" = "172.16.0.84"
    "tlv4-ts-oob" = "172.16.0.87"
    "bos2-ts-oob" = "172.16.0.94"
    "ind4-ts-oob" = "172.16.0.96"
    "sfo6-ts-oob" = "172.16.0.97"
    "tor1-ts-oob" = "172.16.0.98"
    "gsoc-ts-oob" = "172.16.0.109"
    "iad6-ts-oob" = "172.16.0.111"
    "cle1-ts-oob" = "172.16.0.112"
    "sea6-ts-oob" = "172.16.0.113"
    "syd4-ts-oob" = "172.16.0.119"
    "chi8-ts-oob" = "172.16.0.120"
    "iad7-ts-oob" = "172.16.0.121"
"""
lst = lst.split()

data = {}
servers = []

try:

    for s in lst:
        s = s[1:-1]
        if '.' not in s and len(s):
            s = s.replace("-oob", '')
            servers.append({"name": s, "lines": []})
    data["ts"] = servers
    json_object = json.dumps(data, indent=4)
    with open("dc_list.json", "w") as outfile:
        outfile.write(json_object)

except Exception as e:
    print(str(s))

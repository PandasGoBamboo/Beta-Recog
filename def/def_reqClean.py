# ------------------------------------------------------------------------
# This script calls the zdf-api and saves the response into a json file
#
# If you want to use it, you need to modify the parameters for the desired
# Output
# ------------------------------------------------------------------------

# -------------------------------------------------------------------------

# Request on ZDF-API

# -------------------------------------------------------------------------

import requests
import json

# Adjustbale parameters

# Searchquerry
q = '*'

# Maxcount results
hitcount = 5

# Path for request, needs to be adjusted
pathsep = '/'

zdf = 'zdf'

category = 'gesellschaft'

# broadcast = 'terra-x'

# show = 'soehne-der-sonne-die-maya'

path = pathsep + zdf + pathsep + category + pathsep #+ broadcast # + pathsep + show

# Videotype, see also videotypes.xlsx
videotype = 'episode_episode'

# sort By 'date' or 'title'
sort = 'date'

# sort order 'desc' = descending, 'asc' = ascending
order = 'desc'

# show advanced results
advan1 = 'portal-delivery'

# show advanced explanations. e.g shows editorial tags
advan2 = 'explain:true'

# concatenate querry string
payload = {'q': q, 'limit': hitcount, 'paths': path, 'videotypes': videotype, 'sortBy': sort, 'sortOrder': order,
           'profile': advan1, 'tuning': advan2}

# modify header-values
headers = {'API-Auth': 'Bearer 20c238b5345eb428d01ae5c748c5076f033dfcc7'}

# make request
r = requests.get("https://api.zdf.de/search/documents", headers=headers, params=payload)

# print url in console
print(r.url)

# ---------------------------------------------------------------------------------------------------
# save to file
with open("../zdf_data/test/testdata.json", "w") as outfile:
    outfile.write(r.text)

# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# Start of clean.py
# opens file to be cleaned
# with open('../zdf_data/test_zdf_dokumentation.json', "r") as infile:
#    data = json.load(infile)
# ---------------------------------------------------------------------------------------------------

# load response into json
data = r.json()

# load data from hits-object into variable
hits = (data['http://zdf.de/rels/debug']['response']['hits']['hits'])

# opens file for output, variable "broadcast" commented out, adapt if needed
with open("../zdf_data/test/test_" + zdf + "_" + category + "_" # + broadcast +
          ".json", "w", encoding='utf-8') as outfile:
    # iterate over [hits]-Array
    
    for dic in hits:
        
        # delete unnecessary keys from dictionary
        dic.pop("_index")
        dic.pop("_type")
        dic.pop("_score")
        dic.pop("_explanation")

        # delete unnecessary keys from ['_source'] object
        src = dic['_source']
        src.pop("attrs")
        src.pop("broadcaster")
        src.pop("contentType")
        src.pop("videoType")
        # src.pop("duration")
        src.pop("hasVideo")
        src.pop("lastModifiedTimestamp")
        src.pop("lastModifiedBy")

        # src.pop("scheduledVideoType")
        src.pop("streamVisible")
        src.pop("target")
        src.pop("promotions")
        src.pop("type")
        src.pop("editorialTagsFulltext")

        # src.pop("titleTypeahead")
        # src.pop("editorialTagsTypeahead")
        # src.pop("documentFingerprint")
        # src.pop("documentFingerprintSize")
        
        src.pop("blockedTimes")
        src.pop("brandKeyword")
        src.pop("teilbereich")
        src.pop("newsOverline")
        src.pop("profiles")
        src.pop("exactTitleBoost")
        src.pop("exactBrandBoost")
        src.pop("exactCategoryBoost")
        
        # save wanted keys into outfile
    
    json.dump(dic, outfile, ensure_ascii=False, indent=2)
print("done")
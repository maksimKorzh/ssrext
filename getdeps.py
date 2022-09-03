###########################################
#
# Tool to get corresponding .tcz packages
#      from a given .so files list
#
###########################################

# packages
import requests

# matched tczs
matched_tcz = []

# download list of tcz packages
tczs = requests.get('http://repo.tinycorelinux.net/13.x/x86_64/tcz').text.split('\n')[:-1]

# get shared libs for ssr
with open('./ext/deps.txt') as f: depso = f.read().split('\n')[:-1]

# loop over tcz packages
for tcz in tczs:
  # loop over shared libs
  for dep in depso:
    candidate = dep.strip().split('.')[0]
    if candidate in tcz.split('.')[0] and '-dev' not in tcz:
      matched_tcz.append(tcz)

# filter duplicates
matched_tcz = list(set(matched_tcz))

# write results to file
with open('candidates.tcz.dep', 'w') as f:
  f.write('\n'.join(matched_tcz))
  f.write('\n\nMatched: ' + str(len(matched_tcz)) + '  Total shared libs: ' + str(len(depso)) + '\n')

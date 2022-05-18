#!/usr/bin/env python
from display.models import VulList
import json
import datetime
  
with open("../full_data.json", 'r') as f:
    data = json.load(f)
  
for each in data:
    if 'S' not in each:
        each['S'] = 'U' 
    if 'cvss_score' not in each:
        each['cvss_score'] = 0 
        each['cvss_version'] = 0 
        
task_vul_objs = []
for each in data:
    new_vul = VulList(cve_id=each['name'], cnnvd_id=each['other_id'], description=each['description'],
                     vul_unit=each['vul_unit'], affected_unit=each['affected_unit'], attack_vector=each['AV'],
                     attack_complexity=each['AC'], priviledge_required=each['PR'], 
                     user_interaction=each['UI'], confidential=each['C'], integration=each['I'], 
                     available=each['A'], privacy=each['P'], ecnomic=each['E'], functional=each['F'], 
                     human_safety=each['HI'], scope=each['S'], cvss_score=each['cvss_score'], 
                     cvss_version=each['cvss_version'], link=each['link'], date= datetime.datetime.now()
                     )   
    task_vul_objs.append(new_vul)
print(len(task_vul_objs))
# objs = VulList.objects.bulk_create(task_vul_objs)
# print(objs) 
# if objs is None:
#     print("data import failed.")
# else:
#     print("data import success.")

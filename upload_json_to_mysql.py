import json
import datetime
import string
from sqlalchemy import create_engine
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append("../vvdp/")
from vvdb.dto import  UserList, UserOpLog, VulList

engine = create_engine('mysql+pymysql://root:123456789asd...@39.103.238.35:3306/vvdb?charset=utf8')
Session = sessionmaker(bind=engine)
db = Session()
print(db)
with open("full_data.json", 'r') as f:
    data = json.load(f)

for each in data:
    if 'S' not in each:
        each['S'] = 'U'
    if 'cvss_score' not in each:
        each['cvss_score'] = 0
        each['cvss_version'] = 0
for each in data:
    new_vul = VulList(cve_id=each['name'].strip(), cnnvd_id=each['other_id'].strip(), description=each['description'].strip(),
                     vul_unit=each['vul_unit'].strip(), affected_unit=each['affected_unit'].strip(), attack_vector=each['AV'].strip(),
                     attack_complexity=each['AC'].strip(), priviledge_required=each['PR'].strip(), 
                     user_interaction=each['UI'].strip(), confidential=each['C'].strip(), integration=each['I'].strip(), 
                     available=each['A'].strip(), privacy=each['P'].strip(), ecnomic=each['E'].strip(), functional=each['F'].strip(), 
                     human_safety=each['HI'].strip(), scope=each['S'].strip(), cvss_score=each['cvss_score'], 
                     cvss_version=each['cvss_version'], link=each['link'].strip(), date= datetime.datetime.now()
                     )
    db.add(new_vul)
db.commit()
db.close()
print("db session closed.")

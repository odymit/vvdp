import json
import datetime
from sqlalchemy import create_engine
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append("../vvdp/")
from vvdb.dto import  UserList, UserOpLog, VulList

engine = create_engine("mysql+pymysql://root:12345689asd...@39.103.238.35:3306/vvdb?charset=utf-8")
Session = sessionmaker(bind=engine)
db = Session()
print(db)
with open("../vvdp/full_data.json", 'r') as f:
    data = json.load(f)

for each in data:
    if 'S' not in each:
        each['S'] = 'U'
    if 'cvss_score' not in each:
        each['cvss_score'] = 0
        each['cvss_version'] = 0
for each in data:
    new_vul = VulList(cve_id=each['name'], cnnvd_id=each['other_id'], description=each['description'],
                     vul_unit=each['vul_unit'], affected_unit=each['affected_unit'], attack_vector=each['AV'],
                     attack_complexity=each['AC'], priviledge_required=each['PR'], 
                     user_interaction=each['UI'], confidential=each['C'], integration=each['I'], 
                     available=each['A'], privacy=each['P'], ecnomic=each['E'], functional=each['F'], 
                     human_safety=each['HI'], scope=each['S'], cvss_score=each['cvss_score'], 
                     cvss_version=each['cvss_version'], link=each['link'], date=datetime.datetime.now()
                     )
    db.add(new_vul)
db.commit()
#data = db.query(VulList).first()
#print(db, data)
db.close()
print("db session closed.")

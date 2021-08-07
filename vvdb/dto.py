from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Float, VARCHAR,UnicodeText,Text,DateTime
import datetime
Base = declarative_base()

'''
CREATE TABLE 'vul_list' (
  `id` int(11) NOT NULL AUTO_INCREMENT, 
  `cve_id` varchar(255) NOT NULL
)
'''
class VulList(Base):
    __tablename__ = 'vul_list'
    id = Column(Integer, primary_key=True, nullable=False)
    cve_id = Column(VARCHAR(255), unique=True, nullable=False)
    cnnvd_id = Column(VARCHAR(255), nullable=True)
    description = Column(UnicodeText, nullable=False)
    vul_unit = Column(UnicodeText, nullable=False)
    affected_unit = Column(UnicodeText, nullable=False)
    attack_vector = Column(VARCHAR(1), nullable=False)
    attack_complexity = Column(VARCHAR(1), nullable=False)
    priviledge_required = Column(VARCHAR(1), nullable=False)
    user_interaction = Column(VARCHAR(1), nullable=False)
    c  = Column(VARCHAR(1), nullable=False)
    i  = Column(VARCHAR(1), nullable=False)
    a  = Column(VARCHAR(1), nullable=False)
    privacy  = Column(VARCHAR(1), nullable=False)
    ecnomic  = Column(VARCHAR(1), nullable=False)
    functional  = Column(VARCHAR(1), nullable=False)
    human_safety = Column(VARCHAR(1), nullable=False)
    scope = Column(VARCHAR(1), nullable=False)
    cvss_score = Column(Float, nullable=True)
    cvss_version = Column(Float, nullable=True)
    vehicle_sec_score = Column(Float, nullable=True)
    link = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)












'''
CREATE TABLE `user_list`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
'''    
class UserList(Base):
    __tablename__ = 'user_list'
    id = Column(Integer, primary_key=True,nullable=False)
    user_name = Column(VARCHAR(255), nullable=False)
    nick_name = Column(VARCHAR(255), nullable=True)
    pwd = Column(VARCHAR(255), nullable=False)

'''
CREATE TABLE `user_operation_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `operationtime` datetime NULL DEFAULT NULL,
  `operation` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

'''
class UserOpLog(Base):
    __tablename__ = 'user_operation_log'
    id = Column(Integer, primary_key=True,nullable=False)
    user_name = Column(VARCHAR(64), nullable=False)
    operationtime = Column(DateTime(),default=datetime.datetime.now)
    operation = Column(VARCHAR(512), nullable=False)



if __name__ == "__main__":
  print()

import os
from flask import Flask
from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
import sys
from common.mhash import md5
from flask_cors import *

sys.path.append("..")
sys.path.append("./common/")
from common.tockenManage import tockenManage
from vvdb.dto import Dirs, ScheRes, UserList, UserOpLog


# create and configure the app
app = Flask(__name__)
# mysql config
engine = create_engine("mysql+pymysql://root:12345689asd...@39.103.238.35:3306/vvdb?charset=utf-8")
Session = sessionmaker(bind=engine)
db = Session()
mtm = tockenManage()
CORS(app, supports_credentials=True)

# defalt page
@app.route("/")
def index():
    return "Hello, this is a display page."

# login
@app.route('/user/login',methods=["POST"])
def userLogin():
    username = request.json['username']
    pwd =  request.json['password']
    if(len(username) == 0 or len(pwd) ==0 ):
        return {"code":0,"message":'账号密码错误','data':{'token':''}}
    # 数据库检测
    user = db.query(UserList).filter(UserList.user_name == username).first()
    if(pwd is None):
        return {"code":0,"message":'账号密码错误','data':{'token':''}}
    if(md5(user.user_name) != md5(username)  or  md5(user.pwd)!=md5(pwd)  ):
        return {"code":0,"message":'账号密码错误','data':{'token':''}}
    oplog = UserOpLog(user_name = username,operation = 'login')
    db.add(oplog)
    db.commit()
    tocken = mtm.setTocken(username) 
    return {"code":20000,"message":"登录成功","name":username,"data":{"token":tocken}}

#获取头像
@app.route('/user/info',methods=["get"])
def userInfo():
    vue_token = request.headers.get('X-Token')
    print(vue_token)
    username = mtm.getTockenName(vue_token)
    user = db.query(UserList).filter(UserList.user_name == username).first()
    return {'code':20000,'msg':"获取成功",'data':{'name':user.nick_name,'avatar':'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'}}

#登出
@app.route('/user/logout',methods=["POST"])
def userLogout():
    vue_token = request.headers.get('X-Token')
    print(vue_token)
    username = mtm.getTockenName(vue_token)
    oplog = UserOpLog(user_name = username,operation = 'logout')
    db.add(oplog)
    db.commit()
    mtm.removeTocken(vue_token)
    return {'code':20000,'data':'success'}


if __name__ == '__main__':
    app.run(port = '10086',host="0.0.0.0",debug=True) 
    db.close()

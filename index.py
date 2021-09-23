from flask import Flask,url_for,request,render_template,redirect,jsonify,escape,session
from flask_jwt_extended import JWTManager,create_access_token,create_refresh_token,set_access_cookies,set_refresh_cookies,jwt_refresh_token_required,jwt_required,get_jwt_identity,unset_jwt_cookies
from flask_socketio import SocketIO,send
from jwt import InvalidTokenError
from werkzeug.utils import secure_filename
from twilio.rest import Client
from email.message import EmailMessage
from datetime import date
import os,pymongo,torch,random,re,string,geoip2.database,sqlite3,smtplib,hashlib,datetime,hmac
app=Flask(__name__)
app.config["JWT_TOKEN_LOCATION"]=["cookies"]
app.config["JWT_COOKIE_SECURE"]=False
app.config["JWT_ACCESS_COOKIE_PATH"]="/"
app.config["JWT_REFRESH_COOKIE_PATH"]="/"
app.config["JWT_COOKIE_CSRF_PROTECT"]=True
app.config["JWT_SECRET_KEY"]="ASOIFhja8OTGz9askaapASWAR32D42342s345sadfasf)(/§$)(/dASDeAFcrAsDaeastJUgfaasofvpßA)UG9A(/WTAZSFz7A*VFS)JA=*)T78A=Sfq9867a(/)=S(%)AGf"
app.config["SECRET_KEY"]="GaOUIfghAUDGIUSDGuisDGuihDGuisUIdgIUPADgiupSADGiupDGPiuSADGp9uhSWDGp98uhSDGP9uhDGP9uhADEGuhWREG978hWEG)(/Q§WET98zhaS987HGUHADG9DGFzsADG)"
jwt=JWTManager(app)
socketio=SocketIO(app)
app.secret_key="AFaGklDGKLHHSALKDghkjJHKSADGhjkASHJKDGKJhSgd987asdGHÜOqatg()zadsg(UHswdGsiudgshidgKHIJ)"
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/shop")
def shop():
    return render_template("shop.html")
@app.route("/faq")
def faq():
    return render_template("faq.html")
@app.route("/chat")
def chat():
    con=sqlite3.connect("/home/luca/online_shop/SQL")
    cursor=con.cursor()
    con.execute("SELECT MESSAGE FROM USER_MESSAGE_HISTORY")
    messages=cursor.fetchall()
    con.commit()
    con.close()
    print (messages)
    return render_template("chat.html",messages=messages)
@app.route("/rating")
def rating():
    return render_template("rating.html")
@app.route("/impsum")
def impsum():
    return render_template("impressum.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/settings")
def settings():
    return render_template("einstellungen.html")
@app.route("/adminpannel")
def adminpannel():
    return render_template("adminpannel.html")
@socketio.on("message")
def handleMessage(msg):
    print("Message: " + msg)
    con=sqlite3.connect("/home/luca/online_shop/SQL")
    cursor=con.cursor()
    con.execute("INSERT INTO USER_MESSAGE_HISTORY (MESSAGE,SENDER) VALUES (?,?)",(msg,"einNutzer"))
    con.commit()
    con.close()
    send(msg, broadcast=True)
if __name__=="__main__":
    app.run(port=1338,debug=True)
    socketio.run(app)

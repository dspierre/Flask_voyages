import email
import sqlite3
from urllib import request
from flask import Flask, render_template, url_for
from sklearn.tree import DecisionTreeClassifier
import pickle as p
from flask import Flask, request, jsonify, render_template
from app import  app
import numpy as np
import pandas as pd
from werkzeug.utils import redirect
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle

"""def DB_NAME_LOGIN("args"):
    conn = sqlite3.connect("args")
    cur=conn.cursor()
    return cur,conn
 """
def conn(db):
    try:
        con = sqlite3.connect("travel (2).db")
        cur = con.cursor()
        print("Connexion réussie à SQLite")
        return cur, con
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite. ", error)

def close(cur, con):
    cur.close()
    con.close()
    print("Connexion SQLite est fermée")

def create_account(username,mail, password):
    con = sqlite3.connect("travel (2).db")
    con.execute('INSERT INTO users(username, mail,password) VALUES (?,?,?)', ( username,mail, password))
    con.commit()
    con.close()

def password_exist(password):
    cur_check, con_check = conn("travel (2).db")
    #cur_check.execute(select_request(users, "*", f"password = '{password}'"))
    cur_check.execute("select * from Users")
    resultat = list(cur_check)
    find = "indisponible " if len(resultat) == 1 else "False"
    close(cur_check, con_check)
    return find

def select_request(param, param1, param2):
    pass

def  check_mail():
    try:
        con = sqlite3.connect("travel (2).db")
        cur = con.cursor()
        print("Connexion réussie à SQLite")
        return cur, con
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite. ", error)
    cur_check =con("travel (2).db")
    conn=cur_check.execute(select_request("users","*",f"email = '{email}'"))
    con_check = conn("users")
    resultat = list(cur_check)
    find = "TRUE" if len(resultat) == 1 else "False"
    close(cur_check, con_check)
    return find

def password_exist(password):
    cur_check, con_check = conn("travel (2).db")
    #cur_check.execute(select_request(users, "*", f"password = '{password}'"))
    resultat = list(cur_check)
    find = "indisponible " if len(resultat) == 1 else "False"
    close(cur_check, con_check)
    return find

def check_user(mail):
    cur_check, con_check = conn("travel (2).db")
    #cur_check.execute(select_request(users, "*", f"mail ='{mail}'"))
    find = "False " if len(cur_check.fetchall()) == 0 else "True"
    close(cur_check, con_check)
    return find

@app.route('/sign up', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name=request.form.get('mail')
        email = request.form.get('mail')
        Username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        Firstname = request.form.get('Firstname')
        check_password = password_exist(password)

    if check_mail == 'TRUE':
        phrase = "un compte avec ce mail existe déja"
        return render_template("index.html", phrase=phrase)

    elif check_user == 'indisponible':
        phrase2 = "ce username existe déja veuillez en mettre un autre "
        return render_template("index.html", phrase2=phrase2)

    elif password == check_password:
        create_account(email, password, name)
        print(email, name, password)
        return redirect(url_for("home.html"))
    else:
        erreur = "le mot de passe doit être le même que celui tapé en vérification"
        return render_template("index.html", erreur=erreur)

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template("home.html")

@app.route('/loggin', methods=['POST', 'GET'])
def loggin():
    name = request.form.get('name')
    email = request.form.get('Email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmpassword')
    if password == confirmPassword:
        print("ok")
        print("bievenue", name)
        return render_template("home.html")
    else:
        erreur = "probleme de mots de passe"
        return render_template("loggin.html", erreur=erreur)
# Importing the dataset

@app.route('/modele', methods=['POST'])

def predict():
    data = request.get_json()
    modelfile = '\modele\model_SVM.pkl'
    model=p.load (open(modelfile, 'rb'))
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

@app.route('/indication', methods=['POST', 'GET'])
def indication():
    return render_template("indication.html")

if __name__ == '__main__':
    modelfile = 'modele\model_SVM.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=False)

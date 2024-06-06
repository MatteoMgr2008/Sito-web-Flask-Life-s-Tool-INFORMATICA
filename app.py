from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import random
import math
import pandas as pd
import os
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/listatooldisponibili")
def lista_tool_disponibili():
    return render_template("listatooldisponibili.html")

@app.route("/calcolodellamediadeinumeri", methods=["GET", "POST"])
def calcolo_della_media_dei_numeri():
    messaggio = None
    if request.method == "POST":
        lista_numeri_scelti = request.form["numeri_lista"].split()
        lista_numeri_scelti = [int(numero) for numero in lista_numeri_scelti]
        if len(lista_numeri_scelti) > 0:
            media_numeri_lista = sum(lista_numeri_scelti) / len(lista_numeri_scelti)
            messaggio = f"La media dei numeri {lista_numeri_scelti} è: {media_numeri_lista}"
    return render_template("calcolodellamediadeinumeri.html", message = messaggio)

@app.route("/calcolodelquadratodeinumeri")
def calcolo_del_quadrato_dei_numeri():
    return render_template("calcolodelquadratodeinumeri.html")

@app.route("/verificadellaparitaodisparitadiunnumero")
def verifica_della_parita_o_disparita_di_un_numero():
    return render_template("verificadellaparitaodisparitadiunnumero.html")

@app.route("/calcolodelfattoriale")
def calcolo_del_fattoriale():
    return render_template("calcolodelfattoriale.html")

@app.route("/giocodellanciodeldado", methods=["GET", "POST"])
def gioco_del_lancio_del_dado():
    messaggio = None
    if request.method == "POST":
        numero_lanci_dadi = int(request.form["numero_lanci_dadi"])
        numero_faccie_dadi = int(request.form["numero_faccie_dadi"])
        risultati_lanci = []
        for _ in range(numero_lanci_dadi):
            numero_randomico_dado = random.randint(1, numero_faccie_dadi)
            risultati_lanci.append(numero_randomico_dado)
            messaggio = risultati_lanci
    return render_template("giocodellanciodeldado.html", message = messaggio)

@app.route("/giocodellindovinello")
def gioco_dell_indovinello():
    return render_template("giocodellindovinello.html")

@app.route("/giocodelmorracinese")
def gioco_del_morra_cinese():
    return render_template("giocodelmorracinese.html")

if __name__ == "__main__":
    app.run(debug=True)
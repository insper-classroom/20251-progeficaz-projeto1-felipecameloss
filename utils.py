import json
import sqlite3 as sql
from flask import Flask,render_template,request,redirect,url_for,flash

def load_data():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from notes")
    notes=cur.fetchall()
    return notes

def create_data(titulo, detalhes):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("insert into notes(Título,Detalhes) values (?,?)",(titulo,detalhes))
    con.commit()
    con.close()

def load_template(arquivo_template):
    with open(f'static/templates/{arquivo_template}') as file:
        text = file.read()
    return text

def delete_note_from_db(id):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from notes where ID=?",(id,))
    con.commit()
    con.close()
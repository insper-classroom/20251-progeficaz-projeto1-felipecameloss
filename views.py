from utils import *
from flask import render_template, request, redirect
import sqlite3 as sql

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id = dados[0], titulo=dados[1], detalhes=dados[2])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def edit_page(id):

    # titulo = request.form.get('titulo')
    # detalhes = request.form.get('detalhes')
    # con=sql.connect("db_web.db")
    # con.row_factory=sql.Row
    # cur=con.cursor()
    # cur.execute("select Título=?, Detalhes=? where ID=?",(titulo, detalhes,id))
    # notes=cur.fetchall()

    # return load_template('components/edit_note.html').format(id=id, titulo=titulo, detalhes=detalhes)

    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Título, Detalhes FROM notes WHERE ID=?", (id,))
    note = cur.fetchone()
    con.close()

    titulo = note['Título']
    detalhes = note['Detalhes']

    return load_template('components/edit_note.html').format(id=id, titulo=titulo, detalhes=detalhes)

def submit(titulo, detalhes):
    create_data(titulo, detalhes)

def delete_notes(id):
    delete_note_from_db(id)
    
def save_note(id):
    save_note_to_db(id)
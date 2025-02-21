from utils import load_data, load_template, create_data, delete_note_from_db
from flask import render_template, request, redirect
import sqlite3 as sql

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id = dados[0], title=dados[1], details=dados[2])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    create_data(titulo, detalhes)

def delete_notes(id):
    delete_note_from_db(id)

def edit_notes(id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        detalhes = request.form.get('detalhes')
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("update notes set Título=?, Detalhes=? where ID=?", (titulo, detalhes, id))
        con.commit()
        con.close()
        return redirect('/')
    

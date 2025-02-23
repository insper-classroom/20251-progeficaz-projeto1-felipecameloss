from flask import Flask, render_template_string, request, redirect, render_template
import sqlite3 as sql
import views

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route("/delete_notes/<int:id>",methods=['GET'])
def delete_notes(id):
    views.delete_notes(id)
    return redirect('/')

@app.route("/edit_notes/<int:id>",methods=['POST','GET'])
def edit_page(id):
    
    return render_template_string(views.edit_page(id))

@app.route("/save_note/<int:id>",methods=['POST','GET'])
def save_note(id):
    
    views.save_note(id)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return views.error_404()
if __name__ == '__main__':
    app.run(debug=True)
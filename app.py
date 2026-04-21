from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_veterinaria_2026'

DATABASE = 'citas.db'


def get_db():
    """Obtiene una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Inicializa la base de datos creando la tabla pacientes si no existe."""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mascota TEXT NOT NULL,
            propietario TEXT NOT NULL,
            especie TEXT,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# ──────────────────────────────────────────────
# Ruta principal – Agenda (listar todas las citas)
# ──────────────────────────────────────────────
@app.route('/')
def agenda():
    """Muestra todas las citas programadas."""
    conn = get_db()
    citas = conn.execute('SELECT * FROM pacientes ORDER BY fecha ASC').fetchall()
    conn.close()
    return render_template('agenda.html', citas=citas)


# ──────────────────────────────────────────────
# Agendar – Registrar una nueva cita
# ──────────────────────────────────────────────
@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    """Formulario para registrar una nueva cita médica."""
    if request.method == 'POST':
        mascota = request.form.get('mascota', '').strip()
        propietario = request.form.get('propietario', '').strip()
        especie = request.form.get('especie', '').strip()
        fecha = request.form.get('fecha', '').strip()

        # Validación básica
        if not mascota or not propietario or not fecha:
            flash('Todos los campos obligatorios deben ser completados.', 'danger')
            return redirect(url_for('agendar'))

        conn = get_db()
        conn.execute(
            'INSERT INTO pacientes (mascota, propietario, especie, fecha) VALUES (?, ?, ?, ?)',
            (mascota, propietario, especie, fecha)
        )
        conn.commit()
        conn.close()

        flash('Cita agendada exitosamente.', 'success')
        return redirect(url_for('agenda'))

    return render_template('agendar.html')


# ──────────────────────────────────────────────
# Modificar – Editar una cita existente
# ──────────────────────────────────────────────
@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    """Edita la fecha o los datos de una cita existente."""
    conn = get_db()

    if request.method == 'POST':
        mascota = request.form.get('mascota', '').strip()
        propietario = request.form.get('propietario', '').strip()
        especie = request.form.get('especie', '').strip()
        fecha = request.form.get('fecha', '').strip()

        if not mascota or not propietario or not fecha:
            flash('Todos los campos obligatorios deben ser completados.', 'danger')
            return redirect(url_for('modificar', id=id))

        conn.execute(
            'UPDATE pacientes SET mascota=?, propietario=?, especie=?, fecha=? WHERE id=?',
            (mascota, propietario, especie, fecha, id)
        )
        conn.commit()
        conn.close()

        flash('Cita modificada exitosamente.', 'success')
        return redirect(url_for('agenda'))

    cita = conn.execute('SELECT * FROM pacientes WHERE id=?', (id,)).fetchone()
    conn.close()

    if cita is None:
        flash('La cita no fue encontrada.', 'warning')
        return redirect(url_for('agenda'))

    return render_template('modificar.html', cita=cita)


# ──────────────────────────────────────────────
# Cancelar – Eliminar una cita
# ──────────────────────────────────────────────
@app.route('/cancelar/<int:id>')
def cancelar(id):
    """Elimina una cita del sistema."""
    conn = get_db()
    conn.execute('DELETE FROM pacientes WHERE id=?', (id,))
    conn.commit()
    conn.close()

    flash('Cita cancelada exitosamente.', 'info')
    return redirect(url_for('agenda'))


# ──────────────────────────────────────────────
# Punto de entrada
# ──────────────────────────────────────────────
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

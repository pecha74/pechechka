
import os                
from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2               
from psycopg2.extras import RealDictCursor  
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps  
import json                   
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = 'supersecretkey'  

def get_db():
    database_url = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(database_url)

    with conn.cursor() as cur:
        cur.execute("SET search_path TO auth")
    return conn

def init_db():
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute("CREATE SCHEMA IF NOT EXISTS auth")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS operations (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                date DATE NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                type TEXT NOT NULL CHECK (type IN ('income', 'expense'))
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_operations_user_id ON operations(user_id)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_operations_date ON operations(date)")
        conn.commit()
    conn.close()

init_db()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))  
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            if cur.fetchone():
                conn.close()
                return "Пользователь уже существует. <a href='/register'>Попробовать снова</a>"
            password_hash = generate_password_hash(password)
            cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id",
                        (username, password_hash))
            user_id = cur.fetchone()['id']
            conn.commit()
        conn.close()
        session['user_id'] = user_id
        session['username'] = username
        return redirect(url_for('index'))  
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, password_hash FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
        conn.close()
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Неверные имя пользователя или пароль. <a href='/login'>Попробовать снова</a>"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()   
    return redirect(url_for('login'))

@app.route('/')
@login_required   
def index():
    user_id = session['user_id']
    date_from_raw = request.args.get('date_from', '')
    date_to_raw = request.args.get('date_to', '')
    category = request.args.get('category', '')

    def parse_date(date_str):
        if not date_str:
            return None
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str.strip(), '%d/%m/%Y')
            return dt.strftime('%Y-%m-%d')
        except:
            return None

    date_from_sql = parse_date(date_from_raw)
    date_to_sql = parse_date(date_to_raw)

    query = """
        SELECT id, date, category, amount, type
        FROM operations
        WHERE user_id = %s
    """
    params = [user_id]

    if date_from_sql:
        query += " AND date >= %s"
        params.append(date_from_sql)
    if date_to_sql:
        query += " AND date <= %s"
        params.append(date_to_sql)
    if category:
        query += " AND category = %s"
        params.append(category)

    query += " ORDER BY date DESC"

    conn = get_db()
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, params)
        operations = cur.fetchall()
        cur.execute("""
            SELECT DISTINCT category
            FROM operations
            WHERE user_id = %s
            ORDER BY category
        """, (user_id,))
        categories = [row['category'] for row in cur.fetchall()]
    conn.close()

    return render_template('index.html',
                           operations=operations,
                           categories=categories,
                           date_from=date_from_raw,
                           date_to=date_to_raw,
                           selected_category=category)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    user_id = session['user_id']
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        type_op = request.form['type']   
        conn = get_db()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO operations (user_id, date, category, amount, type)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, date, category, amount, type_op))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:record_id>')
@login_required
def delete(record_id):
    user_id = session['user_id']
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM operations WHERE id = %s AND user_id = %s", (record_id, user_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
@login_required
def edit(record_id):
    user_id = session['user_id']
    conn = get_db()
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        type_op = request.form['type']
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE operations
                SET date = %s, category = %s, amount = %s, type = %s
                WHERE id = %s AND user_id = %s
            """, (date, category, amount, type_op, record_id, user_id))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM operations WHERE id = %s AND user_id = %s", (record_id, user_id))
        record = cur.fetchone()
    conn.close()
    if not record:
        return "Запись не найдена", 404
    return render_template('edit.html', record=record)

@app.route('/stats')
@login_required
def stats():
    user_id = session['user_id']
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as total_income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as total_expense
            FROM operations
            WHERE user_id = %s
        """, (user_id,))
        row = cur.fetchone()
    conn.close()
    total_income = row[0] if row[0] is not None else 0
    total_expense = row[1] if row[1] is not None else 0
    balance = total_income - total_expense
    return render_template('stats.html', income=total_income, expense=total_expense, balance=balance)

@app.route('/chart')
@login_required
def chart():
    user_id = session['user_id']
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT category, SUM(amount) as total
            FROM operations
            WHERE user_id = %s AND type = 'expense'
            GROUP BY category
        """, (user_id,))
        rows = cur.fetchall()
    conn.close()
    categories = [row[0] for row in rows]
    amounts = [row[1] for row in rows]
    return render_template('chart.html',
                           categories=json.dumps(categories),
                           amounts=json.dumps(amounts))

@app.route('/advanced_stats')
@login_required
def advanced_stats():
    user_id = session['user_id']
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                TO_CHAR(DATE_TRUNC('month', date), 'YYYY-MM') as month,
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as expense
            FROM operations
            WHERE user_id = %s
                AND date >= (CURRENT_DATE - INTERVAL '12 months')
            GROUP BY DATE_TRUNC('month', date)
            ORDER BY month ASC
        """, (user_id,))
        monthly_data = cur.fetchall()
    months = [row[0] for row in monthly_data]
    incomes = [float(row[1]) for row in monthly_data]
    expenses = [float(row[2]) for row in monthly_data]

    with conn.cursor() as cur:
        cur.execute("""
            SELECT category, SUM(amount) as total
            FROM operations
            WHERE user_id = %s AND type = 'expense'
            GROUP BY category
            ORDER BY total DESC
            LIMIT 5
        """, (user_id,))
        top_categories = cur.fetchall()
    cat_names = [row[0] for row in top_categories]
    cat_amounts = [float(row[1]) for row in top_categories]

    with conn.cursor() as cur:
        cur.execute("""
            SELECT COALESCE(AVG(amount), 0)
            FROM operations
            WHERE user_id = %s 
                AND type = 'expense'
                AND date >= (CURRENT_DATE - INTERVAL '30 days')
        """, (user_id,))
        avg_daily_expense = cur.fetchone()[0]

    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM operations WHERE user_id = %s", (user_id,))
        total_operations = cur.fetchone()[0]

    conn.close()

    return render_template('advanced_stats.html',
                           months=json.dumps(months),
                           incomes=json.dumps(incomes),
                           expenses=json.dumps(expenses),
                           cat_names=json.dumps(cat_names),
                           cat_amounts=json.dumps(cat_amounts),
                           avg_daily_expense=round(avg_daily_expense, 2),
                           total_operations=total_operations)

if __name__ == '__main__':
    app.run(debug=True)
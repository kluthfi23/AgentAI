from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    jsonify
)

from database.database import Database

app = Flask(__name__)
app.secret_key = "agentai_secret"

from database.database import Database

app = Flask(__name__)
app.secret_key = "agentai_secret"


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = Database()

        user = db.login(
            username,
            password
        )

        db.close()

        if user:

            session.clear()

            session["login"] = True
            session["username"] = username

            return redirect("/")

    return render_template("login.html")


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =========================
# DASHBOARD
# =========================

@app.route("/")
def home():

    if not session.get("login"):
        return redirect("/login")

    keyword = request.args.get("q", "").strip()

    db = Database()

    if keyword:
        jobs = db.find_job(keyword)
    else:
        jobs = db.get_jobs()

    total = len(jobs)

    pending = len([
        j for j in jobs
        if j[3] == "Pending"
    ])

    running = len([
        j for j in jobs
        if j[3] == "Running"
    ])

    selesai = len([
        j for j in jobs
        if j[3] == "Selesai"
    ])

    gagal = len([
        j for j in jobs
        if j[3] == "Gagal"
    ])

    db.close()

    return render_template(
        "index.html",
        jobs=jobs,
        total=total,
        pending=pending,
        running=running,
        selesai=selesai,
        gagal=gagal,
        username=session.get("username"),
        keyword=keyword
    )


# =========================
# TAMBAH JOB
# =========================

@app.route("/add", methods=["POST"])
def add_job():

    if not session.get("login"):
        return redirect("/login")

    website = request.form.get("website")
    username = request.form.get("username")

    if website and username:

        db = Database()

        db.add_job(
            website,
            username
        )

        db.close()

    return redirect("/")


# =========================
# HAPUS JOB
# =========================

@app.route("/delete/<int:job_id>")
def delete_job(job_id):

    if not session.get("login"):
        return redirect("/login")

    db = Database()

    db.delete_job(job_id)

    db.close()

    return redirect("/")

# ==========================
# API - GET ALL JOBS
# ==========================

@app.route("/api/jobs")
def api_jobs():

    db = Database()

    jobs = db.get_jobs()

    db.close()

    result = []

    for job in jobs:

        result.append({
            "id": job[0],
            "website": job[1],
            "username": job[2],
            "status": job[3]
        })

    return jsonify(result)

# ==========================
# API - STATS
# ==========================

@app.route("/api/stats")
def api_stats():

    db = Database()

    jobs = db.get_jobs()

    db.close()

    total = len(jobs)

    pending = len([
        j for j in jobs
        if j[3] == "Pending"
    ])

    running = len([
        j for j in jobs
        if j[3] == "Running"
    ])

    selesai = len([
        j for j in jobs
        if j[3] == "Selesai"
    ])

    gagal = len([
        j for j in jobs
        if j[3] == "Gagal"
    ])

    return jsonify({
        "total": total,
        "pending": pending,
        "running": running,
        "selesai": selesai,
        "gagal": gagal
    })

# ==========================
# API - ADD JOB
# ==========================

@app.route("/api/job", methods=["POST"])
def api_add_job():

    website = request.form.get("website")
    username = request.form.get("username")

    if not website:
        return jsonify({
            "success": False,
            "message": "website wajib diisi"
        }), 400

    db = Database()

    db.add_job(
        website,
        username or "api"
    )

    db.close()

    return jsonify({
        "success": True,
        "website": website,
        "username": username
    })

# ==========================
# API - DELETE JOB
# ==========================

@app.route("/api/job/<int:job_id>", methods=["DELETE"])
def api_delete_job(job_id):

    db = Database()

    db.delete_job(job_id)

    db.close()

    return jsonify({
        "success": True,
        "job_id": job_id
    })

# ==========================
# API - GET JOB DETAIL
# ==========================

@app.route("/api/job/<int:job_id>")
def api_job_detail(job_id):

    db = Database()

    jobs = db.get_jobs()

    db.close()

    for job in jobs:

        if job[0] == job_id:

            return jsonify({
                "id": job[0],
                "website": job[1],
                "username": job[2],
                "status": job[3]
            })

    return jsonify({
        "success": False,
        "message": "job tidak ditemukan"
    }), 404

# ==========================
# API - HEALTH
# ==========================

@app.route("/api/health")
def api_health():

    return jsonify({
        "status": "online",
        "app": "AgentAI",
        "version": "0.1.0"
    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

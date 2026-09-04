# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, send_from_directory
from books_data import search_books, BOOKS, SEARCH_SUGGESTIONS
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")


# ─── Servir o frontend ────────────────────────────────────────────────────────

@app.route("/")
def index():
    return send_from_directory("static", "index.html")


# ─── API: busca de livros ─────────────────────────────────────────────────────

@app.route("/api/search")
def api_search():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({
            "success": False,
            "error": "Por favor, informe um termo de busca.",
            "results": [],
            "total": 0,
            "query": ""
        }), 400

    results = search_books(query)

    return jsonify({
        "success": True,
        "query": query,
        "total": len(results),
        "results": results
    })


# ─── API: sugestões de busca ──────────────────────────────────────────────────

@app.route("/api/suggestions")
def api_suggestions():
    return jsonify({
        "success": True,
        "suggestions": SEARCH_SUGGESTIONS
    })


# ─── API: todos os livros (para exploração) ────────────────────────────────────

@app.route("/api/books")
def api_books():
    level = request.args.get("level")

    books = BOOKS
    if level:
        try:
            level_int = int(level)
            books = [b for b in BOOKS if b["level"] == level_int]
        except ValueError:
            pass

    books_sorted = sorted(books, key=lambda b: b["level"])

    return jsonify({
        "success": True,
        "total": len(books_sorted),
        "results": books_sorted
    })


# ─── API: estatísticas ────────────────────────────────────────────────────────

@app.route("/api/stats")
def api_stats():
    total = len(BOOKS)
    by_level = {}
    all_tags = set()

    level_labels = {
        1: "Iniciante",
        2: "Básico",
        3: "Intermediário",
        4: "Avançado",
        5: "Expert"
    }

    for book in BOOKS:
        lvl = book["level"]
        label = level_labels.get(lvl, str(lvl))
        by_level[label] = by_level.get(label, 0) + 1
        all_tags.update(book["tags"])

    return jsonify({
        "success": True,
        "total_books": total,
        "by_level": by_level,
        "total_tags": len(all_tags)
    })


# ─── Inicialização ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)

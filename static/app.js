/* ── TechBooks — app.js ─────────────────────────────────────────────────────── */

// ── Elementos do DOM ──────────────────────────────────────────────────────────
const searchForm      = document.getElementById("searchForm");
const searchInput     = document.getElementById("searchInput");
const suggestionsList = document.getElementById("suggestionsList");
const tagsRow         = document.getElementById("tagsRow");
const welcomeState    = document.getElementById("welcomeState");
const loadingState    = document.getElementById("loadingState");
const errorState      = document.getElementById("errorState");
const errorMessage    = document.getElementById("errorMessage");
const emptyState      = document.getElementById("emptyState");
const resultsSection  = document.getElementById("resultsSection");
const resultsTitle    = document.getElementById("resultsTitle");
const resultsCount    = document.getElementById("resultsCount");
const booksGrid       = document.getElementById("booksGrid");
const clearBtn        = document.getElementById("clearBtn");
const statTotal       = document.getElementById("statTotal");
const statTags        = document.getElementById("statTags");
const bookCardTemplate = document.getElementById("bookCardTemplate");

// ── Estado ────────────────────────────────────────────────────────────────────
let allSuggestions = [];
let currentSuggestionIndex = -1;
let debounceTimer = null;

// ── Mapa de labels de nível ───────────────────────────────────────────────────
const LEVEL_LABELS = {
  1: "Iniciante",
  2: "Básico",
  3: "Intermediário",
  4: "Avançado",
  5: "Expert"
};

// Tags rápidas para exibir no hero (subconjunto das sugestões)
const QUICK_TAGS = [
  "Python", "JavaScript", "Docker", "SQL", "Machine Learning",
  "Git", "React", "Java", "Linux", "AWS"
];


// ── Inicialização ─────────────────────────────────────────────────────────────
(async function init() {
  await Promise.all([loadStats(), loadSuggestions()]);
  renderQuickTags();
  checkUrlQuery();
})();


// ── Carregar estatísticas ─────────────────────────────────────────────────────
async function loadStats() {
  try {
    const res = await fetch("/api/stats");
    if (!res.ok) return;
    const data = await res.json();
    statTotal.textContent = data.total_books;
    statTags.textContent  = data.total_tags;
  } catch (_) {
    // Silencia — não é crítico
  }
}

// ── Carregar sugestões de autocomplete ────────────────────────────────────────
async function loadSuggestions() {
  try {
    const res = await fetch("/api/suggestions");
    if (!res.ok) return;
    const data = await res.json();
    allSuggestions = data.suggestions || [];
  } catch (_) {
    allSuggestions = [];
  }
}

// ── Quick tags ────────────────────────────────────────────────────────────────
function renderQuickTags() {
  tagsRow.innerHTML = "";
  QUICK_TAGS.forEach(tag => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "quick-tag";
    btn.textContent = tag;
    btn.setAttribute("aria-label", `Buscar por ${tag}`);
    btn.addEventListener("click", () => {
      searchInput.value = tag;
      performSearch(tag);
    });
    tagsRow.appendChild(btn);
  });
}


// ── Verificar query na URL (deep link) ────────────────────────────────────────
function checkUrlQuery() {
  const params = new URLSearchParams(window.location.search);
  const q = params.get("q");
  if (q) {
    searchInput.value = q;
    performSearch(q);
  }
}


// ── Formulário de busca ───────────────────────────────────────────────────────
searchForm.addEventListener("submit", e => {
  e.preventDefault();
  const q = searchInput.value.trim();
  if (q) performSearch(q);
});

clearBtn.addEventListener("click", () => {
  searchInput.value = "";
  searchInput.focus();
  showState("welcome");
  hideSuggestions();
  // Limpa a URL
  const url = new URL(window.location);
  url.searchParams.delete("q");
  window.history.pushState({}, "", url);
});


// ── Busca principal ───────────────────────────────────────────────────────────
async function performSearch(query) {
  if (!query.trim()) return;

  hideSuggestions();
  showState("loading");

  // Atualiza URL para deep linking
  const url = new URL(window.location);
  url.searchParams.set("q", query);
  window.history.pushState({}, "", url);

  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 15000);

    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: controller.signal
    });
    clearTimeout(timeout);

    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "Erro ao buscar livros.");
      return;
    }

    if (!data.results || data.results.length === 0) {
      showState("empty");
      return;
    }

    renderResults(data);

  } catch (err) {
    if (err.name === "AbortError") {
      showError("A busca demorou muito. Tente novamente em alguns segundos.");
    } else {
      showError("Não foi possível conectar ao servidor. Tente novamente.");
    }
  }
}


// ── Renderizar resultados ─────────────────────────────────────────────────────
function renderResults(data) {
  booksGrid.innerHTML = "";

  resultsTitle.textContent = `Resultados para "${data.query}"`;
  resultsCount.textContent = `${data.total} livro${data.total !== 1 ? "s" : ""} encontrado${data.total !== 1 ? "s" : ""}, ordenados por nível`;

  data.results.forEach((book, index) => {
    const cardEl = createBookCard(book, index + 1);
    cardEl.style.animationDelay = `${index * 50}ms`;
    booksGrid.appendChild(cardEl);
  });

  showState("results");
  resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
}


// ── Criar card de livro ───────────────────────────────────────────────────────
function createBookCard(book, position) {
  const fragment = bookCardTemplate.content.cloneNode(true);
  const card     = fragment.querySelector(".book-card");

  // Classe de nível para cor da barra
  card.classList.add(`level-${book.level}`);
  card.setAttribute("aria-label", `Livro ${position}: ${book.title}`);

  // Badge de nível
  const badge = card.querySelector(".card-badge");
  badge.textContent = LEVEL_LABELS[book.level] || book.level_label;
  badge.className = `badge badge-${book.level}`;

  // Número de posição + ano
  const header = card.querySelector(".card-header");
  const numSpan = document.createElement("span");
  numSpan.className = "card-number";
  numSpan.textContent = position;
  numSpan.setAttribute("aria-label", `Posição ${position}`);
  header.insertBefore(numSpan, header.firstChild);

  card.querySelector(".card-year").textContent = book.year || "";
  card.querySelector(".card-title").textContent = book.title;
  card.querySelector(".card-author").textContent = book.author;
  card.querySelector(".card-description").textContent = book.description;

  // Meta
  const pagesEl = card.querySelector(".card-pages");
  const langEl  = card.querySelector(".card-lang");
  pagesEl.textContent = book.pages ? `${book.pages} págs.` : "";
  langEl.textContent  = book.language || "Português";

  // Tags (máx 4)
  const tagsContainer = card.querySelector(".card-tags");
  const displayTags = (book.tags || []).slice(0, 4);
  displayTags.forEach(tag => {
    const span = document.createElement("span");
    span.className = "card-tag";
    span.textContent = tag;
    tagsContainer.appendChild(span);
  });

  // Link
  const link = card.querySelector(".card-link");
  link.href = book.buy_link || `https://www.amazon.com.br/s?k=${encodeURIComponent(book.title)}`;
  link.setAttribute("aria-label", `Ver "${book.title}" na Amazon`);

  // Retorna o elemento <article> diretamente, não o fragment
  return card;
}


// ── Controle de estados de UI ─────────────────────────────────────────────────
const STATES = ["welcomeState", "loadingState", "errorState", "emptyState", "resultsSection"];

function showState(state) {
  // Esconde todos primeiro
  welcomeState.style.display   = "none";
  loadingState.style.display   = "none";
  errorState.style.display     = "none";
  emptyState.style.display     = "none";
  resultsSection.style.display = "none";

  welcomeState.hidden   = true;
  loadingState.hidden   = true;
  errorState.hidden     = true;
  emptyState.hidden     = true;
  resultsSection.hidden = true;

  // Mostra só o estado ativo
  if (state === "welcome") {
    welcomeState.style.display = "block";
    welcomeState.hidden = false;
  } else if (state === "loading") {
    loadingState.style.display = "flex";
    loadingState.hidden = false;
  } else if (state === "error") {
    errorState.style.display = "flex";
    errorState.hidden = false;
  } else if (state === "empty") {
    emptyState.style.display = "flex";
    emptyState.hidden = false;
  } else if (state === "results") {
    resultsSection.style.display = "block";
    resultsSection.hidden = false;
    resultsSection.setAttribute("tabindex", "-1");
    resultsSection.focus();
  }
}

function showError(msg) {
  errorMessage.textContent = msg;
  showState("error");
}


// ── Autocomplete ──────────────────────────────────────────────────────────────
searchInput.addEventListener("input", () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => updateSuggestions(), 180);
});

searchInput.addEventListener("keydown", e => {
  const items = suggestionsList.querySelectorAll(".suggestion-item");
  if (!items.length) return;

  if (e.key === "ArrowDown") {
    e.preventDefault();
    currentSuggestionIndex = Math.min(currentSuggestionIndex + 1, items.length - 1);
    updateActiveSuggestion(items);
  } else if (e.key === "ArrowUp") {
    e.preventDefault();
    currentSuggestionIndex = Math.max(currentSuggestionIndex - 1, -1);
    updateActiveSuggestion(items);
  } else if (e.key === "Enter") {
    if (currentSuggestionIndex >= 0 && items[currentSuggestionIndex]) {
      e.preventDefault();
      selectSuggestion(items[currentSuggestionIndex].textContent);
    }
  } else if (e.key === "Escape") {
    hideSuggestions();
  }
});

// Fechar sugestões ao clicar fora
document.addEventListener("click", e => {
  if (!searchForm.contains(e.target)) hideSuggestions();
});

function updateSuggestions() {
  const query = searchInput.value.trim().toLowerCase();
  currentSuggestionIndex = -1;

  if (!query || query.length < 1) {
    hideSuggestions();
    return;
  }

  const matches = allSuggestions
    .filter(s => s.toLowerCase().includes(query))
    .slice(0, 7);

  if (!matches.length) {
    hideSuggestions();
    return;
  }

  suggestionsList.innerHTML = "";
  matches.forEach(match => {
    const li = document.createElement("li");
    li.className = "suggestion-item";
    li.setAttribute("role", "option");
    li.textContent = match;
    li.addEventListener("mousedown", e => {
      e.preventDefault(); // evita blur no input
      selectSuggestion(match);
    });
    suggestionsList.appendChild(li);
  });

  suggestionsList.hidden = false;
  searchInput.setAttribute("aria-expanded", "true");
}

function updateActiveSuggestion(items) {
  items.forEach((item, i) => {
    const isActive = i === currentSuggestionIndex;
    item.setAttribute("aria-selected", String(isActive));
    if (isActive) {
      searchInput.value = item.textContent;
      item.scrollIntoView({ block: "nearest" });
    }
  });
}

function selectSuggestion(text) {
  searchInput.value = text;
  hideSuggestions();
  performSearch(text);
}

function hideSuggestions() {
  suggestionsList.hidden = true;
  suggestionsList.innerHTML = "";
  currentSuggestionIndex = -1;
  searchInput.setAttribute("aria-expanded", "false");
}

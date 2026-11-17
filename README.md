# Sito web Flask "Life's Tool"

🇮🇹 [Italiano](#italiano) | 🇬🇧 [English](#english)

<a id="italiano"></a>
## 🇮🇹 Italiano

Sito web creato con la libreria Python, Flask, riguardante dei tool matematici e di altro genere.

Link al sito web: https://matteoomgr2008.pythonanywhere.com/

Progetto realizzato per la materia **Informatica**. Il sito si chiama *"Life's Tool: Make Your Life Simplify"* e raccoglie piccoli strumenti pensati per semplificare la vita quotidiana. Le pagine sono in italiano.

### Funzionalità

- **Home page** (`/`): presentazione del progetto, link al codice su GitHub e pulsante per andare alla lista dei tool.
- **Lista dei tool disponibili** (`/listatooldisponibili`): elenco dei tool, divisi in "Tool matematici" e "Tool dei giochi interattivi".

**Tool matematici**

| Tool | Percorso | Stato |
|------|----------|-------|
| Calcolo della media dei numeri | `/calcolodellamediadeinumeri` | Funzionante: si inseriscono numeri separati da uno spazio (anche decimali con la virgola, ad es. `5,7`) e il sito mostra la media |
| Calcolo del quadrato dei numeri | `/calcolodelquadratodeinumeri` | In lavorazione ("WORKING PROGRESS") |
| Verifica della parità o disparità di un numero | `/verificadellaparitaodisparitadiunnumero` | In lavorazione ("WORKING PROGRESS") |
| Calcolo del fattoriale | `/calcolodelfattoriale` | In lavorazione ("WORKING PROGRESS") |

**Tool dei giochi interattivi**

| Tool | Percorso | Stato |
|------|----------|-------|
| Gioco del lancio del dado | `/giocodellanciodeldado` | Funzionante: si scelgono il numero di dadi (1–1000) e il numero di facce (2–1000) e il sito mostra il risultato di ogni lancio; all'invio compare l'avviso "Alea iacta est - Il dado è tratto (Giulio Cesare)" |
| Gioco dell'indovinello | `/giocodellindovinello` | In lavorazione ("WORKING PROGRESS") |
| Gioco del morra cinese | `/giocodelmorracinese` | In lavorazione ("WORKING PROGRESS") |

### Contenuto della repository

```
app.py                         # Applicazione Flask con tutte le route
templates/                     # Pagine HTML (template Jinja2)
  index.html                   # Home page
  listatooldisponibili.html    # Lista dei tool
  calcolodellamediadeinumeri.html
  giocodellanciodeldado.html
  calcolodelquadratodeinumeri.html, verificadellaparitaodisparitadiunnumero.html,
  calcolodelfattoriale.html, giocodellindovinello.html,
  giocodelmorracinese.html     # Pagine segnaposto "WORKING PROGRESS"
static/
  styles-*.css                 # Fogli di stile delle varie pagine
  script-giocodellanciodeldado.js  # Avviso mostrato al lancio del dado
  images/                      # Immagini delle pagine e favicon (.ico)
```

### Tecnologie utilizzate

- Python 3 con **Flask** (route e template Jinja2)
- HTML, CSS e un po' di JavaScript
- Hosting su **PythonAnywhere**

### Requisiti

- Python 3
- Le librerie importate in `app.py`: `flask`, `pandas`, `matplotlib` (pandas e matplotlib sono importate ma non ancora usate, però servono perché l'app si avvii)

Nella repository non è presente un file `requirements.txt`.

### Come avviare il sito in locale

```bash
git clone https://github.com/MatteoMgr2008/Sito-web-Flask-Life-s-Tool-INFORMATICA.git
cd Sito-web-Flask-Life-s-Tool-INFORMATICA
pip install flask pandas matplotlib
python app.py
```

Poi apri il browser su http://127.0.0.1:5000/ (l'app parte in modalità debug).

### Autore

[MatteoMgr2008](https://github.com/MatteoMgr2008)

---

<a id="english"></a>
## 🇬🇧 English

A website built with the Python library Flask, offering math tools and other kinds of tools.

Website link: https://matteoomgr2008.pythonanywhere.com/

This project was made for **Computer Science** (Informatica) class. The site is called *"Life's Tool: Make Your Life Simplify"* and collects small tools meant to make everyday life easier. The pages are in Italian.

### Features

- **Home page** (`/`): introduces the project, links to the code on GitHub and has a button that leads to the list of tools.
- **List of available tools** (`/listatooldisponibili`): the tools, split into "Math tools" and "Interactive game tools".

**Math tools**

| Tool | Route | Status |
|------|-------|--------|
| Average of numbers | `/calcolodellamediadeinumeri` | Working: enter numbers separated by spaces (decimals with a comma are fine too, e.g. `5,7`) and the site shows their average |
| Square of numbers | `/calcolodelquadratodeinumeri` | Work in progress ("WORKING PROGRESS") |
| Even/odd check | `/verificadellaparitaodisparitadiunnumero` | Work in progress ("WORKING PROGRESS") |
| Factorial | `/calcolodelfattoriale` | Work in progress ("WORKING PROGRESS") |

**Interactive game tools**

| Tool | Route | Status |
|------|-------|--------|
| Dice roll game | `/giocodellanciodeldado` | Working: choose how many dice to roll (1–1000) and how many faces each die has (2–1000), and the site shows the result of every roll; on submit an alert says "Alea iacta est - Il dado è tratto (Giulio Cesare)" |
| Riddle game | `/giocodellindovinello` | Work in progress ("WORKING PROGRESS") |
| Rock-paper-scissors | `/giocodelmorracinese` | Work in progress ("WORKING PROGRESS") |

### Repository contents

```
app.py                         # Flask application with all the routes
templates/                     # HTML pages (Jinja2 templates)
  index.html                   # Home page
  listatooldisponibili.html    # List of tools
  calcolodellamediadeinumeri.html
  giocodellanciodeldado.html
  calcolodelquadratodeinumeri.html, verificadellaparitaodisparitadiunnumero.html,
  calcolodelfattoriale.html, giocodellindovinello.html,
  giocodelmorracinese.html     # "WORKING PROGRESS" placeholder pages
static/
  styles-*.css                 # Stylesheets for the pages
  script-giocodellanciodeldado.js  # Alert shown when rolling the dice
  images/                      # Page images and favicons (.ico)
```

### Technologies

- Python 3 with **Flask** (routes and Jinja2 templates)
- HTML, CSS and a bit of JavaScript
- Hosted on **PythonAnywhere**

### Requirements

- Python 3
- The libraries imported in `app.py`: `flask`, `pandas`, `matplotlib` (pandas and matplotlib are imported but not used yet; the app still needs them in order to start)

There is no `requirements.txt` file in the repository.

### Running the site locally

```bash
git clone https://github.com/MatteoMgr2008/Sito-web-Flask-Life-s-Tool-INFORMATICA.git
cd Sito-web-Flask-Life-s-Tool-INFORMATICA
pip install flask pandas matplotlib
python app.py
```

Then open http://127.0.0.1:5000/ in your browser (the app runs in debug mode).

### Author

[MatteoMgr2008](https://github.com/MatteoMgr2008)

# Guidelines: De la Studiu Filozofic la Pagina Web Editorial

## Partea I: Generarea Continutului (TXT)

### Prompt pentru Generarea Studiului

```
Creează un studiu/analiză despre filozofia lui [NUME FILOZOF] pe înțelesul tuturor.

Structura dorită:
1. **Introducere captivantă** - cine a fost, de ce contează azi
2. **Contextul istoric** - epoca, influențele, rivalitățile
3. **Conceptele cheie** - explicate simplu, cu exemple din viața reală
4. **Sistemul filozofic** - cum se leagă ideile între ele
5. **Citate memorabile** - 3-5 citate esențiale cu explicații
6. **Critici și controverse** - ce i s-a reproșat, puncte slabe
7. **Moștenirea** - influența asupra gândirii moderne
8. **Aplicații practice** - cum ne ajută ideile lui azi

Ton: Accesibil dar nu superficial. Scrie ca pentru un cititor inteligent care nu are background filozofic.

Lungime: 3000-5000 cuvinte.

Include:
- Analogii și metafore pentru concepte abstracte
- Exemple concrete din viața cotidiană
- Conexiuni cu probleme actuale
- Structură clară cu subtitluri
```

### Variante de Prompt

**Pentru filozofi antici:**
```
Creează un studiu despre [FILOZOF] care să răspundă la: De ce ar citi un om din 2024 pe [FILOZOF]? Ce probleme actuale rezolvă ideile lui?
```

**Pentru curente filozofice:**
```
Analizează [CURENT FILOZOFIC] - origini, principii, reprezentanți, critici. Explică de ce a apărut și ce problemă încerca să rezolve.
```

**Pentru comparații:**
```
Compară viziunile lui [FILOZOF A] și [FILOZOF B] despre [TEMĂ]. Cine avea dreptate? De ce contează azi?
```

---

## Partea II: Transformarea în HTML Editorial

### Principii de Design

1. **Content First** - Designul servește textul, nu invers
2. **White Space** - Spațiu generos între elemente
3. **Typography** - Ierarhie clară, fonturi elegante
4. **Restraint** - Maxim 2-3 culori, fără efecte gratuite
5. **Timeless** - Evită trenduri, preferă clasicul

### Paleta de Culori

```css
:root {
    /* Fundal */
    --primary: #ffffff;
    --secondary: #f8f8f8;

    /* Text */
    --text: #1a1a1a;
    --text-muted: #666666;
    --text-light: #999999;

    /* Accent - alege UNA din variantele de mai jos */
    --accent: #c41e3a;  /* Roșu cardinal - clasic, autoritar */
    /* --accent: #1a4f6e; */  /* Albastru închis - academic, serios */
    /* --accent: #2d5a27; */  /* Verde forest - organic, natural */
    /* --accent: #8b4513; */  /* Maro - cald, vintage */

    /* Utilitare */
    --border: #e5e5e5;
    --success: #2d8659;
    --error: #c41e3a;
}
```

### Tipografie

```css
/* Titluri - Serif elegant */
font-family: 'Playfair Display', Georgia, serif;
font-weight: 400;  /* Nu bold pentru titluri mari */

/* Corp text - Serif lizibil */
font-family: 'Merriweather', Georgia, serif;
line-height: 1.8-1.9;
font-size: 1.05rem;

/* Etichete, navigație - Sans-serif */
font-family: 'Inter', -apple-system, sans-serif;
text-transform: uppercase;
letter-spacing: 0.1-0.2em;
font-size: 0.7-0.8rem;
```

### Structura HTML

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Titlu] - Studiu Filozofic</title>

    <!-- Fonturi -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Merriweather:ital,wght@0,300;0,400;1,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
    <nav>...</nav>

    <header class="hero">
        <span class="category">FILOZOFIE</span>
        <h1>[Numele Filozofului]</h1>
        <p class="subtitle">[Subtitlu descriptiv]</p>
    </header>

    <main>
        <article>
            <section class="intro">
                <p class="lead">[Primul paragraf - cu drop cap]</p>
            </section>

            <section>
                <h2>[Subtitlu]</h2>
                <p>...</p>
            </section>

            <aside class="pull-quote">
                <blockquote>"[Citat memorabil]"</blockquote>
                <cite>— [Autor], [Sursă]</cite>
            </aside>

            <!-- Repetă secțiuni după nevoie -->
        </article>
    </main>

    <footer>...</footer>
</body>
</html>
```

### Componente Cheie

#### 1. Hero Section
```css
.hero {
    min-height: 100vh;
    background: var(--primary);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 6rem 2rem;
    border-bottom: 1px solid var(--border);
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 10vw, 7rem);
    font-weight: 400;
    color: var(--text);
}

.hero .category {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 2rem;
}
```

#### 2. Drop Cap (Prima Literă Mare)
```css
.lead::first-letter {
    font-family: 'Playfair Display', serif;
    font-size: 5rem;
    float: left;
    line-height: 0.85;
    padding-right: 1rem;
    color: var(--accent);
}
```

#### 3. Pull Quote (Citat Evidențiat)
```css
.pull-quote {
    padding: 4rem 2rem;
    background: var(--secondary);
    text-align: center;
    margin: 4rem 0;
    position: relative;
}

.pull-quote::before {
    content: '"';
    font-family: 'Playfair Display', serif;
    font-size: 15rem;
    position: absolute;
    top: -2rem;
    left: 2rem;
    color: var(--accent);
    opacity: 0.1;
}

.pull-quote blockquote {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-style: italic;
    max-width: 700px;
    margin: 0 auto;
}
```

#### 4. Secțiuni cu Număr
```css
.section-number {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-muted);
}

/* Exemplu: "01 / CONTEXTUL ISTORIC" */
```

#### 5. Navigație
```css
nav {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.98);
    border-bottom: 1px solid var(--border);
    padding: 1rem 3rem;
}

nav a {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
}
```

### Reguli de Stil

#### DO (Fă)
- Folosește mult spațiu alb
- Păstrează ierarhia tipografică
- Limitează-te la 2-3 culori
- Folosește borduri de 1px, subtile
- Aliniază textul la stânga (nu justify)
- Folosește imagini/ilustrații B&W sau monocrome

#### DON'T (Nu Fă)
- Evită gradiente colorate
- Evită umbre box-shadow puternice
- Evită border-radius (sau maxim 2-4px)
- Evită animații excesive
- Evită fonturi decorative/fanteziste
- Evită mai mult de 2 fonturi

### Elemente Interactive (Opțional)

Dacă adaugi simulatoare sau quiz-uri:

```css
/* Butoane - Simple, pătrate */
.btn {
    padding: 1rem 2rem;
    border: 1px solid var(--text);
    background: transparent;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border-radius: 0;
    cursor: pointer;
}

.btn:hover {
    background: var(--text);
    color: var(--primary);
}

/* Cards */
.card {
    border: 1px solid var(--border);
    padding: 2rem;
    background: var(--primary);
}

.card:hover {
    border-color: var(--text);
}
```

### Checklist Final

- [ ] Fonturi încărcate corect (Playfair, Merriweather, Inter)
- [ ] O singură culoare accent folosită consistent
- [ ] Hero cu titlu mare, curat
- [ ] Drop cap la primul paragraf
- [ ] Cel puțin un pull-quote
- [ ] Navigație fixă, subtilă
- [ ] Footer întunecat pentru contrast
- [ ] Responsive pe mobile
- [ ] Fără efecte gratuite (particule, animații excesive)
- [ ] Spațiere consistentă între secțiuni (6rem padding)

---

## Exemple de Referință

**Reviste pentru inspirație vizuală:**
- The New Yorker
- The Atlantic
- Monocle
- Aeon Magazine
- The Paris Review

**Principiul de bază:**
Dacă designul atrage atenția asupra lui însuși, e prea mult. Conținutul trebuie să fie eroul.

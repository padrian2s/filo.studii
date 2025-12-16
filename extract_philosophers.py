#!/usr/bin/env python3
"""
Script pentru extragerea numelor de filozofi din titlurile videoclipurilor
de pe canalul YouTube Casa Paleologu.

Folosește yt-dlp (nu necesită API key).

Instalare: pip install yt-dlp
Rulare: python extract_philosophers.py
"""

import subprocess
import json
import re
from collections import Counter

CHANNEL_URL = "https://www.youtube.com/@casapaleologu/videos"

# Lista de filozofi cunoscuți pentru matching
KNOWN_PHILOSOPHERS = [
    # Antici
    "Socrate", "Platon", "Aristotel", "Epicur", "Zenon", "Seneca",
    "Marc Aureliu", "Marcus Aurelius", "Epictet", "Heraclit", "Parmenide",
    "Democrit", "Pitagora", "Diogene", "Plotin", "Cicero",

    # Medievali
    "Augustin", "Toma d'Aquino", "Toma de Aquino", "Aquino",
    "Boethius", "Anselm", "Abelard", "Ockham",

    # Moderni
    "Descartes", "Spinoza", "Leibniz", "Locke", "Hume", "Berkeley",
    "Kant", "Hegel", "Schopenhauer", "Nietzsche", "Kierkegaard",
    "Marx", "Mill", "Bentham", "Rousseau", "Voltaire", "Montesquieu",
    "Pascal", "Hobbes", "Bacon", "Machiavelli",

    # Contemporani
    "Husserl", "Heidegger", "Sartre", "Camus", "Beauvoir",
    "Wittgenstein", "Russell", "Popper", "Kuhn", "Foucault",
    "Derrida", "Deleuze", "Levinas", "Arendt", "Habermas",
    "Rawls", "Nozick", "Rorty", "Quine", "Gadamer",

    # Români
    "Blaga", "Lucian Blaga", "Cioran", "Emil Cioran", "Eliade", "Mircea Eliade",
    "Noica", "Constantin Noica", "Nae Ionescu", "Vulcănescu", "Mircea Vulcănescu",
    "Petre Țuțea", "Țuțea", "Steinhardt", "Liiceanu", "Gabriel Liiceanu",
    "Pleșu", "Andrei Pleșu", "Patapievici", "Paleologu", "Alexandru Paleologu",

    # Alții
    "Confucius", "Lao Tzu", "Buddha", "Freud", "Jung",
    "Dostoievski", "Tolstoi", "Goethe", "Emerson", "Thoreau"
]


def get_video_titles():
    """Extrage titlurile videoclipurilor folosind yt-dlp."""
    print("Se extrag titlurile videoclipurilor...")
    print("(Acest proces poate dura câteva minute)\n")

    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--flat-playlist",
                "--print", "%(title)s",
                "--no-warnings",
                CHANNEL_URL
            ],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode != 0:
            print(f"Eroare yt-dlp: {result.stderr}")
            return []

        titles = [t.strip() for t in result.stdout.strip().split('\n') if t.strip()]
        print(f"S-au găsit {len(titles)} videoclipuri.\n")
        return titles

    except FileNotFoundError:
        print("EROARE: yt-dlp nu este instalat.")
        print("Instalează cu: pip install yt-dlp")
        return []
    except subprocess.TimeoutExpired:
        print("EROARE: Timeout - operațiunea a durat prea mult.")
        return []


def extract_philosophers_from_titles(titles):
    """Extrage numele filozofilor din titluri."""
    found_philosophers = Counter()
    titles_by_philosopher = {}

    for title in titles:
        title_upper = title.upper()

        for philosopher in KNOWN_PHILOSOPHERS:
            # Căutare case-insensitive
            if philosopher.upper() in title_upper:
                # Normalizează numele (ex: "Emil Cioran" -> "Cioran")
                normalized = normalize_name(philosopher)
                found_philosophers[normalized] += 1

                if normalized not in titles_by_philosopher:
                    titles_by_philosopher[normalized] = []
                titles_by_philosopher[normalized].append(title)

    return found_philosophers, titles_by_philosopher


def normalize_name(name):
    """Normalizează numele filozofilor (elimină prenumele pentru unii)."""
    normalizations = {
        "Lucian Blaga": "Blaga",
        "Emil Cioran": "Cioran",
        "Mircea Eliade": "Eliade",
        "Constantin Noica": "Noica",
        "Mircea Vulcănescu": "Vulcănescu",
        "Petre Țuțea": "Țuțea",
        "Gabriel Liiceanu": "Liiceanu",
        "Andrei Pleșu": "Pleșu",
        "Alexandru Paleologu": "Paleologu",
        "Marcus Aurelius": "Marc Aureliu",
        "Toma d'Aquino": "Toma de Aquino",
    }
    return normalizations.get(name, name)


def find_unknown_potential_names(titles, known_found):
    """Caută potențiale nume proprii care nu sunt în lista cunoscută."""
    # Pattern pentru nume proprii (cuvinte cu majusculă)
    potential_names = Counter()

    # Cuvinte de ignorat
    ignore_words = {
        "DESPRE", "CU", "LA", "DE", "DIN", "PE", "SI", "SAU", "DAR", "CA",
        "CARE", "CE", "CUM", "UNDE", "CAND", "PENTRU", "PRIN", "SPRE",
        "ROMANIA", "ROMANIAN", "EUROPA", "AMERICA", "FRANTA", "GERMANIA",
        "CASA", "PALEOLOGU", "INTERVIEW", "PARTEA", "PART", "VOL", "EP",
        "VIDEO", "LIVE", "NEW", "THE", "AND", "WITH", "YOUTUBE"
    }

    for title in titles:
        # Găsește cuvinte cu majusculă
        words = re.findall(r'\b[A-ZĂÂÎȘȚ][a-zăâîșț]+\b', title)
        for word in words:
            if word.upper() not in ignore_words and len(word) > 3:
                if word not in known_found:
                    potential_names[word] += 1

    # Returnează doar cele care apar de mai multe ori
    return {name: count for name, count in potential_names.items() if count >= 2}


def main():
    print("=" * 60)
    print("EXTRACTOR DE FILOZOFI - Casa Paleologu YouTube")
    print("=" * 60 + "\n")

    # Extrage titlurile
    titles = get_video_titles()

    if not titles:
        print("Nu s-au putut extrage titlurile.")
        return

    # Găsește filozofii
    philosophers, titles_by_phil = extract_philosophers_from_titles(titles)

    # Afișează rezultatele
    print("=" * 60)
    print("FILOZOFI GĂSIȚI")
    print("=" * 60 + "\n")

    if philosophers:
        # Sortează după numărul de apariții
        sorted_philosophers = sorted(philosophers.items(), key=lambda x: (-x[1], x[0]))

        print(f"{'FILOZOF':<25} {'APARIȚII':>10}")
        print("-" * 37)

        for philosopher, count in sorted_philosophers:
            print(f"{philosopher:<25} {count:>10}")

        print(f"\n{'TOTAL FILOZOFI UNICI:':<25} {len(philosophers):>10}")
        print(f"{'TOTAL VIDEOCLIPURI:':<25} {len(titles):>10}")

        # Detalii per filozof
        print("\n" + "=" * 60)
        print("DETALII - TITLURI PER FILOZOF")
        print("=" * 60)

        for philosopher, _ in sorted_philosophers:
            print(f"\n### {philosopher} ({len(titles_by_phil[philosopher])} videoclipuri)")
            for title in titles_by_phil[philosopher][:5]:  # Max 5 titluri
                print(f"  - {title[:70]}{'...' if len(title) > 70 else ''}")
            if len(titles_by_phil[philosopher]) > 5:
                print(f"  ... și încă {len(titles_by_phil[philosopher]) - 5} videoclipuri")
    else:
        print("Nu s-au găsit filozofi în titluri.")

    # Caută potențiale nume necunoscute
    potential = find_unknown_potential_names(titles, set(philosophers.keys()))
    if potential:
        print("\n" + "=" * 60)
        print("POSIBILI FILOZOFI NEIDENTIFICAȚI")
        print("(nume proprii care apar frecvent)")
        print("=" * 60 + "\n")

        for name, count in sorted(potential.items(), key=lambda x: -x[1])[:20]:
            print(f"  {name}: {count} apariții")

    # Salvează în fișier
    output_file = "filozofi_casa_paleologu.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("FILOZOFI DIN VIDEOCLIPURILE CASA PALEOLOGU\n")
        f.write("=" * 50 + "\n\n")

        f.write("LISTĂ ALFABETICĂ:\n")
        f.write("-" * 30 + "\n")
        for phil in sorted(philosophers.keys()):
            f.write(f"- {phil} ({philosophers[phil]} videoclipuri)\n")

        f.write(f"\n\nTOTAL: {len(philosophers)} filozofi unici\n")
        f.write(f"Din {len(titles)} videoclipuri analizate\n")

    print(f"\n✓ Lista salvată în: {output_file}")


if __name__ == "__main__":
    main()

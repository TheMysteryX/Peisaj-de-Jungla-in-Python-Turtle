# Peisaj-de-Jungla-in-Python-Turtle
Un peisaj de junglă desenat în întregime cu biblioteca turtle din Python: sol, copac mare cu rădăcini și umbră, ferigi, plante, o floare, pietricele, crenguțe, frunze căzute și copaci în fundal. Nu sunt folosite imagini sau biblioteci externe, totul este generat din cod, prin mișcări ale „broaștei țestoase" și umpleri de culoare.

> **Previzualizare:** 
> <img width="1797" height="1123" alt="image" src="https://github.com/user-attachments/assets/528f7922-c6d3-49fd-ae2b-33dc73261d62" />
---

## Cuprins

- [Caracteristici](#caracteristici)
- [Cerințe](#cerințe)
- [Rulare](#rulare)
- [Structura codului](#structura-codului)
- [Ordinea de desenare](#ordinea-de-desenare)
- [Sistemul de coordonate](#sistemul-de-coordonate)
- [Personalizare](#personalizare)

---

## Caracteristici

- Scenă de rezoluție mare (**2560 × 1600**), cu fundal verde deschis și sol maro
- Copac central cu rădăcini, trunchi și umbră proprie
- Trei tipuri de ferigi: **drepte**, **aplecate** și variantele lor **oglindite**
- Ferigi de prim-plan (culori închise) și ferigi de fundal (culori pale, pentru efect de adâncime)
- Plante cu 3 frunze și flori cu 6 petale, cu două culori
- Pietricele, o piatră mare cu detalii, crenguțe cu ramuri și frunze căzute
- Desenare rapidă: animația este dezactivată (`tracer(0, 0)`, `speed(0)`)
- Funcții reutilizabile, cu parametri pentru mărime și culoare

## Cerințe

- **Python 3.6+**
- Modulul `turtle`, care vine cu Python (necesită `tkinter`)

## Rulare

```bash
git clone https://github.com/TheMysteryX/Peisaj-de-Jungla-in-Python-Turtle/
cd Peisaj-de-Jungla-in-Python-Turtle
python desen.py
```

## Structura codului

Proiectul este un singur fișier Python, organizat în două părți: **funcții** (definițiile elementelor) și **desenul propriu-zis** (apelurile care compun scena).

### Funcții de bază

| Funcție | Descriere |
|---|---|
| `sol(latime, inaltime, culoare)` | Dreptunghi umplut pentru solul maro (desenat spre dreapta/jos) |
| `fundal(latime, inaltime, culoare)` | Dreptunghi umplut pentru fundalul verde (desenat spre dreapta/sus) |
| `copaci(grosime, cul)` | Trunchi vertical simplu, folosit pentru copacii din fundal |
| `bat(lungime, grosime, culoare)` | Un segment gros; element de bază pentru crengi și tulpini de ferigă |

### Vegetație

| Funcție | Descriere |
|---|---|
| `planta3(lungime, culoare)` | Plantă cu 3 frunze |
| `planta6(lungime, culoare1, culoare2)` | Plantă/floare cu 6 petale, în două culori (`planta3` + încă 3 frunze) |
| `crenguta(lung, gros, cul)` | Crenguță: un băț principal cu mai multe ramuri |

### Elemente de sol

| Funcție | Descriere |
|---|---|
| `pietricica(marime, culoare)` | Formă neregulată, folosită pentru pietricele, piatra mare și **frunze căzute** (cu alte culori) |

### Ferigi

Fiecare tip de ferigă este compus din funcții mici, combinate:

| Funcție | Rol |
|---|---|
| `frunzaFeriga(lungime, culoare)` | O frunză (romb umplut) |
| `pereche_frunze(lungime, culoare)` | O pereche de frunze opuse |
| `inainte(lungime)` | Avansează pe tulpină spre următoarea pereche |
| `feriga(lungime, grosime, cul1, cul2)` | Feriga **dreaptă**, cu frunze în culori alternante |
| `pereche_frunze2`, `inainte2`, `feriga2(lungime, cul1, cul2)` | Feriga **aplecată** |
| `*_mirror` (`frunzaFeriga_mirror`, `feriga_mirror`, `feriga2_mirror`, ...) | Variantele **oglindite** (virează la dreapta în loc de stânga) |
| `ferigaback`, `feriga2back`, `inainte2back` | Variantele de **fundal**, cu culori pale |

Toate ferigile alternează două culori (`cul1`, `cul2`) între perechile de frunze, pentru un aspect mai natural.

## Ordinea de desenare

Ordinea contează, pentru că elementele desenate mai târziu acoperă pe cele anterioare:

1. Solul
2. Fundalul
3. Copacul central (rădăcini și trunchi)
4. Umbra copacului
5. Plantele diverse (`planta3` / `planta6`)
6. Floarea cu centru galben
7. Pietricele și crenguțe pe sol
8. Frunze căzute
9. Piatra mare și detaliile ei
10. Ferigile de prim-plan
11. Copacii din fundal
12. Ferigile din fundal

## Sistemul de coordonate

`turtle` folosește originea `(0, 0)` în **centrul ferestrei**:

- `x` crește spre dreapta, `y` crește în sus
- Ecranul are dimensiunea `2560 × 1600`, deci coordonatele merg aproximativ de la `-1280` la `1280` pe orizontală și de la `-800` la `800` pe verticală
- Linia solului începe la `y = -200`

Elementele sunt poziționate cu `t.penup()` → `t.goto(x, y)` → `t.pendown()`, apoi se apelează funcția dorită.

## Personalizare

**Rezoluția ferestrei**, pentru ecrane mai mici:

```python
turtle.setup(1280, 800)
```

Dacă o modifici, ajustează și dimensiunile din `sol(...)` și `fundal(...)`, plus pozițiile elementelor.

**Adăugarea unui element** (exemplu: o plantă nouă):

```python
t.penup()
t.goto(500, -300)
t.pendown()
planta3(100, "#2E5C2B")
```

**Schimbarea culorilor:** toate culorile sunt coduri hexadecimale (`"#47331d"`), deci pot fi înlocuite direct.

## Note și limitări

- Funcțiile modifică orientarea broaștei (`t.right`, `t.left`) și nu o resetează. Direcția de la un element la altul depinde de apelurile anterioare, deci **mutarea sau eliminarea unei bucăți din codul de desenare poate schimba orientarea elementelor următoare**. Dacă vrei independență între elemente, adaugă `t.setheading(0)` după `t.goto(...)`.
- Cu `tracer(0, 0)` desenul se afișează la intrarea în bucla principală. Dacă imaginea nu apare complet, adaugă `turtle.update()` înainte de `turtle.done()`.
- Fereastra de 2560 × 1600 poate depăși ecranul pe monitoare mici.
- Codul conține multe apeluri repetitive pentru pietricele și frunze. Pot fi înlocuite cu liste de parametri și o buclă:

```python
pietricele = [(-200, -250, 20, "#3d2c1a"), (-500, -400, 15, "#2E1E0F")]
for x, y, marime, culoare in pietricele:
    t.penup(); t.goto(x, y); t.pendown()
    pietricica(marime, culoare)
```
---

*Proiect realizat cu Python și `turtle`.*

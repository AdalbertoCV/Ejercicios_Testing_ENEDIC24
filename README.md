# Pruebas de Software — Ejercicios y proyecto integrador

Repositorio del curso de **Pruebas de Software** (Ingeniería de Software, Universidad Autónoma de Zacatecas, enero–diciembre 2024). Recorre los cuatro niveles de la pirámide de pruebas con Python: **doctest → pruebas unitarias con cobertura → pruebas de aceptación BDD → pruebas end-to-end sobre una aplicación Django real**.

El proyecto integrador es un sistema de votaciones electrónicas, probado en sus tres capas: modelos, formularios y vistas por unidad, y el flujo completo de voto vía navegador con Selenium.

---

## Niveles de prueba cubiertos

### 1. `pruebas_doctest/` — Documentación ejecutable

Pruebas embebidas en la documentación del propio módulo, escritas en archivos `.txt` que se ejecutan como especificación viva.

| Ejercicio | Qué prueba |
|---|---|
| `calculadora/` | Operaciones aritméticas básicas |
| `edades/` | Cálculo de edad a partir de fecha de nacimiento |
| `promedio/` | Promedio de calificaciones |

```bash
python -m doctest pruebas_doctest/calculadora/test_calculadora.txt -v
```

### 2. `pruebas_unitarias/` — `unittest` + cobertura

Siete módulos con su suite de pruebas correspondiente, midiendo cobertura con `coverage.py`:

| Módulo | Reto de prueba |
|---|---|
| `calculadora/` | Operaciones y manejo de división entre cero |
| `edades/` | Casos frontera de fechas |
| `fechas/` | Conversión de fechas y de números a letras |
| `horas_extras/` | Cálculo de nómina con reglas condicionales — buen caso para **cobertura de ramas** |
| `numerosaletra/` | Conversión de números a texto: muchas ramas, mucho caso especial |
| `promedio/` | Promedios y validación de entradas |
| `tenis/` | Sistema de puntuación de tenis (deuce, ventaja, juego) — el ejercicio clásico de partición de equivalencia |

```bash
coverage run -m unittest discover pruebas_unitarias/tenis
coverage report -m
```

### 3. `pruebas_aceptacion/` — BDD con Behave

Pruebas de aceptación escritas en **Gherkin** (`Característica / Escenario / Dado / Cuando / Entonces`), en español, con sus *step definitions* en Python.

| Suite | Escenarios |
|---|---|
| `calculadora/` | Sumar, restar, multiplicar, dividir, potencia y raíz |
| `fechas/` | Conversión de fechas y números a letras |
| `promedio/` | Cálculo de promedios |
| `pruebas_tribunal/` | Automatización de login sobre un sitio real con **Selenium WebDriver** |
| `ejemplo_selenium/` | Ejemplos base de automatización de navegador |

```bash
cd pruebas_aceptacion/calculadora
behave
```

### 4. `proyectos_django/` — Proyecto integrador: sistema de votaciones

Aplicación **Django sobre Docker** que simula una elección presidencial: registro de partidos y candidatos, emisión de voto y cómputo de resultados.

Está probada en todas sus capas:

- **`tests/tests_models.py`** — validación de los modelos `Candidato` y `Partido`.
- **`tests/test_forms.py`** — validación de formularios de registro.
- **`tests/test_views.py`** — respuestas de las vistas de votación y resultados.
- **`pruebas_aceptacion/features/`** — cuatro suites BDD end-to-end con Selenium: `login`, `registro_partido`, `registro_candidato` y `votar`, ejecutando el flujo real en el navegador contra la app levantada.

### `Notas/`

Apuntes teóricos del curso — por ahora, **complejidad ciclomática** y su relación con el número mínimo de casos de prueba necesarios para cubrir todos los caminos.

---

## Estructura del repositorio

```
.
├── pruebas_doctest/          # Nivel 1: doctest
│   └── calculadora/  edades/  promedio/
├── pruebas_unitarias/        # Nivel 2: unittest + coverage
│   └── calculadora/  edades/  fechas/  horas_extras/
│       numerosaletra/  promedio/  tenis/
├── pruebas_aceptacion/       # Nivel 3: BDD con Behave + Selenium
│   ├── calculadora/  fechas/  promedio/
│   ├── pruebas_tribunal/     #   login automatizado con Selenium
│   └── ejemplo_selenium/     #   ejemplos base
├── proyectos_django/         # Nivel 4: proyecto integrador
│   ├── app/votantes/
│   │   ├── candidatos/       #   modelos, vistas, formularios
│   │   ├── candidatos/tests/ #   pruebas unitarias por capa
│   │   └── pruebas_aceptacion/features/   # BDD end-to-end
│   ├── Dockerfile
│   └── docker-compose.yml    #   Django + MariaDB
├── Notas/                    # Apuntes teóricos
├── .env.example              # Plantilla de variables de entorno
└── .gitignore
```

---

## Cómo ejecutarlo

### Ejercicios sueltos

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install coverage behave selenium
```

Después, cada bloque se corre como se indica en su sección arriba.

### Proyecto de votaciones

```bash
cd proyectos_django
cp ../.env.example .env      # y edita los valores
docker compose up --build
```

La aplicación queda en `http://localhost:8000`.

Para las pruebas end-to-end necesitas además el **driver del navegador** (`chromedriver` o `geckodriver`) en el `PATH`, y la aplicación levantada:

```bash
cd app/votantes/pruebas_aceptacion
behave
```

---

## Configuración de credenciales

Este repositorio **no incluye credenciales**. Antes de correr las pruebas que las requieren:

- Copia `.env.example` a `proyectos_django/.env` y rellena los valores.
- Copia `pruebas_aceptacion/ejemplo_selenium/credenciales.example.py` a `credenciales.py` en el mismo directorio.

Ambos archivos están listados en `.gitignore`.

---

## Stack

`Python 3` · `Django` · `unittest` · `doctest` · `coverage.py` · `Behave (BDD/Gherkin)` · `Selenium WebDriver` · `MariaDB` · `Docker` · `Docker Compose`

---

## Autor

**Adalberto Cerrillo Vázquez** — Ingeniería de Software, Universidad Autónoma de Zacatecas.

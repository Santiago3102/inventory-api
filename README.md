# Inventario Simple para Pyme o Tienda

Sistema web de control de inventario para pequeños negocios: registra productos,
entradas y salidas de stock, y avisa cuándo reabastecer.

Proyecto del curso Laboratorio de Ingeniería de Software
Universidad Tecnológica de Pereira · 2026

## Problema
Las tiendas pequeñas controlan el inventario en cuadernos u hojas de cálculo, lo que
genera desabastecimiento no detectado y pérdida de ventas.

## Alcance del MVP
**Incluye:** CRUD de productos, entradas y salidas de stock, alertas de reabastecimiento
(stock actual ≤ stock mínimo) e historial de movimientos por producto.
**No incluye:** proveedores, facturación/POS, múltiples bodegas.

## Stack
Python 3.12 · FastAPI · SQLAlchemy · MySQL 8 · HTML/CSS/JS con Bootstrap 5
Despliegue: Render (app) · Clever Cloud / Railway (base de datos)

## Estructura del repositorio
- `docs/` documentación y diagramas
- `poc/` prueba de concepto (su propio README explica qué valida y qué no)
- `backend/` API REST con FastAPI
- `frontend/` interfaz web (HTML, CSS y JavaScript)

## Documentación
- Documento del proyecto: <enlace [a Google Docs](https://docs.google.com/document/d/1tZEDNvzFRlC8dB1_9uhR_n7Gy4cXLfz2aa_CrzRTJp8/edit?usp=sharing)>
- Backlog y casos de uso: <enlace [a Google Sheets](https://docs.google.com/spreadsheets/d/1C_jGg-3STGPluSnixYa9JC384XM4tP1b/edit?usp=sharing&ouid=102417051153349433992&rtpof=true&sd=true)>
- Mockups: <enlace [a Figma](https://www.figma.com/make/Sr5qpNLfsaOiDtHOSE4Nli/Sistema-de-Control-de-Inventario?t=3FZHfwTcKhbPNIU3-20&fullscreen=1)>

## Cómo ejecutar
Pendiente: se completará al terminar el sprint 1.

## Flujo de trabajo
Ramas: `main` (estable) ← `develop` (integración) ← `feature/*`.
Todo cambio entra por Pull Request, nunca directo a `main` ni a `develop`.

## Equipo
- Santiago Gomez Ramirez
- Juan Diego Gil Arango
- Juan David Roman Marin

Docente: Juan Manuel Mejia Naranjo

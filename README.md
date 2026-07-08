# django-crud-react — API REST con Django + cliente en ViteJS

> 🚧 Proyecto en desarrollo.

REST API construida con Django (`crudApi`, `tasks`) que expone endpoints para enviar y gestionar datos. El plan es consumir esa API desde un cliente creado con **ViteJS**, realizando las peticiones HTTP correspondientes, y estilizarlo con **TailwindCSS**.

## Contenido

- `crudApi/` — configuración del proyecto Django.
- `tasks/` — app Django con los modelos y endpoints de la API.
- `manage.py`, `db.sqlite3` — proyecto Django y base de datos de desarrollo.

## Tecnologías

Python · Django · REST API · ViteJS (cliente, en desarrollo) · TailwindCSS (planeado)

## Cómo ejecutar el backend

```bash
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

## Autor

Horacio Laphitz — [GitHub](https://github.com/HoracioLaphitz) · [LinkedIn](https://www.linkedin.com/in/horacio-laphitz)

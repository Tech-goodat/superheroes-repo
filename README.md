# Superheroes Flask API

This Flask API project is designed to track heroes and their superpowers. It provides various endpoints for managing heroes, powers, and their associations.

## Developer Information

**Developer:** Felix Kiprotich

**Email:** felixkiprotich2000@gmail.com

## Setup

To set up the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies for both the backend and frontend:
   ```bash
   pipenv install
   pipenv shell
   npm install --prefix client
   ```
3. Initialize and migrate the database:
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db upgrade head
   ```
4. Seed the database with initial data:
   ```bash
   flask db revision --autogenerate -m 'Initial migration'
   flask db upgrade head
   python server/seed.py
   ```

## Running the Flask API

To run the Flask API, execute the following command in your terminal:

```bash
python server/app.py
```

The Flask API will be accessible at [`http://localhost:5555`](http://localhost:5555).

## Endpoints

### 1. GET /heroes

Returns a list of heroes in JSON format.

### 2. GET /heroes/:id

Returns details of a specific hero identified by `id` in JSON format.

### 3. GET /powers

Returns a list of powers in JSON format.

### 4. GET /powers/:id

Returns details of a specific power identified by `id` in JSON format.

### 5. PATCH /powers/:id

Updates an existing power identified by `id`. Accepts an object with a `description` property in the request body.

### 6. POST /hero_powers

Creates a new `HeroPower` association between a hero and a power. Accepts an object with `strength`, `power_id`, and `hero_id` properties in the request body.

---

With these endpoints, you can manage heroes, powers, and their associations effectively using the Flask API provided in this project. Feel free to test the endpoints using Postman, pytest, or the included React frontend application.
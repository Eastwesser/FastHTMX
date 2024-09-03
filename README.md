# FastHTMX Project

This is a simple FastAPI project template using HTMX for dynamic web applications.

## Project Structure

  - `app/`: Contains the main application logic.
  - `api/`: Holds API versioning and endpoints.
  - `core/`: Contains core configurations and middleware.
  - `models/`: (Empty) For future database models and schemas.
  - `templates/`: Contains Jinja2 templates for rendering HTML.
  - `static/`: Directory for static files like CSS, JavaScript, images.

- `tests/`: Contains unit tests for the project.

## How to Run

1. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the development server**:

    ```sh
    uvicorn app.main:app --reload
    ```

4. **Open your browser and navigate to** `http://127.0.0.1:8000/`

## Testing

You can run tests using `pytest`:

```sh
pytest
```

You can also use http files to manually test endpoints using a tool like HTTPie.

5. **Environment Variables**

This project uses a .env file to manage environment variables. Example:

.env

```text
PROJECT_NAME=FastHTMX
API_V1_STR=/api/v1
CSRF_SECRET=your-secret-key
```

## Requirements
- Python 3.10+
- FastAPI
- HTMX
- Jinja2
- Starlette CSRF Middleware
- Uvicorn

### requirements.txt:

```text
annotated-types==0.7.0
anyio==4.4.0
click==8.1.7
colorama==0.4.6
exceptiongroup==1.2.2
fastapi==0.112.2
h11==0.14.0
idna==3.8
iniconfig==2.0.0
Jinja2==3.1.4
MarkupSafe==2.1.5
packaging==24.1
pluggy==1.5.0
pydantic==2.8.2
pydantic_core==2.20.1
pytest==8.3.2
python-dotenv==1.0.1
sniffio==1.3.1
starlette==0.38.4
tomli==2.0.1
typing_extensions==4.12.2
uvicorn==0.30.6
```

Project started: 3rd September 2024

"# FastHTMX" 

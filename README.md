# Small template for connecting django to react

Installation
------------

#### Python => 3.11

#### Node => 18.4.0

Start
-----

```
docker-compose up
```

### Ports here

```docker-compose.yaml```

```dockerfile
version: "3"

services:
  backend:
    build: backend
    env_file:
      - backend/.env
    ports:
      - "8000:8000"

  frontend:
    build: frontend
    ports:
      - "3001:3000"
```

### Standard ports

* [Backend](http://localhost:8000/): 8000
* [Frontend](http://localhost:3001/): 3001

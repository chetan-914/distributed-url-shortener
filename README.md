
# Distributed URL Shortener

---

## 🚀 Overview

This project is a **distributed, production-oriented URL Shortener service** built using modern backend architecture principles.

It is designed to handle:

* High read traffic
* Distributed ID generation
* Cache protection
* Database connection pooling
* Containerized deployment

The system uses:

* FastAPI for API layer
* PostgreSQL for persistence
* PgBouncer for connection pooling
* Redis for caching
* Bloom Filters for cache penetration protection
* Snowflake algorithm for distributed ID generation
* Base62 encoding for short URL generation
* Docker & Docker Compose for orchestration

---

## 🏗 System Architecture

```
Client
  ↓
FastAPI Service
  ↓
Redis Cache (Read-through)
  ↓
Bloom Filter (Existence Check)
  ↓
PostgreSQL (via PgBouncer)
```

---

## ✨ Key Features

### 🔗 URL Shortening

* Converts long URLs into short, unique, Base62 encoded URLs
* Uses Snowflake distributed ID generator (no DB bottleneck)

---

### ⚡ High Performance Caching

* Redis read-through caching
* Write-through cache population
* Configurable TTL

---

### 🌸 Bloom Filter Protection

Prevents cache/database penetration by rejecting invalid short codes before hitting DB.

Guarantees:

* No false negatives
* Minimal DB load during attacks

---

### 🧠 Distributed ID Generation

Snowflake ID structure:

```
Timestamp + Machine ID + Sequence
```

Benefits:

* Globally unique IDs
* Time sortable
* High throughput generation

---

### 🗄 Database Layer

* PostgreSQL for persistence
* PgBouncer for connection pooling
* Optimized for high concurrency

---

### 🐳 Containerized Infrastructure

Runs using Docker Compose:

* FastAPI service
* PostgreSQL
* PgBouncer
* Redis

---

## 🛠 Tech Stack

| Layer            | Technology             |
| ---------------- | ---------------------- |
| API              | FastAPI                |
| ORM              | SQLAlchemy             |
| Database         | PostgreSQL             |
| Connection Pool  | PgBouncer              |
| Cache            | Redis                  |
| ID Generation    | Snowflake Algorithm    |
| Encoding         | Base62                 |
| Protection       | Bloom Filter           |
| Containerization | Docker, Docker Compose |

---

## 📁 Project Structure

```
app/
 ├ main.py
 │ 
 ├ core/
 │ ├ config.py
 │ ├ database.py
 │ ├ redis.py
 │ ├ bloom_filter.py
 │
 ├ models/
 │ ├ base.py
 │ ├ url.py
 │
 ├ schemas/
 │ ├ url.py
 │
 ├ services/
 │ ├ id_generator.py
 │ ├ url_service.py
 │
 ├ utils/
 │ ├ base62.py
 │
 ├ api/
 │ ├ routes/
 │ │ ├ url.py
 │
 ├ scripts/
 │ ├ init_db.py
```

---

## ⚙️ How It Works

### Create Short URL

```
POST /urls
```

Flow:

1. Validate request
2. Generate Snowflake ID
3. Base62 encode
4. Store in PostgreSQL
5. Cache in Redis
6. Insert into Bloom Filter

---

### Redirect

```
GET /{short_code}
```

Flow:

1. Bloom filter check
2. Redis lookup
3. PostgreSQL fallback
4. Redirect response

---

## 🐳 Running with Docker

### Start Services

```
docker compose up --build
```

---

### Stop Services

```
docker compose down
```

---

## 🔧 Environment Configuration

Example environment variables:

```
DATABASE_URL=postgresql://user:pass@postgres:6432/db
REDIS_URL=redis://redis:6379
BASE_URL=http://localhost:8000
MACHINE_ID=1
```

---

## 📊 Performance Optimizations

* PgBouncer connection pooling
* Redis caching layer
* Bloom filter request filtering
* Stateless API servers
* Distributed ID generation

---

## 🔐 Production Considerations

Planned / Future Enhancements:

* Nginx reverse proxy
* HTTPS termination
* Async DB handling
* Horizontal FastAPI scaling
* Metrics & Observability
* Rate limiting
* Distributed Bloom filters

---

## 🧪 Testing

Manual testing via:

* Postman
* curl
* Browser redirect testing

---

## 📌 Future Improvements

* Async SQLAlchemy
* Redis Cluster support
* Kafka-based analytics pipeline
* Click tracking analytics
* Multi-region deployment

---

## 🧠 Design Philosophy

Built using:

* First-principles system design
* Separation of concerns
* Service-oriented layering
* Production-first thinking

---

## 👨‍💻 Author

Built as a distributed systems backend engineering project.

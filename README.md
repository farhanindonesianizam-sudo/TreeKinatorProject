# TreeKinatorProject
TreeKinatorProject_DataStructure

# 🌳 TreeKinator — Binary Tree Informatics Recommendation System

TreeKinator adalah aplikasi berbasis **Binary Tree Decision System** yang membantu pengguna menentukan jalur pembelajaran, bahasa pemrograman, framework, dan teknologi terbaik berdasarkan minat di bidang Informatika.

Project ini menggunakan:

- ⚡ FastAPI sebagai Backend API
- 🎨 Vue.js + Vite sebagai Frontend
- 🌲 Binary Tree sebagai Recommendation Logic
- 🔄 REST API Communication
- 🧠 Object-Oriented Programming (OOP)

---

# 📚 Table of Contents

- Features
- Technologies Used
- Project Structure
- Requirements
- Clone Repository
- Backend Installation
- Frontend Installation
- Running Backend
- Running Frontend
- Running Full Project
- API Documentation
- API Endpoints
- How TreeKinator Works
- Example Decision Flow
- Screenshots
- Common Errors
- Future Development
- Developer
- License

---

# 🚀 Features

✅ Binary Tree Recommendation System  
✅ Strict 3-Stage Decision Logic  
✅ 6 Informatics Categories  
✅ FastAPI REST API  
✅ Vue.js Frontend  
✅ JSON-Based Communication  
✅ Swagger Documentation  
✅ OOP-Based Architecture  
✅ Frontend & Backend Separation  
✅ CORS Enabled  

---

# 🌲 Informatics Categories

| ID | Category |
|---|---|
| 1 | Web Development |
| 2 | Mobile Development |
| 3 | Data Science & AI |
| 4 | Game Development |
| 5 | Cyber Security |
| 6 | IoT & Robotics |

---

# 🛠️ Technologies Used

## Backend

| Technology | Function |
|---|---|
| Python | Main Programming Language |
| FastAPI | Backend Framework |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |

---

## Frontend

| Technology | Function |
|---|---|
| Vue.js | Frontend Framework |
| Vite | Frontend Build Tool |
| JavaScript | Frontend Logic |

---

# 📂 Project Structure

```bash
BINARY_TREE_PROJECT/
│
├── backend/
│   ├── __pycache__/
│   └── main.py
│
├── frontend/
│   ├── .vscode/
│   │   ├── extensions.json
│   │   └── settings.json
│   │
│   ├── node_modules/
│   │
│   ├── public/
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── App.vue
│   │   └── main.js
│   │
│   ├── .gitignore
│   ├── index.html
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
│
├── logic_terminal.py
├── main_2.py
└── README.md
```

---

# 📋 Requirements

Sebelum menjalankan project ini, pastikan sudah menginstall:

| Software | Version |
|---|---|
| Python | 3.10+ |
| Node.js | 18+ |
| npm | Latest |
| Git | Latest |

---

# 🔎 Check Installed Version

## Python

```bash
python --version
```

---

## Node.js

```bash
node -v
```

---

## npm

```bash
npm -v
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/BINARY_TREE_PROJECT.git
```

Masuk ke folder project:

```bash
cd BINARY_TREE_PROJECT
```

---

# ⚙️ Backend Installation

## 1. Open Backend Folder

```bash
cd backend
```

---

## 2. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### MacOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Backend Dependencies

Install manual:

```bash
pip install fastapi uvicorn pydantic
```

---

## Alternative Using requirements.txt

Create `requirements.txt` file:

```txt
fastapi
uvicorn
pydantic
```

Then install:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Backend Server

Masih di folder `backend`, jalankan:

```bash
python -m uvicorn main:app --reload
```

Jika berhasil, terminal akan menampilkan:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Backend API Documentation

Setelah backend berjalan:

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🎨 Frontend Installation

## 1. Open Frontend Folder

Buka terminal baru:

```bash
cd frontend
```

---

## 2. Install Frontend Dependencies

```bash
npm install
```

Dependencies akan otomatis diinstall berdasarkan file:

```text
package.json
```

---

# ▶️ Running Frontend

Masih di folder `frontend`, jalankan:

```bash
npm run dev
```

Jika berhasil, terminal akan menampilkan:

```bash
VITE vX.X.X ready in XXX ms

➜ Local: http://localhost:5173/
```

Buka browser:

```text
http://localhost:5173
```

---

# 🚀 Running Full Project

TreeKinator membutuhkan:

✅ Backend berjalan  
✅ Frontend berjalan  

Gunakan 2 terminal berbeda.

---

# 🖥️ Terminal 1 — Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

---

# 🎨 Terminal 2 — Frontend

```bash
cd frontend
npm run dev
```

---

# 🌐 Access Project

## Frontend

```text
http://localhost:5173
```

---

## Backend API

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

---

# 1. Root Endpoint

## Request

```http
GET /
```

## Response

```json
{
  "message": "Informatics Forest API is Active! API backend siap melayani frontend Anda."
}
```

---

# 2. Get All Forests

Mengambil semua kategori utama TreeKinator.

## Request

```http
GET /api/forests
```

## Response Example

```json
[
  {
    "id": "1",
    "name": "Web Development",
    "root_node_id": "WEB_ROOT"
  },
  {
    "id": "2",
    "name": "Mobile Development",
    "root_node_id": "MOB_ROOT"
  }
]
```

---

# 3. Get Specific Node

Mengambil node tertentu berdasarkan `node_id`.

## Request

```http
GET /api/node/{node_id}
```

---

## Example

```http
GET /api/node/WEB_ROOT
```

---

## Response Example

```json
{
  "id": "WEB_ROOT",
  "question": "Fokus ke Visual/Frontend (1) atau Logika/Backend (2)?",
  "is_leaf": false,
  "result": null,
  "frameworks": [],
  "left_id": "W_FE",
  "right_id": "W_BE"
}
```

---

# 🌲 How TreeKinator Works

TreeKinator menggunakan konsep:

# Strict 3-Stage Binary Tree

Setiap node memiliki:

- Pertanyaan
- Left Child
- Right Child

Pengguna akan terus memilih jalur hingga mencapai:

✅ Bahasa Pemrograman  
✅ Framework  
✅ Ecosystem Recommendation  

---

# 🧠 Example Decision Flow

```text
Web Development
│
├── Backend
│   ├── Production Speed
│   │   ├── AI Ecosystem
│   │   │   └── Python + FastAPI/Django
```

---

# 🔥 Example Recommendations

| Category | Recommendation |
|---|---|
| Frontend Web | JavaScript + React |
| Enterprise Web | TypeScript + Angular |
| Backend AI | Python + FastAPI |
| Mobile Cross Platform | Dart + Flutter |
| AI Engineering | Python + TensorFlow |
| Game Development | C++ + Unreal Engine |
| Cyber Security | Go + Nuclei |
| Embedded System | C + Arduino |

---

# 🧪 Testing API Using Swagger

## Example Testing `/api/node/WEB_ROOT`

### Step 1

Open browser:

```text
http://127.0.0.1:8000/docs
```

---

### Step 2

Find endpoint:

```text
GET /api/node/{node_id}
```

---

### Step 3

Click:

```text
Try it out
```

---

### Step 4

Input:

```text
WEB_ROOT
```

---

### Step 5

Click:

```text
Execute
```

---

# 🏗️ System Architecture

```text
Frontend (Vue.js)
        ↓
REST API Communication
        ↓
Backend (FastAPI)
        ↓
Binary Tree Logic Engine
```

---

# 📸 Screenshots

## Frontend

```text
Add your frontend screenshot here
```

Example:

```md
![Frontend](./screenshots/frontend.png)
```

---

## Swagger API

```md
![Swagger](./screenshots/swagger.png)
```

---

# 🚫 Files Not Uploaded to GitHub

Folder berikut biasanya tidak diupload:

```text
node_modules/
venv/
__pycache__/
```

Karena folder tersebut akan dibuat otomatis setelah install dependencies.

---

# ⚠️ Important Notes

## CORS Configuration

Saat development:

```python
allow_origins=["*"]
```

Untuk production, sebaiknya diganti dengan domain frontend asli.

---

## In-Memory Database

Project ini masih menggunakan:

```python
db_nodes = {}
```

Data akan reset ketika server dimatikan.

---

# ❌ Common Errors

---

# 1. Address Already in Use

Jika muncul:

```bash
Address already in use
```

Gunakan port lain:

```bash
python -m uvicorn main:app --reload --port 8001
```

---

# 2. npm command not found

Install Node.js terlebih dahulu:

```text
https://nodejs.org
```

---

# 3. Module Not Found

Install dependencies kembali:

```bash
pip install -r requirements.txt
```

atau:

```bash
npm install
```

---

# 4. CORS Error

Pastikan backend FastAPI sedang berjalan:

```text
http://127.0.0.1:8000
```

---

# 📈 Future Development

- [ ] Authentication System
- [ ] User Session
- [ ] Database Integration
- [ ] Recommendation History
- [ ] Binary Tree Visualization
- [ ] Admin Dashboard
- [ ] Docker Support
- [ ] Cloud Deployment

---

# 👨‍💻 Developer

Developed by:

# Farhan Nizam S.A

---

# 📜 License

This project is licensed under the MIT License.

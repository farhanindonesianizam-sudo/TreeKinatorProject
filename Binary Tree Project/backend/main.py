'''### Cara Menguji Backend Ini:
1.  Buka terminal VS Code di folder proyekmu.
2.  Jalankan servernya dengan perintah:
    ```bash
   python -m uvicorn main:app --reload 
    ```
3.  Buka *browser* dan akses **http://127.0.0.1:8000/docs**. Di sana, kamu bisa menguji langsung endpoint `/api/forests` dan `/api/node/{node_id}` (misalnya ketikkan `WEB_ROOT` di kotak inputnya) untuk memastikan data JSON-nya keluar dengan benar sebelum nanti disambungkan ke Vue.js.

Apakah API ini sudah berhasil berjalan dan mengeluarkan *response* JSON saat kamu uji di *browser*? Kabari saya jika kamu butuh bantuan *testingSiap! Keputusan yang sangat tepat untuk memisahkan fokus. Menyelesaikan *backend* (mesinnya) terlebih dahulu sambil menunggu desain *frontend* (tampilannya) matang adalah alur kerja standar di industri *Software Engineering*.

Seperti yang sempat kita singgung, karena FastAPI berjalan di *server*, sifatnya adalah **Stateless** (tidak mengingat interaksi sebelumnya). Jadi, alih-alih menggunakan `while True` dan `input()` seperti di terminal, kita akan membuat *endpoint* API (URL) yang bisa ditanya oleh *frontend* menggunakan `node_id`.

Berikut adalah **kode lengkap `main.py`** untuk *backend* FastAPI kamu. Kode ini sudah memuat ke-6 cabang IT lengkap dengan logika *Strict 3-Stage Binary Tree* yang sudah kita sepakati.

### File: `main.py`
```python'''
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Informatics Forest API")

# Konfigurasi CORS (Wajib agar Vue.js nanti bisa mengambil data dari FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Saat produksi, ganti dengan URL frontend Vue.js kamu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# 1. PYDANTIC MODELS (Format Response JSON)
# ==========================================
class NodeResponse(BaseModel):
    id: str
    question: Optional[str] = None
    is_leaf: bool
    result: Optional[str] = None
    frameworks: Optional[List[str]] = None
    left_id: Optional[str] = None
    right_id: Optional[str] = None

class TreeInfo(BaseModel):
    id: str
    name: str
    root_node_id: str

# ==========================================
# 2. OOP CORE LOGIC
# ==========================================
class Node:
    def __init__(self, id, question=None, result=None, frameworks=None):
        self.id = id
        self.question = question
        self.result = result
        self.frameworks = frameworks or []
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.result is not None

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "is_leaf": self.is_leaf(),
            "result": self.result,
            "frameworks": self.frameworks,
            "left_id": self.left.id if self.left else None,
            "right_id": self.right.id if self.right else None,
        }

# ==========================================
# 3. DATABASE IN-MEMORY & BUILDERS
# ==========================================
db_nodes = {}

def register_tree(node: Node):
    """Mendaftarkan node beserta semua anak-anaknya ke dalam dictionary (O(1) search)"""
    if node is None:
        return
    db_nodes[node.id] = node
    register_tree(node.left)
    register_tree(node.right)

# --- TREE BUILDERS ---
def build_web_tree():
    root = Node("WEB_ROOT", "Fokus ke Visual/Frontend (1) atau Logika/Backend (2)?")
    
    # Kiri: Frontend
    fe = Node("W_FE", "Aplikasi Web Fungsional (1) atau Pengalaman Visual/Kreatif (2)?")
    fe.left = Node("W_FE_APP", "Standard Web (1) atau Enterprise/Scale (2)?")
    fe.left.left = Node("R_W1", result="JavaScript", frameworks=["Vue.js", "React"])
    fe.left.right = Node("R_W2", result="TypeScript", frameworks=["Angular", "Next.js"])
    
    fe.right = Node("W_FE_EXP", "2D Animation (1) atau 3D Simulation (2)?")
    fe.right.left = Node("R_W3", result="JavaScript", frameworks=["GSAP", "PixiJS"])
    fe.right.right = Node("R_W4", result="C++ (Wasm)", frameworks=["Three.js", "Emscripten"])
    
    # Kanan: Backend
    be = Node("W_BE", "Mengutamakan Performa Eksekusi (1) atau Kecepatan Produksi (2)?")
    be.left = Node("W_BE_PERF", "High Concurrency (1) atau System Safety (2)?")
    be.left.left = Node("R_W5", result="Go", frameworks=["Gin", "Fiber"])
    be.left.right = Node("R_W6", result="Rust", frameworks=["Actix", "Rocket"])
    
    be.right = Node("W_BE_PROD", "AI Ecosystem (1) atau Rapid Web Dev (2)?")
    be.right.left = Node("R_W7", result="Python", frameworks=["FastAPI", "Django"])
    be.right.right = Node("R_W8", result="PHP", frameworks=["Laravel", "Symfony"])

    root.left = fe
    root.right = be
    return root

def build_mobile_tree():
    root = Node("MOB_ROOT", "Multi-platform / 1 Codebase (1) atau Native spesifik OS (2)?")
    
    multi = Node("M_MULTI", "Fokus pada UI Modern (1) atau Kebutuhan Bisnis/Arsitektur (2)?")
    multi.left = Node("M_M_UI", "Pixel Perfect UI (1) atau Web-like Logic (2)?")
    multi.left.left = Node("R_M1", result="Dart", frameworks=["Flutter"])
    multi.left.right = Node("R_M2", result="JavaScript", frameworks=["React Native"])
    
    multi.right = Node("M_M_BIZ", "Enterprise Level (1) atau C# Ecosystem (2)?")
    multi.right.left = Node("R_M3", result="Java", frameworks=["Codename One"])
    multi.right.right = Node("R_M4", result="C#", frameworks=[".NET MAUI"])
    
    native = Node("M_NATIVE", "Target Utama Android (1) atau iOS/Apple (2)?")
    native.left = Node("M_N_AND", "Modern Jetpack (1) atau Legacy Support XML (2)?")
    native.left.left = Node("R_M5", result="Kotlin", frameworks=["Jetpack Compose"])
    native.left.right = Node("R_M6", result="Java", frameworks=["Android SDK"])
    
    native.right = Node("M_N_IOS", "Modern SwiftUI (1) atau Objective-C Legacy (2)?")
    native.right.left = Node("R_M7", result="Swift", frameworks=["SwiftUI"])
    native.right.right = Node("R_M8", result="Objective-C", frameworks=["UIKit"])

    root.left = multi
    root.right = native
    return root

def build_data_tree():
    root = Node("DAT_ROOT", "Fokus ke Kecerdasan Data/AI (1) atau Rekayasa/Infrastruktur (2)?")
    
    intel = Node("D_INTEL", "Fokus Pemodelan AI (1) atau Analisis & Visualisasi Data (2)?")
    intel.left = Node("D_I_MOD", "Deep Learning (1) atau Statistical Math (2)?")
    intel.left.left = Node("R_D1", result="Python", frameworks=["PyTorch", "TensorFlow"])
    intel.left.right = Node("R_D2", result="R", frameworks=["Tidyverse", "Shiny"])
    
    intel.right = Node("D_I_ANA", "Fast Execution (1) atau Web Data Viz (2)?")
    intel.right.left = Node("R_D3", result="Julia", frameworks=["Flux.jl", "DataFrames"])
    intel.right.right = Node("R_D4", result="JavaScript", frameworks=["D3.js", "Chart.js"])
    
    eng = Node("D_ENG", "Infrastruktur Big Data (1) atau Manajemen Storage Database (2)?")
    eng.left = Node("D_E_BIG", "Memory Processing (1) atau Stream Processing (2)?")
    eng.left.left = Node("R_D5", result="Scala", frameworks=["Apache Spark"])
    eng.left.right = Node("R_D6", result="Java", frameworks=["Apache Flink"])
    
    eng.right = Node("D_E_DB", "Relational SQL (1) atau NoSQL Scalability (2)?")
    eng.right.left = Node("R_D7", result="SQL", frameworks=["PostgreSQL", "MySQL"])
    eng.right.right = Node("R_D8", result="Java/Go", frameworks=["Cassandra", "MongoDB"])

    root.left = intel
    root.right = eng
    return root

def build_game_tree():
    root = Node("GAM_ROOT", "Fokus Visual/Engine Power (1) atau Logika Sistem Core (2)?")
    
    eng = Node("G_ENG", "Fokus 3D Power (1) atau 2D/Indie (2)?")
    eng.left = Node("G_E_3D", "Hardcore Control (1) atau Balanced Dev (2)?")
    eng.left.left = Node("R_G1", result="C++", frameworks=["Unreal Engine"])
    eng.left.right = Node("R_G2", result="C#", frameworks=["Unity Engine"])
    
    eng.right = Node("G_E_2D", "Scripting Focus (1) atau Browser Based (2)?")
    eng.right.left = Node("R_G3", result="C#", frameworks=["Godot", "Monogame"])
    eng.right.right = Node("R_G4", result="JavaScript", frameworks=["Phaser", "Babylon.js"])
    
    logic = Node("G_LOG", "System Level Core (1) atau Gameplay AI/Scripting (2)?")
    logic.left = Node("G_L_COR", "Standard C++ (1) atau Modern Memory Safety (2)?")
    logic.left.left = Node("R_G5", result="C++", frameworks=["DirectX", "Vulkan"])
    logic.left.right = Node("R_G6", result="Rust", frameworks=["Bevy Engine"])
    
    logic.right = Node("G_L_SCR", "Simplicity (1) atau Complex Logic (2)?")
    logic.right.left = Node("R_G7", result="Lua", frameworks=["Roblox", "LÖVE"])
    logic.right.right = Node("R_G8", result="Python", frameworks=["Pygame"])

    root.left = eng
    root.right = logic
    return root

def build_security_tree():
    root = Node("SEC_ROOT", "Offensive / Penyerangan (1) atau Defensive / Pertahanan (2)?")
    
    off = Node("S_OFF", "Eksploitasi Sistem Core (1) atau Web Breach/Scanning (2)?")
    off.left = Node("S_O_EXP", "Low-level Memory (1) atau Network/Automation (2)?")
    off.left.left = Node("R_S1", result="C / C++", frameworks=["GDB", "Binary Ninja"])
    off.left.right = Node("R_S2", result="Python", frameworks=["Scapy", "Metasploit"])
    
    off.right = Node("S_O_WEB", "Fast Scanning (1) atau DOM Manipulation (2)?")
    off.right.left = Node("R_S3", result="Go", frameworks=["Nuclei", "Custom Tools"])
    off.right.right = Node("R_S4", result="JavaScript", frameworks=["XSS Payloads"])
    
    defen = Node("S_DEF", "Proteksi Aktif (1) atau Forensik Data (2)?")
    defen.left = Node("S_D_PRO", "Threat Detection (1) atau Firewall Logic (2)?")
    defen.left.left = Node("R_S5", result="Python", frameworks=["Log Parsers", "ML Detection"])
    defen.left.right = Node("R_S6", result="Go", frameworks=["Network Filters"])
    
    defen.right = Node("S_D_FOR", "System Analysis (1) atau Data Recovery (2)?")
    defen.right.left = Node("R_S7", result="Bash / Shell", frameworks=["Linux Tools", "Volatility"])
    defen.right.right = Node("R_S8", result="C++", frameworks=["Custom Recovery Tools"])

    root.left = off
    root.right = defen
    return root

def build_iot_tree():
    root = Node("IOT_ROOT", "Fokus Embedded Hardware (1) atau Logika Robotika (2)?")
    
    emb = Node("I_EMB", "Micro-controller Dasar (1) atau Perangkat Terhubung/IoT (2)?")
    emb.left = Node("I_E_MIC", "Real-time Bare Metal (1) atau Modern Embedded (2)?")
    emb.left.left = Node("R_I1", result="C", frameworks=["Arduino", "FreeRTOS"])
    emb.left.right = Node("R_I2", result="Rust", frameworks=["Embedded HAL"])
    
    emb.right = Node("I_E_CON", "High Level IoT (1) atau Linux Gateway (2)?")
    emb.right.left = Node("R_I3", result="MicroPython", frameworks=["ESP32", "Pi Pico"])
    emb.right.right = Node("R_I4", result="C++", frameworks=["Qt for Embedded"])
    
    rob = Node("I_ROB", "Core Control/Gerak (1) atau Computer Vision (2)?")
    rob.left = Node("I_R_CON", "Standard ROS (1) atau AI Prototyping (2)?")
    rob.left.left = Node("R_I5", result="C++", frameworks=["ROS2"])
    rob.left.right = Node("R_I6", result="Python", frameworks=["PyRobot", "MoveIt"])
    
    rob.right = Node("I_R_VIS", "Edge Analysis (1) atau IoT Integrated (2)?")
    rob.right.left = Node("R_I7", result="C++", frameworks=["OpenCV"])
    rob.right.right = Node("R_I8", result="JavaScript", frameworks=["Johnny-Five"])

    root.left = emb
    root.right = rob
    return root

# --- Inisialisasi Data ---
register_tree(build_web_tree())
register_tree(build_mobile_tree())
register_tree(build_data_tree())
register_tree(build_game_tree())
register_tree(build_security_tree())
register_tree(build_iot_tree())

forest_list = [
    {"id": "1", "name": "Web Development", "root_node_id": "WEB_ROOT"},
    {"id": "2", "name": "Mobile Development", "root_node_id": "MOB_ROOT"},
    {"id": "3", "name": "Data Science & AI", "root_node_id": "DAT_ROOT"},
    {"id": "4", "name": "Game Development", "root_node_id": "GAM_ROOT"},
    {"id": "5", "name": "Cyber Security", "root_node_id": "SEC_ROOT"},
    {"id": "6", "name": "IoT & Robotics", "root_node_id": "IOT_ROOT"},
]

# ==========================================
# 4. API ENDPOINTS
# ==========================================
@app.get("/", tags=["General"])
def read_root():
    return {"message": "Informatics Forest API is Active! API backend siap melayani frontend Anda."}

@app.get("/api/forests", response_model=List[TreeInfo], tags=["Tree Core"])
def get_all_forests():
    """Mengembalikan daftar 6 cabang utama beserta ID root-nya."""
    return forest_list

@app.get("/api/node/{node_id}", response_model=NodeResponse, tags=["Tree Core"])
def get_node(node_id: str):
    """Mengembalikan data spesifik untuk node yang sedang aktif."""
    node = db_nodes.get(node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"Node dengan ID '{node_id}' tidak ditemukan.")
    
    return node.to_dict()
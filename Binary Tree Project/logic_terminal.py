import os

# ==========================================
# 1. CLASS DEFINITION (OOP CORE)
# ==========================================
class Node:
    def __init__(self, id, question=None, result=None, frameworks=None):
        self.id = id
        self.question = question
        self.result = result
        self.frameworks = frameworks
        self.left = None   # Pilihan 1
        self.right = None  # Pilihan 2

    def is_leaf(self):
        return self.result is not None


# ==========================================
# 2. TREE BUILDERS (MEMBANGUN HUTAN)
# ==========================================
def build_web_tree():
    # --- STAGE 3 & LEAF ---
    # Frontend
    fe_app = Node("W_FE_APP", "Fokus pada Standard Web (1) atau Enterprise/Skala Besar (2)?")
    fe_app.left = Node("R_W1", result="JavaScript", frameworks=["Vue.js", "React"])
    fe_app.right = Node("R_W2", result="TypeScript", frameworks=["Angular", "Next.js"])
    
    fe_exp = Node("W_FE_EXP", "Fokus pada 2D Animation (1) atau 3D Simulation (2)?")
    fe_exp.left = Node("R_W3", result="JavaScript", frameworks=["GSAP", "PixiJS"])
    fe_exp.right = Node("R_W4", result="C++ (Wasm)", frameworks=["Three.js", "Emscripten"])
    
    # Backend
    be_perf = Node("W_BE_PERF", "Fokus pada High Concurrency (1) atau System Safety (2)?")
    be_perf.left = Node("R_W5", result="Go", frameworks=["Gin", "Fiber"])
    be_perf.right = Node("R_W6", result="Rust", frameworks=["Actix", "Rocket"])
    
    be_prod = Node("W_BE_PROD", "Fokus pada AI Ecosystem (1) atau Rapid Web Dev (2)?")
    be_prod.left = Node("R_W7", result="Python", frameworks=["FastAPI", "Django"])
    be_prod.right = Node("R_W8", result="PHP", frameworks=["Laravel", "Symfony"])

    # --- STAGE 2 ---
    fe = Node("W_FE", "Aplikasi Web Fungsional (1) atau Pengalaman Visual/Kreatif (2)?")
    fe.left = fe_app
    fe.right = fe_exp
    
    be = Node("W_BE", "Mengutamakan Performa Tinggi (1) atau Kecepatan Produksi (2)?")
    be.left = be_perf
    be.right = be_prod

    # --- STAGE 1 (ROOT) ---
    root = Node("WEB_ROOT", "Fokus ke Visual/Frontend (1) atau Logika/Backend (2)?")
    root.left = fe
    root.right = be
    return root

def build_mobile_tree():
    # --- STAGE 3 & LEAF ---
    multi_ui = Node("M_M_UI", "Pixel Perfect UI (1) atau Logika berbasis Web (2)?")
    multi_ui.left = Node("R_M1", result="Dart", frameworks=["Flutter"])
    multi_ui.right = Node("R_M2", result="JavaScript", frameworks=["React Native"])
    
    multi_biz = Node("M_M_BIZ", "Arsitektur Robust/Enterprise (1) atau Ekosistem C# (2)?")
    multi_biz.left = Node("R_M3", result="Java", frameworks=["Codename One"])
    multi_biz.right = Node("R_M4", result="C#", frameworks=[".NET MAUI"])
    
    nat_and = Node("M_N_AND", "Modern Development (1) atau Legacy Support XML (2)?")
    nat_and.left = Node("R_M5", result="Kotlin", frameworks=["Jetpack Compose"])
    nat_and.right = Node("R_M6", result="Java", frameworks=["Android SDK"])
    
    nat_ios = Node("M_N_IOS", "Modern Development (1) atau Legacy Support (2)?")
    nat_ios.left = Node("R_M7", result="Swift", frameworks=["SwiftUI"])
    nat_ios.right = Node("R_M8", result="Objective-C", frameworks=["UIKit"])

    # --- STAGE 2 ---
    multi = Node("M_MULTI", "Fokus pada UI Modern (1) atau Kebutuhan Bisnis (2)?")
    multi.left = multi_ui
    multi.right = multi_biz
    
    native = Node("M_NATIVE", "Target Utama Android (1) atau iOS/Apple (2)?")
    native.left = nat_and
    native.right = nat_ios

    # --- STAGE 1 (ROOT) ---
    root = Node("MOB_ROOT", "Multi-platform / 1 Codebase (1) atau Native spesifik OS (2)?")
    root.left = multi
    root.right = native
    return root

def build_data_tree():
    # --- STAGE 3 & LEAF ---
    int_mod = Node("D_I_MOD", "Deep Learning (1) atau Statistical Math (2)?")
    int_mod.left = Node("R_D1", result="Python", frameworks=["PyTorch", "TensorFlow"])
    int_mod.right = Node("R_D2", result="R", frameworks=["Tidyverse", "Shiny"])
    
    int_ana = Node("D_I_ANA", "Fast Execution (1) atau Data Visualization di Web (2)?")
    int_ana.left = Node("R_D3", result="Julia", frameworks=["Flux.jl", "DataFrames"])
    int_ana.right = Node("R_D4", result="JavaScript", frameworks=["D3.js", "Chart.js"])
    
    eng_big = Node("D_E_BIG", "Memory Processing (1) atau Stream Processing (2)?")
    eng_big.left = Node("R_D5", result="Scala", frameworks=["Apache Spark"])
    eng_big.right = Node("R_D6", result="Java", frameworks=["Apache Flink"])
    
    eng_db = Node("D_E_DB", "Relational SQL (1) atau NoSQL Scalability (2)?")
    eng_db.left = Node("R_D7", result="SQL", frameworks=["PostgreSQL", "MySQL"])
    eng_db.right = Node("R_D8", result="Java/Go", frameworks=["Cassandra", "MongoDB"])

    # --- STAGE 2 ---
    intel = Node("D_INTEL", "Fokus Pemodelan AI (1) atau Analisis Data (2)?")
    intel.left = int_mod
    intel.right = int_ana
    
    eng = Node("D_ENG", "Infrastruktur Big Data (1) atau Manajemen Database (2)?")
    eng.left = eng_big
    eng.right = eng_db

    # --- STAGE 1 (ROOT) ---
    root = Node("DAT_ROOT", "Fokus ke Kecerdasan Data/AI (1) atau Rekayasa/Infrastruktur (2)?")
    root.left = intel
    root.right = eng
    return root

def build_game_tree():
    # Agar rapi, formatnya disamakan dengan struktur di atas
    # --- ROOT ---
    root = Node("GAM_ROOT", "Menggunakan Game Engine yang sudah ada (1) atau Buat Logika Sistem sendiri (2)?")
    
    eng = Node("G_ENG", "Fokus 3D Power (1) atau 2D/Indie (2)?")
    eng.left = Node("G_E_3D", "Hardcore Control (1) atau Balanced Dev (2)?")
    eng.left.left = Node("R_G1", result="C++", frameworks=["Unreal Engine"])
    eng.left.right = Node("R_G2", result="C#", frameworks=["Unity Engine"])
    
    eng.right = Node("G_E_2D", "Scripting Focus (1) atau Browser Based (2)?")
    eng.right.left = Node("R_G3", result="C#", frameworks=["Godot", "Monogame"])
    eng.right.right = Node("R_G4", result="JavaScript", frameworks=["Phaser", "Babylon.js"])
    
    logic = Node("G_LOG", "Core Dev/Engine (1) atau AI/Scripting Gameplay (2)?")
    logic.left = Node("G_L_COR", "System Level (1) atau Modern Memory Safety (2)?")
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
    
    off = Node("S_OFF", "Fokus Eksploitasi Sistem (1) atau Web Breach/Scanning (2)?")
    off.left = Node("S_O_EXP", "System/Low-level (1) atau Network/Automation (2)?")
    off.left.left = Node("R_S1", result="C / C++", frameworks=["GDB", "Binary Ninja"])
    off.left.right = Node("R_S2", result="Python", frameworks=["Scapy", "Metasploit"])
    
    off.right = Node("S_O_WEB", "Fast Scanning (1) atau DOM Manipulation (2)?")
    off.right.left = Node("R_S3", result="Go", frameworks=["Nuclei"])
    off.right.right = Node("R_S4", result="JavaScript", frameworks=["XSS Payloads"])
    
    defen = Node("S_DEF", "Fokus Proteksi Aktif (1) atau Forensik Data (2)?")
    defen.left = Node("S_D_PRO", "Threat Detection (1) atau Firewall Logic (2)?")
    defen.left.left = Node("R_S5", result="Python", frameworks=["Log Parsers", "ML Tools"])
    defen.left.right = Node("R_S6", result="Go", frameworks=["Network Filters"])
    
    defen.right = Node("S_D_FOR", "System Analysis (1) atau Data Recovery (2)?")
    defen.right.left = Node("R_S7", result="Bash / Shell", frameworks=["Volatility"])
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

# ==========================================
# 3. TERMINAL APP RUNNER
# ==========================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Menyatukan semua pohon ke dalam sebuah kamus (Hutan)
    forest = {
        "1": {"name": "Web Development", "root": build_web_tree()},
        "2": {"name": "Mobile Development", "root": build_mobile_tree()},
        "3": {"name": "Data Science & AI", "root": build_data_tree()},
        "4": {"name": "Game Development", "root": build_game_tree()},
        "5": {"name": "Cyber Security", "root": build_security_tree()},
        "6": {"name": "IoT & Robotics", "root": build_iot_tree()},
    }

    while True:
        clear_screen()
        print("="*50)
        print(" 🌲 WELCOME TO INFORMATICS FOREST 🌲 ")
        print("="*50)
        print("Silakan pilih cabang IT yang ingin Anda jelajahi:")
        for key, value in forest.items():
            print(f"[{key}] {value['name']}")
        print("[0] Keluar Aplikasi")
        print("="*50)
        
        choice = input("Pilihan Anda (0-6): ")
        
        if choice == '0':
            print("Terima kasih telah menjelajahi Informatics Forest!")
            break
            
        if choice not in forest:
            input("Pilihan tidak valid. Tekan Enter untuk mengulangi...")
            continue
            
        # Memulai penjelajahan di pohon yang dipilih
        current_tree_name = forest[choice]['name']
        current_node = forest[choice]['root']
        
        clear_screen()
        print(f"--- Memasuki area: {current_tree_name} ---\n")
        
        # Logika Traversal (Menyusuri Cabang)
        step_count = 1
        history = []
        
        while not current_node.is_leaf():
            print(f"Tahap {step_count}: {current_node.question}")
            answer = input("Jawab [1] untuk Pilihan Pertama, [2] untuk Pilihan Kedua: ")
            
            if answer == '1':
                history.append("Pilihan 1")
                current_node = current_node.left
                step_count += 1
            elif answer == '2':
                history.append("Pilihan 2")
                current_node = current_node.right
                step_count += 1
            else:
                print("-> Input tidak valid, silakan ketik 1 atau 2.\n")
        
        # Menampilkan Hasil Akhir (Leaf Node)
        print("\n" + "="*50)
        print("🎉 HASIL REKOMENDASI UNTUK ANDA 🎉")
        print("="*50)
        print(f"Jalur yang diambil : {' -> '.join(history)}")
        print(f"Bahasa Pemrograman : ** {current_node.result} **")
        print(f"Framework Utama    : {', '.join(current_node.frameworks)}")
        print("="*50)
        
        input("\nTekan Enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()
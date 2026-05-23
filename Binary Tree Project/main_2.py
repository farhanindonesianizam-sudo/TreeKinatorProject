from fastapi import FastAPI
app = FastAPI()

#main logic
class Node:
    def __init__(self, id, question=None, result=None, frameworks=None):
        self.id = id
        self.question = question  # Pertanyaan untuk user
        self.result = result      # Nama bahasa (hanya ada di Leaf Node)
        self.frameworks = frameworks  # Daftar framework (hanya ada di Leaf Node)
        self.left = None          # Jalur "Ya"
        self.right = None         # Jalur "Tidak"

    def is_leaf(self):
        return self.result is not None
    

def build_web_tree():
    # --- LEVEL 3 (Leaf Nodes / Hasil Akhir) ---
    # Jalur Frontend
    res_js = Node("WEB_JS", result="JavaScript", frameworks=["Vue.js", "React"])
    res_ts = Node("WEB_TS", result="TypeScript", frameworks=["Angular", "Next.js"])
    res_js_anim = Node("WEB_JS_ANIM", result="JavaScript", frameworks=["GSAP", "PixiJS"])
    res_wasm = Node("WEB_WASM", result="C++ (Wasm)", frameworks=["Three.js", "Emscripten"])

    # Jalur Backend
    res_go = Node("WEB_GO", result="Go", frameworks=["Gin", "Fiber"])
    res_rust = Node("WEB_RUST", result="Rust", frameworks=["Actix", "Rocket"])
    res_py = Node("WEB_PY", result="Python", frameworks=["FastAPI", "Django"])
    res_php = Node("WEB_PHP", result="PHP", frameworks=["Laravel", "Symfony"])

    # --- LEVEL 2 (Spesialisasi) ---
    # Cabang Frontend
    node_fe_app = Node("FE_APP", question="Apakah butuh tipe data ketat untuk skala besar?")
    node_fe_app.left = res_ts  # Ya (TypeScript)
    node_fe_app.right = res_js # Tidak (JavaScript)

    node_fe_exp = Node("FE_EXP", question="Apakah butuh simulasi 3D tingkat tinggi?")
    node_fe_exp.left = res_wasm # Ya (C++/Wasm)
    node_fe_exp.right = res_js_anim # Tidak (JS Anim)

    # Cabang Backend
    node_be_perf = Node("BE_PERF", question="Apakah mementingkan penanganan user masif (Concurrency)?")
    node_be_perf.left = res_go   # Ya (Go)
    node_be_perf.right = res_rust # Tidak (Rust)

    node_be_prod = Node("BE_PROD", question="Apakah butuh ekosistem AI yang kuat?")
    node_be_prod.left = res_py   # Ya (Python)
    node_be_prod.right = res_php # Tidak (PHP)

    # --- LEVEL 1 (Core Focus) ---
    node_visual = Node("WEB_VISUAL", question="Apakah targetnya aplikasi browser standar?")
    node_visual.left = node_fe_app
    node_visual.right = node_fe_exp

    node_logic = Node("WEB_LOGIC", question="Apakah mengutamakan performa eksekusi?")
    node_logic.left = node_be_perf
    node_logic.right = node_be_prod

    # --- ROOT (Pohon Web) ---
    root_web = Node("WEB_ROOT", question="Apakah Anda ingin fokus ke Sisi Visual (Frontend)?")
    root_web.left = node_visual # Ya -> Visual
    root_web.right = node_logic # Tidak -> Logic/Backend

    return root_web


class InformaticsForest:
    def __init__(self):
        # Forest: Koleksi dari 6 pohon utama
        self.forest = {
            "web": build_web_tree(),
            # "mobile": build_mobile_tree(), # Akan ditambahkan berikutnya
            # "data": build_data_tree(),
            # ... dsb
        }
        # Flat dictionary untuk akses cepat ke semua node berdasarkan ID
        self.all_nodes = {}
        self._flatten_forest()

    def _flatten_forest(self):
        """Memasukkan semua node ke dalam dictionary agar bisa dipanggil langsung via ID"""
        for root in self.forest.values():
            stack = [root]
            while stack:
                curr = stack.pop()
                if curr:
                    self.all_nodes[curr.id] = curr
                    stack.append(curr.left)
                    stack.append(curr.right)

    def get_next_step(self, current_node_id, choice: bool):
        curr_node = self.all_nodes.get(current_node_id)
        if not curr_node or curr_node.is_leaf():
            return None
        
        return curr_node.left if choice else curr_node.right

@app.get("/")
def read_root():
    return {"Hello": "World"}

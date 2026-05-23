<template>
  <div id="app" class="app-container">
    
    <!-- ========================================== -->
    <!-- ORNAMEN BACKGROUND -->
    <!-- ========================================== -->
    <div class="ornament ornament-tl"></div>
    <div class="ornament ornament-tr"></div>
    <div class="ornament ornament-bl"></div>
    <div class="ornament ornament-br"></div>

    <!-- ========================================== -->
    <!-- 1. PAGE: START -->
    <!-- ========================================== -->
    <div v-if="currentPage === 'start'" class="page-content start-page">
      <h1 class="title">TreeKinator</h1>
      <p class="description">
        Treekinator adalah aplikasi tebak karakter yang "pintar". Dengan bantuan Binary Search Tree, aplikasi ini tidak menebak secara acak, tapi menyaring kemungkinan lewat pertanyaan sampai menemukan jawaban yang tepat.
      </p>
      <button class="btn-primary start-btn" @click="changePage('select-tree')">
        START!!!
      </button>
    </div>

    <!-- ========================================== -->
    <!-- 2. PAGE: PEMILIHAN TREE (HEXAGON MENU) -->
    <!-- ========================================== -->
    <div v-if="currentPage === 'select-tree'" class="page-content home-page">
      <button class="btn-back" @click="changePage('start')">← Kembali</button>
      <h2 class="page-title">PAGE HOME</h2>

      <div class="hexagon-wrapper" @mouseleave="hoveredTree = null">
        <!-- Teks di Tengah Hexagon -->
        <div class="center-info">
          <p class="center-text">
            {{ hoveredTree ? getTreeDesc(hoveredTree) : 'Pilihlah sesuai dengan bidang yang kalian inginkan :)' }}
          </p>
        </div>

        <!-- Render 6 Hexagon -->
        <div 
          v-for="(tree, index) in trees" 
          :key="tree.id"
          class="hexagon"
          :class="[
            `hex-pos-${index + 1}`, 
            {
              'is-hovered': hoveredTree === tree.id,
              'is-dimmed': hoveredTree && hoveredTree !== tree.id
            }
          ]"
          @mouseenter="hoveredTree = tree.id"
          @click="startTree(tree.rootId)"
        >
          <div class="hex-content">
            <div class="hex-icon" v-html="tree.icon"></div>
            <span class="hex-label">{{ tree.name }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- 3. PAGE: PEMILIHAN PILIHAN (QUESTIONS) -->
    <!-- ========================================== -->
    <div v-if="currentPage === 'questions'" class="page-content question-page">
      <!-- Tombol kembali di ujung kiri atas -->
      <button class="btn-back" @click="changePage('select-tree')">← Kembali</button>
      
      <div v-if="isLoading" class="loading">
        <h2 class="question-text">Menghubungkan ke sistem...</h2>
      </div>
      
      <div v-else-if="currentNode" class="content-box">
        <h2 class="question-text">{{ currentNode.question }}</h2>
        <div class="choices">
          <button class="btn-primary choice-btn" @click="selectAnswer(currentNode.left_id)">
            Pilihan 1
          </button>
          <button class="btn-primary choice-btn" @click="selectAnswer(currentNode.right_id)">
            Pilihan 2
          </button>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- 4. PAGE: HASIL (RESULT) -->
    <!-- ========================================== -->
    <div v-if="currentPage === 'result'" class="page-content result-page">
      <!-- Tombol kembali di ujung kiri atas -->
      <button class="btn-back" @click="changePage('select-tree')">← Kembali</button>
      
      <div v-if="currentNode" class="content-box result-box">
        <h1 class="result-title">{{ currentNode.result }}</h1>
        <p class="result-subtitle">Berdasarkan pilihanmu, ini adalah rekomendasi terbaik:</p>
        
        <div class="framework-list">
          <span v-for="fw in currentNode.frameworks" :key="fw" class="tag">
            {{ fw }}
          </span>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPage: 'start', 
      hoveredTree: null,
      currentNode: null,
      isLoading: false,
      API_BASE_URL: 'http://127.0.0.1:8000/api/node/',
      trees: [
        { id: '1', name: 'AI', rootId: 'DAT_ROOT', icon: '🧠', desc: 'Data Science, Machine Learning, dan Artificial Intelligence.' },
        { id: '2', name: 'CYBER', rootId: 'SEC_ROOT', icon: '🛡️', desc: 'Keamanan sistem, penetrasi, dan forensik digital.' },
        { id: '3', name: 'MOBILE', rootId: 'MOB_ROOT', icon: '📱', desc: 'Pembuatan aplikasi handphone Android dan iOS.' },
        { id: '4', name: 'GAME', rootId: 'GAM_ROOT', icon: '🎮', desc: 'Pembuatan game, logika mekanik, dan game engine.' },
        { id: '5', name: 'IoT', rootId: 'IOT_ROOT', icon: '⚙️', desc: 'Internet of Things, Robotika, dan Embedded Systems.' },
        { id: '6', name: 'WEB', rootId: 'WEB_ROOT', icon: '💻', desc: 'Pembuatan website, frontend, dan backend server.' }
      ]
    };
  },
  methods: {
    changePage(page) {
      this.currentPage = page;
      if (page === 'select-tree') {
        this.currentNode = null;
      }
    },
    getTreeDesc(id) {
      const tree = this.trees.find(t => t.id === id);
      return tree ? tree.desc : '';
    },
    async fetchNode(nodeId) {
      if (!nodeId) return;
      
      this.isLoading = true;
      try {
        const response = await fetch(`${this.API_BASE_URL}${nodeId}`);
        if (!response.ok) throw new Error("Gagal mengambil data");
        
        const data = await response.json();
        this.currentNode = data;
        
        if (data.is_leaf) {
          this.currentPage = 'result';
        } else {
          this.currentPage = 'questions';
        }
      } catch (error) {
        console.error("Error:", error);
        alert("Gagal terhubung ke server backend!\nPastikan server FastAPI (Python) sudah berjalan.");
      } finally {
        this.isLoading = false;
      }
    },
    startTree(rootId) {
      this.fetchNode(rootId);
    },
    selectAnswer(nextNodeId) {
      this.fetchNode(nextNodeId);
    }
  }
};
</script>

<!-- STYLE GLOBAL: Membunuh margin putih bawaan browser -->
<style>
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: #2E2E2E;
}
</style>

<!-- STYLE SCOPED: Khusus untuk komponen ini -->
<style scoped>
:root {
  --bg-color: #2E2E2E;
  --primary-orange: #FF9F43;
  --bright-yellow: #FFD166;
  --dim-gray: #6C6C6C;
  --text-white: #FFFFFF;
}

* {
  box-sizing: border-box;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.app-container {
  background-color: var(--bg-color, #2E2E2E);
  color: var(--text-white, #FFFFFF);
  min-height: 100vh;
  width: 100vw;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ==========================================
   ORNAMEN SUDUT
   ========================================== */
.ornament {
  position: absolute;
  z-index: 0;
}
.ornament-tl {
  top: -50px;
  left: -50px;
  width: 300px;
  height: 300px;
  background-color: var(--primary-orange, #FF9F43);
  border-radius: 50%;
}
.ornament-tr {
  top: 20px;
  right: -50px;
  width: 250px;
  height: 80px;
  background-color: var(--bright-yellow, #FFD166);
  border-radius: 40px;
}
.ornament-bl {
  bottom: 20px;
  left: -50px;
  width: 300px;
  height: 80px;
  background-color: var(--primary-orange, #FF9F43);
  border-radius: 40px;
}
.ornament-br {
  bottom: -100px;
  right: -100px;
  width: 350px;
  height: 350px;
  background-color: var(--bright-yellow, #FFD166);
  border-radius: 50%;
}

.page-content {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 1000px;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* ==========================================
   KOMPONEN TOMBOL
   ========================================== */
.btn-primary {
  background-color: var(--primary-orange, #FF9F43);
  color: #000;
  border: none;
  padding: 15px 40px;
  font-size: 1.2rem;
  font-weight: bold;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.btn-primary:hover {
  background-color: var(--bright-yellow, #FFD166);
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(255, 209, 102, 0.6);
}
.btn-back {
  position: absolute;
  top: 30px;
  left: 30px;
  background-color: var(--bg-color, #2E2E2E); /* Latar gelap agar kontras dengan ornamen */
  color: var(--bright-yellow, #FFD166); /* Teks kuning cerah */
  border: 2px solid var(--bright-yellow, #FFD166);
  padding: 10px 25px;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease;
  z-index: 50; /* Selalu berada di paling atas */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4); /* Efek bayangan agar menonjol */
}

.btn-back:hover {
  background-color: var(--bright-yellow, #FFD166);
  color: #000;
  transform: scale(1.05);
}

/* ==========================================
   KOTAK KONTEN (SESUAI GAMBAR REFERENSI)
   ========================================== */
.content-box {
  width: 100%;
  max-width: 800px;
  padding: 80px 40px;
  border: 2px solid var(--bright-yellow, #FFD166);
  border-radius: 20px;
  background-color: transparent;
  text-align: center;
  margin-top: 20px;
}

/* ==========================================
   PAGE 1: START
   ========================================== */
.start-page { text-align: center; }
.title {
  font-size: 4rem;
  color: var(--bright-yellow, #FFD166);
  margin-bottom: 20px;
}
.description {
  font-size: 1.2rem;
  line-height: 1.6;
  max-width: 600px;
  margin-bottom: 40px;
}

/* ==========================================
   PAGE 2: HEXAGON MENU
   ========================================== */
.home-page .page-title {
  align-self: flex-start;
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.hexagon-wrapper {
  position: relative;
  width: 500px;
  height: 500px;
  margin: 0 auto;
}

.center-info {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 140px;
  text-align: center;
  z-index: 5;
  pointer-events: none; 
}
.center-text {
  font-weight: bold;
  font-size: 1.1rem;
  color: var(--text-white, #FFFFFF);
}

.hexagon {
  position: absolute;
  top: 50%; 
  left: 50%;
  width: 160px;
  height: 140px;
  background-color: var(--primary-orange, #FF9F43);
  clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.3s ease-in-out;
}

.hex-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  color: #000;
}
.hex-icon {
  font-size: 2.5rem;
  margin-bottom: 5px;
}
.hex-label {
  font-weight: bold;
  font-size: 1rem;
}

.hex-pos-1 { transform: translate(-50%, calc(-50% - 145px)); }
.hex-pos-2 { transform: translate(calc(-50% + 125px), calc(-50% - 72px)); }
.hex-pos-3 { transform: translate(calc(-50% + 125px), calc(-50% + 72px)); }
.hex-pos-4 { transform: translate(-50%, calc(-50% + 145px)); }
.hex-pos-5 { transform: translate(calc(-50% - 125px), calc(-50% + 72px)); }
.hex-pos-6 { transform: translate(calc(-50% - 125px), calc(-50% - 72px)); }

.hexagon.is-hovered {
  background-color: var(--bright-yellow, #FFD166);
  z-index: 20;
}
.hex-pos-1.is-hovered { transform: translate(-50%, calc(-50% - 145px)) scale(1.1); }
.hex-pos-2.is-hovered { transform: translate(calc(-50% + 125px), calc(-50% - 72px)) scale(1.1); }
.hex-pos-3.is-hovered { transform: translate(calc(-50% + 125px), calc(-50% + 72px)) scale(1.1); }
.hex-pos-4.is-hovered { transform: translate(-50%, calc(-50% + 145px)) scale(1.1); }
.hex-pos-5.is-hovered { transform: translate(calc(-50% - 125px), calc(-50% + 72px)) scale(1.1); }
.hex-pos-6.is-hovered { transform: translate(calc(-50% - 125px), calc(-50% - 72px)) scale(1.1); }

.hexagon.is-dimmed {
  background-color: var(--dim-gray, #6C6C6C);
  opacity: 0.5;
}

/* ==========================================
   PAGE 3: QUESTIONS
   ========================================== */
.question-text {
  font-size: 2.2rem;
  margin-bottom: 50px;
  color: var(--bright-yellow, #FFD166);
  font-weight: 600;
}
.choices {
  display: flex;
  gap: 30px;
  justify-content: center;
}

/* ==========================================
   PAGE 4: RESULT
   ========================================== */
.result-title {
  font-size: 5rem;
  color: var(--bright-yellow, #FFD166);
  margin-bottom: 20px;
  font-weight: 800;
  letter-spacing: 2px;
}
.result-subtitle {
  font-size: 1.2rem;
  margin-bottom: 40px;
}
.framework-list {
  display: flex;
  gap: 20px;
  justify-content: center;
}
.tag {
  background-color: var(--primary-orange, #FF9F43);
  color: #000;
  padding: 15px 30px;
  border-radius: 12px;
  font-weight: bold;
  font-size: 1.3rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
</style>
// point d'entrée de l'application
const app = document.getElementById("app");

// fonction principale
function init() {
  renderHome();
}

// écran d'accueil
function renderHome() {
  app.innerHTML = `
    <h2>Bienvenue</h2>
    <p>Choisis un mode :</p>

    <button onclick="startLearning()">Apprendre</button>
    <button onclick="startQuiz()">Quiz</button>
  `;
}

// mode apprentissage (vide pour l'instant)
function startLearning() {
  app.innerHTML = `
    <h2>Mode apprentissage</h2>
    <p>À venir...</p>
    <button onclick="renderHome()">Retour</button>
  `;
}

// mode quiz (vide pour l'instant)
function startQuiz() {
  app.innerHTML = `
    <h2>Quiz</h2>
    <button onclick="startA1Quiz()">A1</button>
    <button onclick="startA2Quiz()">A2</button>
    <button onclick="renderHome()">B1</button>
    <button onclick="renderHome()">B2</button>
    <button onclick="renderHome()">Retour</button>
  `;
}

function startA1Quiz() {
  app.innerHTML = `
    <h2>Quiz A1</h2>
    <p>À venir...</p>
    <button onclick="startQuiz()">Retour</button>
  `;
}

function startA2Quiz() {
  app.innerHTML = `
    <h2>Quiz A2</h2>
    <p>À venir...</p>
    <button onclick="startQuiz()">Retour</button>
  `;
}

function startB1Quiz() {
  app.innerHTML = `
    <h2>Quiz B1</h2>
    <p>À venir...</p>
    <button onclick="startQuiz()">Retour</button>
  `;
}

function startB2Quiz() {
  app.innerHTML = `
    <h2>Quiz B2</h2>
    <p>À venir...</p>
    <button onclick="startQuiz()">Retour</button>
  `;
}
// lancer l'app
init();
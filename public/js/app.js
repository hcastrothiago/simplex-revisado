const fo = document.getElementById("funcaoObjetivo")
const LaTexFO = document.getElementById("LaTexFO")
const restricoes = document.getElementById("restricoes")
const LaTexRestricoes = document.getElementById("LaTexRestricoes")

const run = (inputArea, LaTexOutput) => {
    // Obter o conteúdo digitado e dividir por linhas
    const lines = inputArea.value.split("\n");

    // Limpar o conteúdo anterior
    LaTexOutput.innerHTML = "";

    // Processar cada linha individualmente
    lines.forEach(line => {
        if (line.trim() !== "") {
            const div = document.createElement("div");
            div.className = "latex-line";
            div.innerHTML = `$$${line}$$`;
            LaTexOutput.appendChild(div);
        }
    });    

    // Re-renderizar usando MathJax
    MathJax.typesetPromise([LaTexOutput]).catch((err) => console.error(err));
}

fo.addEventListener("input", () => run(fo, LaTexFO));
// fo.addEventListener("DOMContentLoaded", run(fo, LaTexFO));
//estou com problemas no latex-line, ela não está quebrando linhas
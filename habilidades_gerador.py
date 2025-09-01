# Lista de habilidades com ícones do Font Awesome (substitua pelos seus)
habilidades = [
    {"nome": "Python", "icone": "fa-python"},
    {"nome": "JavaScript", "icone": "fa-js"},
    {"nome": "React", "icone": "fa-react"},
    {"nome": "Git", "icone": "fa-git-alt"},
    # Adicione mais aqui
]

# Gera o HTML
html = """
<h3>Minhas Habilidades</h3>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  .skills-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  .skill-item {
    text-align: center;
    transition: transform 0.3s ease;
  }
  .skill-item:hover {
    transform: scale(1.2) rotate(10deg); /* Animação: cresce e gira ao hover */
  }
  .skill-icon {
    font-size: 40px;
    color: #007bff; /* Cor personalizável */
  }
</style>
<div class="skills-container">
"""

for hab in habilidades:
    html += f"""
  <div class="skill-item">
    <i class="fab {hab['icone']} skill-icon"></i>
    <p>{hab['nome']}</p>
  </div>
"""

html += "</div>"

# Salva o HTML gerado em um arquivo ou imprime
print(html)  # Copie isso para o README
# Ou salve: with open('habilidades.html', 'w') as f: f.write(html)

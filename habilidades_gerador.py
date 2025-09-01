habilidades = [
    {"nome": "HTML", "icone": "https://media.giphy.com/media/XAxylRMCdpbEWUAvr8/giphy.gif"},
    {"nome": "Python", "icone": "https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif"},
    {"nome": "JavaScript", "icone": "https://media.giphy.com/media/ln7z2eWriiQAllfVcn/giphy.gif"},
]
# O resto do script permanece igual, mas remova o CSS de :hover
html = """
### Minhas Habilidades
<div style="display: flex; gap: 15px; flex-wrap: wrap;">
"""
for hab in habilidades:
    html += f"""
    <div style="text-align: center;">
      <img alt="{hab['nome']}" height="40" width="50" src="{hab['icone']}">
      <p>{hab['nome']}</p>
    </div>
    """
html += "</div>"
print(html)
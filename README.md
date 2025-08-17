# 🎬 Controle Remoto PowerPoint

Um **controle remoto de slides via celular**, feito em Python, que permite **avançar, voltar, iniciar e sair da apresentação** do PowerPoint diretamente pelo navegador do seu celular, usando **QR Code** e **PyAutoGUI**. Ideal para apresentações, palestras, aulas e cultos.

---

## ⚡ Funcionalidades

- ▶️ **Iniciar apresentação** (F5)  
- ⬅️ **Voltar slide**  
- ➡️ **Avançar slide**  
- ⏹️ **Sair da apresentação** (ESC)  


---

## 🛠 Tecnologias usadas

- Python 3  
- PyAutoGUI (controle de teclado e mouse)  
- QRCode (gera QR Code no terminal)  
- HTTP Server integrado (SimpleHTTPServer / socketserver)  

---

## 💻 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/controle-ppt-remoto.git
cd controle-ppt-remoto
```
2. Instale as dependências:
```bash
pip install pyautogui qrcode[pil]
```
3. Execute o script:
```bash
python controle_ppt.py
```
## 📱 Como usar

1. Abra o terminal e rode o script.  
2. Escaneie o **QR Code que aparece no terminal** com o seu celular.  
3. A página abrirá no navegador do celular com os seguintes botões:

| Botão       | Função                        |
|-------------|-------------------------------|
| ▶️ Iniciar  | Inicia a apresentação (F5)    |
| ⬅️ Anterior | Volta um slide                |
| ➡️ Próximo  | Avança um slide               |
| ⏹️ Sair     | Sai da apresentação (ESC)     |

4. Abra a apresentação no PowerPoint e use os botões do celular para controlar os slides.


## ⚠️ Observações

- PC e celular devem estar na mesma rede Wi-Fi

- PowerPoint precisa estar em foco para que as teclas funcionem

- Funciona em Windows e Mac (Python instalado)

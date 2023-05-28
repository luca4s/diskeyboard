# diskeyboard
permite que mensagens do discord em um canal de texto controlem o seu teclado
# requisitos
- python 3
- discord.py, pyautogui e asyncio (`pip install -r requirements.txt`)
# como configurar (`config.json`)
- `token`: a token do seu bot do discord
- `channelid`: o canal de texto onde as teclas serão enviadas e recebidas
- `holdtime`: a quantidade em segundos em que as teclas serão pressionadas
- `write`: define se os usuários podem enviar uma palavra para ser digitada (não pode ser parte da `keylist`)
- `combos`: um objeto que define todos os combos de teclas especiais permitidas
- `keylist`: uma lista com todas as teclas permitidas (você pode ver as teclas aqui: https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)
# como usar
simplismente mande mensagens com as teclas que você quer pressionar no canal onde as teclas são executadas
- se for um combo de teclas, escreva ela assim: `alt f4`, `ctrl shift right`

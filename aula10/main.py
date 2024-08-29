import pyautogui
import time

def preencher(atleta, modalidade, medalha, comite):

    campoAtleta = pyautogui.locateCenterOnScreen(
        "atleta1.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoAtleta, duration = 0.7)
    pyautogui.write(atleta)


    campoModalidade = pyautogui.locateCenterOnScreen(
        "Modalidade.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoModalidade, duration = 0.7)
    pyautogui.write(modalidade)


    campoMedalha = pyautogui.locateCenterOnScreen(
        "Medalha.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoMedalha, duration = 0.7)
    pyautogui.write(medalha)


    campoComite = pyautogui.locateCenterOnScreen(
        "Comite.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoComite, duration = 0.7)
    pyautogui.write(comite)

    campoEnviar = pyautogui.locateCenterOnScreen(
        "enviar.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoEnviar, duration = 0.7)
    time.sleep(2)

    campoEnviar = pyautogui.locateCenterOnScreen(
        "outraEnviar.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoEnviar, duration = 0.7)

    #rolar tela: 
    #import time
    #pyautogui.scroll(y=300)
    #time.slepp(2)

    time.sleep(1)
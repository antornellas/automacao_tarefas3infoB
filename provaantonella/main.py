import pyautogui
import time


def preencher(aluno, atividade, nota):

    campoAluno = pyautogui.locateCenterOnScreen(
        "aluno.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoAluno, duration = 0.7)
    pyautogui.write(aluno)


    campoAtividade = pyautogui.locateCenterOnScreen(
        "atividade.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoAtividade, duration = 0.7)
    pyautogui.write(atividade)


    campoNota = pyautogui.locateCenterOnScreen(
        "nota.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoNota, duration = 0.7)
    pyautogui.write(nota)


    campoTurma = pyautogui.locateCenterOnScreen(
        "turma.png",
        grayscale=True,
        confidence=0.8
        )
    pyautogui.click(campoTurma, duration = 0.7)
    time.sleep(2)

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

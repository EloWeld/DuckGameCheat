from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

# Создаем контроллер, который позволяет симулировать нажатия клавиш
kbd_controller = Controller()
timer = time.time()
gl = dict(working=True)
# Определяем функцию, которая будет выполняться при нажатии клавиши
def on_press(key: keyboard.KeyCode):
    global gl
    print(key)
    # Если нажата цифра '6' на нумпаде
    if key == keyboard.Key.caps_lock and gl['working']:
        # Имитируем нажатия трех различных клавиш (здесь: a, b, c)
        kbd_controller.press(keyboard.Key.left)
        time.sleep(0.02)
        kbd_controller.release(keyboard.Key.left)
        time.sleep(0.01)
        kbd_controller.press('x')
        time.sleep(0.04)
        kbd_controller.release('x')
        #RELOAD
        time.sleep(0.03)
        kbd_controller.press('x')
        time.sleep(0.05)
        kbd_controller.release('x')
    if hasattr(key, 'vk') and  key.vk == 83 and gl['working']:
        # Имитируем нажатия трех различных клавиш (здесь: a, b, c)
        kbd_controller.press(keyboard.Key.right)
        time.sleep(0.02)
        kbd_controller.release(keyboard.Key.right)
        time.sleep(0.01)
        kbd_controller.press('x')
        time.sleep(0.04)
        kbd_controller.release('x')
        #RELOAD
        time.sleep(0.03)
        kbd_controller.press('x')
        time.sleep(0.05)
        kbd_controller.release('x')
    if hasattr(key, 'vk') and  key.char == 'd' and gl['working']:
        # Имитируем нажатия трех различных клавиш (здесь: a, b, c)
        kbd_controller.press('z')
        time.sleep(0.03)
        kbd_controller.release('z')
        time.sleep(0.03)
        kbd_controller.press('z')
        time.sleep(0.035)
        kbd_controller.press('x')
        time.sleep(0.04)
        kbd_controller.release('z')
        kbd_controller.release('x')
        #RELOAD
        time.sleep(0.03)
        kbd_controller.press('x')
        time.sleep(0.05)
        kbd_controller.release('x')
        
    if hasattr(key, 'vk') and  key.char == 'f' and gl['working']:
        # Имитируем нажатия трех различных клавиш (здесь: a, b, c)
        kbd_controller.press(keyboard.Key.shift_l)
        time.sleep(0.01)
        kbd_controller.press('z')
        time.sleep(0.01)
        kbd_controller.press('x')
        time.sleep(0.01)
        kbd_controller.release('z')
        time.sleep(0.01)
        kbd_controller.release('x')
        time.sleep(0.01)
        kbd_controller.release(keyboard.Key.shift_l)
        
    if hasattr(key, 'vk') and  key.vk == 96: # 0 numpad
        # Имитируем нажатия трех различных клавиш (здесь: a, b, c)
        gl['working'] = not gl['working'] 
        
def on_release(key):
    global timer
    print(time.time() - timer, key)
    timer = time.time()
    if key == Key.shift_r:
        # Останавливаем слушатель
        return False

# Создаем слушателя нажатий клавиш
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Запускаем слушателя
listener.start()

# Блокируем основной поток
listener.join()
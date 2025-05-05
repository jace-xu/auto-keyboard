import keyboard
import time

def type_text(text):
    for char in text:
        keyboard.write(char)  # 模拟键盘输入字符
        time.sleep(0.05)  # 模拟打字间隔，0.1秒可以调整为更快或更慢

def main():
    print("请输入要模拟打字的内容：")
    text = input()  # 获取用户输入的文本
    print("按下 F2 键开始模拟打字...")
    keyboard.wait('f2')  # 等待按下 F2 键
    print("开始打字...")
    type_text(text)
    print("\n打字完成！")

if __name__ == "__main__":
    main()
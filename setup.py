import subprocess
import sys
def install(pakage):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',pakage])

install("pyautogui")
install("tk")
print('''𝑬𝒏𝒕𝒆𝒓 𝒚𝒐𝒖 𝒑𝒂𝒕𝒉 𝒐𝒇 𝒘𝒉𝒂𝒕𝒔𝒂𝒑𝒑 𝒇𝒐𝒓 𝒆𝒙𝒂𝒎𝒑𝒍𝒆
𝒊𝒇 𝒚𝒐𝒖 𝒘𝒉𝒂𝒕𝒔𝒂𝒑𝒑 𝒊𝒔 𝒂𝒕 𝒚𝒐𝒖 𝒅𝒆𝒔𝒌𝒕𝒐𝒑 𝒔𝒐 𝒚𝒐𝒖 𝒘𝒓𝒊𝒕𝒆 𝒍𝒊𝒌𝒆 𝒕𝒉𝒊𝒔
𝑪:\\𝑼𝒔𝒆𝒓𝒔\\𝑫𝒆𝒔𝒌𝒕𝒐𝒑\\𝑾𝒉𝒂𝒕𝒔𝑨𝒑𝒑.𝒍𝒏𝒌 ''')

a = input("𝑬𝒏𝒕𝒆𝒓 𝒚𝒐𝒖𝒓 𝒑𝒂𝒕𝒉:")
print("𝑫𝒐𝒏𝒕 𝒑𝒖𝒕 𝒔𝒆𝒄 𝒂𝒇𝒕𝒆𝒓 𝒔𝒆𝒄 𝒋𝒖𝒔𝒕 𝒏𝒖𝒎𝒃𝒆𝒓 𝒍𝒊𝒌𝒆 𝟏𝟎 𝒇𝒐𝒓 𝟏𝟎𝒔𝒆𝒄 𝒂𝒏𝒅 𝒔𝒐..𝒐𝒏")
b = input("𝑬𝒏𝒕𝒆𝒓 𝒕𝒉𝒂𝒕 𝒉𝒐𝒘 𝒎𝒖𝒄𝒉 𝒕𝒊𝒎𝒆 𝒚𝒐𝒖 𝒘𝒉𝒂𝒕𝒔𝒂𝒑𝒑 𝒕𝒂𝒌𝒆 𝒕𝒐 𝒃𝒐𝒐𝒕 𝒊𝒏 𝒔𝒆𝒄:")
with open("data/path.txt","w") as file:
    file.write(a)
    file.write("\n")
    file.write(b)
    


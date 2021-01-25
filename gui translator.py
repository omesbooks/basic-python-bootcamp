#GUITranslator.py
from tkinter import *
#จากไลบรารีชื่อ tkinter * คือให้ดึงความสามารถหลักมาทั้งหมดเฉพาะจากไฟล์ _init_
from tkinter import ttk # ttk is theme of tk อันนี้เป็นการ import ไฟล์ย่อยมาใช้งานอีกที
from googletrans import Translator
translator = Translator() #สร้างฟังก์ชันแปลภาษา
       

GUI = Tk()   #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #กำหนดขนาดหน้าต่าง กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by GS.OHM') #กำหนดชื่อหน้าต่าง
#--------Config--------
FONT = ('Angsana New',15)
#--------Label--------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()
#--------entry (ช่องกรอกข้อความ)--------
v_vocab = StringVar() #กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font = FONT)  #สร้าง Edit Field
E1.pack(pady = 20)
#--------button ปุ่ม--------
def Translate():
       vocab = v_vocab.get() #.get คือให้แสดงผลออกมา
       meaning = translator.translate(vocab,dest = 'th')
    #   print(  vocab+ ':'+meaning.text)
     #  print(meaning.pronunciation)
       v_result.set(vocab+ ' : '+meaning.text) #สั่งเก็บในตัวแปล v_result เพื่อที่ Label R1 จะเอาไปแสดงผลต่อ
'''
B1 = Button(GUI,text = 'Translate') # สร้างปุ่ม
B1.pack() #show ปุ่มขึ้นมาวางจากบนลงล่าง
'''       
B1 = ttk.Button(GUI,text = 'Translate',command = Translate) # สร้างปุ่มด้วย ttk
B1.pack(ipadx=20,ipady=10) #show ปุ่มขึ้นมาวางจากบนลงล่าง ส่วนในวงเล็บคือการปรับขนาดปุ่ม
#--------Label--------
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()
#--------Result--------
v_result = StringVar()      #นี่คือกล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground = 'green')
R1.pack()




GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด (ให้เอาไว้บรรทัดสุดท้ายเท่านั้น)

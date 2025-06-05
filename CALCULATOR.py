print("murali")

for i in range(5):
    if i==2:
        break
    print(i)


for i in range(10):
    if i%2==0:
        continue
    print(i)



for i in range(20):
    if i%3==0:
        continue
    print(i)


a=[1,0,4,'bob']
print(a)
a.reverse()
print(a)


c=[10,20,30,40,50]
print(c[0:3])
print(c[3:4])
print(c[::-4])
print(c[::-1])
c.remove(20)
print(c)






import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result.set(eval(entry.get()))
        except Exception:
            result.set("Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
        result.set("")
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 18))
result_label.grid(row=1, column=0, columnspan=4)

# Buttons
buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

for i, button_text in enumerate(buttons):
    btn = tk.Button(root, text=button_text, font=("Arial", 18), width=5, command=lambda bt=button_text: on_click(bt))
    btn.grid(row=(i // 4) + 2, column=i % 4)

# Run the application
root.mainloop()
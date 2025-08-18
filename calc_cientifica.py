import tkinter as tk
import math


def click_boton(caracter):
    current_text = display.get()

    if caracter == '=':
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))

        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'x!':
        try:
            result = eval(current_text)
            total = math.factorial(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'sin':
        try:
            result = eval(current_text)
            total = math.sin(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'ln':
        try:
            result = eval(current_text)
            total = math.log(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'π':
        try:
            total = math.pi
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    
    elif caracter == 'cos':
        try:
            result = eval(current_text)
            total = math.cos(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'log':
        try:
            result = eval(current_text)
            total = math.log10(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'e':
        try:
            total = math.e
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'tan':
        try:
            result = eval(current_text)
            total = math.tan(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == '√':
        try:
            result = eval(current_text)
            total = math.sqrt(result)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'x²':
        try:
            result = eval(current_text)
            total = math.pow(result, 2)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'x³':
        try:
            result = eval(current_text)
            total = math.pow(result, 3)
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error") 

    elif caracter == '%':
        try:
            result = eval(current_text)
            total = result / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(total))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, caracter)



root = tk.Tk()
root.title("Calculadora Cientifica")
root.geometry("500x400")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)


display = tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
display.grid(row=0, column=0, columnspan=7, sticky=tk.NSEW, padx=5, pady=5)

botones = ['x!','sin','ln','7','8','9','/',
           'π','cos','log','4','5','6','*',
           'e','tan','√','1','2','3','-',
           'x²','(',')','0','.','=','+',
           'x³','%','C',]

row_num = 1
col_num = 0

for boton_texto in botones:
    if boton_texto == '=':
        button = tk.Button(root, text= boton_texto, font=("Arial", 16),command= lambda b= boton_texto: click_boton(b))

    elif boton_texto == 'C':
        button = tk.Button(root, text= boton_texto, font=("Arial", 16),command= lambda b= boton_texto: click_boton(b))

    elif boton_texto == '%':
        button = tk.Button(root, text= boton_texto, font=("Arial", 16),command= lambda b= boton_texto: click_boton(b))

    elif boton_texto == 'cos':
        button = tk.Button(root, text= boton_texto, font=("Arial", 16),command= lambda b= boton_texto: click_boton(b))

    else:
        button = tk.Button(root, text= boton_texto, font=("Arial", 16),command= lambda b= boton_texto: click_boton(b))

    button.grid(row= row_num, column= col_num, sticky=tk.NSEW, padx=5, pady=5)


    

    col_num += 1
    if col_num > 6 :
        col_num = 0
        row_num += 1




root.mainloop()
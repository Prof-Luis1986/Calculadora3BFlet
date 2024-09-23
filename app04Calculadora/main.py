import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_multiplicacion(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_division(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
    except ZeroDivisionError:
        lblResultado.value="Error división por cero" 


def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="Ingresa el primer número",color="yellow")
    txtNum2=ft.TextField(label="Ingresa el segundo número",color="yellow")
    lblResultado=ft.Text("Resultado: ",color="yellow")
    
    def on_calc_suma(e):
        calc_suma(txtNum1,txtNum2,lblResultado)
        page.update()
        
    def on_calc_resta(e):
        calc_resta(txtNum1,txtNum2,lblResultado)
        page.update()
        
    def on_calc_multiplicacion(e):
        calc_multiplicacion(txtNum1,txtNum2,lblResultado)
        page.update()
        
    def on_calc_division(e):
        calc_division(txtNum1,txtNum2,lblResultado)
        page.update()
        
    def limpiar(e):
        txtNum1.value=""
        txtNum2.value=""
        lblResultado.value="Resultado: "
        page.update()
        
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_click=on_calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=on_calc_division)
    btnLimpiar=ft.ElevatedButton(text="Limpiar",on_click=limpiar)
        
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],alignment="center"),
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMultiplicacion,
            btnDivision,
            btnLimpiar
        ],alignment="center")
    )
    


ft.app(main)

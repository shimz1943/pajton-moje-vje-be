import PySimpleGUI as grafika

unos_sirine_dasaka = grafika.Input(key="id_inputa")


layout = [
    [grafika.Text("Širina dasaka: "), unos_sirine_dasaka],
    [grafika.OK(key="ok_botun"), grafika.Exit()]
]

prozor = grafika.Window("Kubiciranje", layout)

while True:
    klikovi, vrijednosti = prozor.read()
    duzina_daske_u_metrima = 4
    debljina_daske = 0.024

    if klikovi == grafika.WIN_CLOSED or klikovi == "Exit":
        break

    elif klikovi == "ok_botun":
        vrijednost_varijable = vrijednosti["id_inputa"]

        try:
            pretvarac_u_broj = float(vrijednost_varijable)

            ukupna_kubikaza = pretvarac_u_broj * duzina_daske_u_metrima * debljina_daske
            print("Kubikaža je: ", ukupna_kubikaza, "m3. Jeben ti boga")

        except ValueError:
            print("odjebi sa stringovima")

prozor.close()

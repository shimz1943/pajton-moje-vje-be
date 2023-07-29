import PySimpleGUI as grafika

unos_sirine_dasaka = grafika.Input(key="id_inputa")


layout = [
    [grafika.Text("Širina dasaka: "), unos_sirine_dasaka],
    [grafika.OK(key="ok_botun"), grafika.Exit()],
    [grafika.Text("", key="prikaz_rezultata")]
]

prozor = grafika.Window("Kubiciranje for dummies", layout)

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

            ukupna_kubikaza = round(
                pretvarac_u_broj * duzina_daske_u_metrima * debljina_daske, 4)
            prozor["prikaz_rezultata"].update(ukupna_kubikaza)

        except ValueError:
            print("Ne prihvaćam string brate...")

prozor.close()

from ia_client import generar_backlog_json
from backlog import parsear_backlog
from export_excel import exportar_excel

def main():
    print("Describe el proyecto:\n")
    texto = input("> ")
    print("Escribeme el número de sprint del proyecto\n")

    sprint_num = input("> ")
    
    archivo = f"sprint_{sprint_num}.xlsx"

    backlog_json = generar_backlog_json(texto)
    work_items = parsear_backlog(backlog_json, f"Sprint {sprint_num}")

    exportar_excel(work_items, archivo, f"Sprint {sprint_num}")

    print(f"Sprint {sprint_num} generado correctamente.")
    print(f"Archivo creado: {archivo}")

if __name__ == "__main__":
    main()
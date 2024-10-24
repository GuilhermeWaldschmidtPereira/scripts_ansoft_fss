def soma(x,y,output_file_path):
    num_linhas = len(x)
    line_points = []

    # Lê o arquivo
    line_data = """
    ' ----------------------------------------------
    ' Script Recorded by Ansoft Designer Version 3.5.0
    ' 12:58 AM  Sep 27, 2024
    ' ----------------------------------------------
    Dim oAnsoftApp
    Dim oDesktop
    Dim oProject
    Dim oDesign
    Dim oEditor
    Dim oModule
    Set oAnsoftApp = CreateObject("AnsoftDesigner.DesignerScript")
    Set oDesktop = oAnsoftApp.GetAppDesktop()
    oDesktop.RestoreWindow
    Set oProject = oDesktop.SetActiveProject("{}")
    Set oDesign = oProject.SetActiveDesign("PlanarEM1")
    Set oEditor = oDesign.SetActiveEditor("Layout")


    oEditor.CreatePolygon Array("NAME:Contents", "polyGeometry:=", Array("Name:=",  _\n  "poly_14", "LayerName:=", "Trace", "lw:=", "0mm", "n:=", {}, "U:=", "mm", """.format(output_file_path, num_linhas)

    # Grava as coordenadas x e y do arquivo no padrão aceito pelo script
    for col1, col2 in zip(x,y):
        line_points.append(f'"x:=", {float(col1)*10}, "y:=", {float(col2)*10}')

    line_data += ', '.join(line_points) + "))"

    # Escreve o arquivo de saída no formato .vbs
    with open(f"{output_file_path}.vbs", 'w') as output_file:
        output_file.write(line_data)
        output_file.write('\n oProject.Save')
        
    # Para novas implementações, descomentar as linhas abaixo, ela vai abrir o Ansoft Designer e salvar cada uma das espirais
        
    # Executa o arquivo .adsn gerado
    # os.system(f'cmd /c "start {output_file_path_adsn}"')
    # time.sleep(2)
    # # Roda o arquivo .vbs
    # os.system(f'cmd /c "start {output_file_path}"')
    # time.sleep(2)
    # # Salva o arquivo .adsn
    # pyautogui.hotkey('ctrl', 's')
    # time.sleep(2)
    # # Fecha o arquivo .adsn
    # pyautogui.hotkey('alt', 'f4')
        
def build_file(x,y,output_file_path):
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
    Set oProject = oDesktop.SetActiveProject("espirais")
    Set oDesign = oProject.SetActiveDesign("PlanarEM1")
    Set oEditor = oDesign.SetActiveEditor("Layout")


    oEditor.CreateLine Array("NAME:Contents", "lineGeometry:=", Array("Name:=",  _
    "line_697", "LayerName:=", "Trace", "lw:=", "2mil", "endstyle:=", 0, "joinstyle:=",  _
    0, "n:=", {}, "U:=", "mm", """.format(num_linhas)

    # Grava as coordenadas x e y do arquivo no padrão aceito pelo script
    for col1, col2 in zip(x,y):
        line_points.append(f'"x:=", {float(col1)/2}, "y:=", {float(col2)/2}')

    line_data += ', '.join(line_points) + "))"

    # Escreve o arquivo de saída no formato .vbs
    with open(f"{output_file_path}.vbs", 'w') as output_file:
        output_file.write(line_data)
        output_file.write('\n oProject.Save')
        
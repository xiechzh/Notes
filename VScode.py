# This file is a note for visual studio code using, include issue and resolve

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#**************************************************************************************************************
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW


#***********************  PYTHON  ******************************
#****************************************************************

#issue can not import module from other file
# WHY THIS ISSURE：VScode会自动将根目录下的文件加入pythonpath路径，但不会将子目录加入到pythonpath中。所以根目录下再建目录的pyghon模块无法被解析
1.create {} launch.json file:
    {
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {"PYTHONPATH": "${workspaceRoot}"},
            "envFile": "${workspaceFolder}/.env"
        }
    ]
    }
2. mk file .env under root file:
    PYTHONPATH=./data/filter
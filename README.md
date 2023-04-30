# autolasercut

<p>Automatic Laser Cutter Interface</p>
<p>SEIS 739</p>
<p>Project members: Sasha Schrandt</p>

This application website allows users to create simple laser cutting toolpaths for things like box creation, gear generating, and image tracing. It is designed to output color coded svg files that should be ready to upload directly to your laser cutter. Additionally, it uses a database to keep track of previously created toolpaths so that you can cut them again on-demand.

run the following in the terminal to start the server:
    python manage.py runserver 8000

navigate a web browser to:
    localhost:8000


to generate a class diagram in the terminal:
    python manage.py graph_models -a -g --dot -o classDiagram.dot
    dot -Tpng classDiagram.dot -o classDiagram.png

    

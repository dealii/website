# Installation instructions for mkdocs

    pip install mkdocs
    pip install mkdocs-material
    pip install markdown-include

Alternatively you can use conda to install all packages into a new environment named `dealii-website` like this:

    conda env create -f environment.yml

Then the server can be run locally as

    mkdocs serve

and you should see something like

    INFO    -  Documentation built in 0.15 seconds
    INFO    -  [08:40:55] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO    -  [08:40:55] Serving on <http://127.0.0.1:8000/>
    WARNING -  [08:40:57] "GET /pictures/clover57.png HTTP/1.1" code 404
    WARNING -  [08:40:57] "GET /pictures/github-logo.gif HTTP/1.1" code 404
    WARNING -  [08:40:57] "GET /pictures/valid-html401.png HTTP/1.1" code 404
    INFO    -  [08:40:57] Browser connected: <http://127.0.0.1:8000/>

If you want to add to the timeline, access this google document, and ask for access write permission:
<https://docs.google.com/spreadsheets/d/1FYT2_aIxZT4VFJeJDrqAu5out9HwCDwsxWU299e5hlk/edit?gid=0#gid=0>

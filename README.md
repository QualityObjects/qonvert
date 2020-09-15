QOnvert
=======

Small REST API to reduce image files sizes, specially oriented to scanned document, so the resulting image is still readable, but quite smaller in size.

Building
==========

    python3 setup.py bdist_wheel

How to launch it (dev mode)
===================

    # Installing third-party deps
    python3 -m pip install -t lib/ -r requirements.txt 
    python3 -m pip install -t lib/ -r requirements.dev.txt 
    PYTHONPATH=src:lib python3 script/qonvert-server



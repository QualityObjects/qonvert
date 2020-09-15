rem prepare tgz
rem tar -cvz -f qonvert-src.tgz --exclude="*/build" --exclude="*/lib" --exclude="*/dist" --exclude="*/.git" convert/

docker build --tag=qualityobjects/qonvert-server:latest .
rem docker run --rm -it -p8080:8080 qonvert-server

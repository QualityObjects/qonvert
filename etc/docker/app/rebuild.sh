# To build the package:
# $ python3 setup.py bdist_wheel


export PKG_PATH=$(find ../../../dist/ -name "*.whl" | sort -r | head -1)
cp "$PKG_PATH" .
export PKG_PATH=$(ls -1 *.whl)
#The pkg file is something like: qonvert_server-0.0.1-py3-none-any.whl
export APP_VERSION=$(find ../../../src/ -name "version.txt" | xargs cat )
export IMG_VERSION=$(python3 -c 'import os;print(".".join(os.environ["APP_VERSION"].strip().split(".")[:-1]))')

docker build --tag=qualityobjects/qonvert-server:latest --tag=qualityobjects/qonvert-server:$IMG_VERSION \
     --build-arg="wheel_pkg=$PKG_PATH" \
     --label="version=$APP_VERSION" --label="maintainer=Quality Objects S.L." \
     --rm -f Dockerfile.runtime .
# docker run --rm -it -p8080:8080 qonvert-server

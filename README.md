## $\textnormal{Description}$

> - Anythin related to computer vision.

```plaintext
OpenCV Docs: https://docs.opencv.org/4.x/index.html
```

<br />
<br />



## $\textnormal{OpenCV Guides}$

> - Download and build the core modules.

```sh
# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip

# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
unzip opencv.zip

# Create build directory
mkdir -p build && cd build

# Configure
cmake  ../opencv-4.x

# Build
cmake --build .
```

> - By default OpenCV will be installed to the `/usr/local` directory, <br />
    all files will be copied to following locations:

```plaintext
/usr/local/bin              : executable files
/usr/local/lib              : libraries (.so)
/usr/local/cmake/opencv4    : cmake package
/usr/local/include/opencv4  : headers
/usr/local/share/opencv4    : other files (e.g. trained cascades in XML format)
```

> - Install the OpenCV.

```sh
# Go the build directory.
cd build

# Run the install script in Makefile.
sudo make install
```

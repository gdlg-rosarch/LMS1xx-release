# Script generated with Bloom
pkgdesc="ROS - The lms1xx package contains a basic ROS driver for the SICK LMS1xx line of LIDARs."
url='http://ros.org/wiki/LMS1xx'

pkgname='ros-kinetic-lms1xx'
pkgver='0.1.6_1'
pkgrel=1
arch=('any')
license=('LGPL'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roslaunch'
'ros-kinetic-roslint'
'ros-kinetic-rosunit'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=lms1xx
source=()
md5sums=()

prepare() {
    cp -R $startdir/lms1xx $srcdir/lms1xx
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}


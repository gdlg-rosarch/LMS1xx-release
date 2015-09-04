Name:           ros-indigo-lms1xx
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS lms1xx package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/LMS1xx
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosconsole-bridge
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rosconsole-bridge
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-sensor-msgs

%description
The lms1xx package contains a basic ROS driver for the SICK LMS1xx line of
LIDARs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Sep 04 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.4-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.3-0
- Autogenerated by Bloom

* Tue Jan 20 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.2-0
- Autogenerated by Bloom


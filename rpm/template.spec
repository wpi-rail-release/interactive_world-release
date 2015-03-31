Name:           ros-indigo-interactive-world-tools
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS interactive_world_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/interactive_world_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       jsoncpp-devel
Requires:       libcurl-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-carl-dynamixel
Requires:       ros-indigo-carl-moveit
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-interactive-world-msgs
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-rail-manipulation-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-ros
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-carl-dynamixel
BuildRequires:  ros-indigo-carl-moveit
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-interactive-world-msgs
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-rail-manipulation-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  yaml-cpp-devel

%description
Tools and Modules for the Interactive World Models

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
* Tue Mar 31 2015 Russell Toris <rctoris@wpi.edu> - 0.0.7-0
- Autogenerated by Bloom

* Mon Mar 30 2015 Russell Toris <rctoris@wpi.edu> - 0.0.6-0
- Autogenerated by Bloom

* Wed Feb 18 2015 Russell Toris <rctoris@wpi.edu> - 0.0.5-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Russell Toris <rctoris@wpi.edu> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jan 16 2015 Russell Toris <rctoris@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Tue Dec 16 2014 Russell Toris <rctoris@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom


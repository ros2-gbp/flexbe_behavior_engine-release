Name:           ros-indigo-flexbe-states
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS flexbe_states package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/flexbe_states
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-flexbe-msgs
Requires:       ros-indigo-flexbe-testing
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rospy
Requires:       ros-indigo-smach-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rostest

%description
flexbe_states provides a collection of predefined states. Feel free to add new
states.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sat Dec 01 2018 Philipp Schillinger <schillin@kth.se> - 1.1.0-0
- Autogenerated by Bloom


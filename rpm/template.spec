%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-flexbe-onboard
Version:        2.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS flexbe_onboard package

License:        BSD
URL:            http://ros.org/wiki/flexbe_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-flexbe-core
Requires:       ros-humble-flexbe-msgs
Requires:       ros-humble-flexbe-states
Requires:       ros-humble-launch-ros
Requires:       ros-humble-rclpy
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-flexbe-core
BuildRequires:  ros-humble-flexbe-msgs
BuildRequires:  ros-humble-flexbe-states
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-launch-testing
%endif

%description
flexbe_onboard implements the robot-side of the behavior engine from where all
behaviors are started.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed May 01 2024 Philipp Schillinger <philsplus@gmail.com> - 2.3.4-1
- Autogenerated by Bloom

* Thu Aug 10 2023 Philipp Schillinger <philsplus@gmail.com> - 2.3.3-1
- Autogenerated by Bloom

* Tue Aug 01 2023 Philipp Schillinger <philsplus@gmail.com> - 2.3.2-1
- Autogenerated by Bloom


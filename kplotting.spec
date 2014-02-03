%define major 5
%define libname %mklibname KF5Plotting %{major}
%define devname %mklibname KF5Plotting -d
%define debug_package %{nil}

Name: kplotting
Version: 4.95.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 plotting library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

%description
KPlotting offers graph drawing functions.

KPlotting can be used to draw beautiful graphs on top of QWidgets. It
takes care of transformation of data coordinates to screen coordinates,
among other things.

%package -n %{libname}
Summary: The KDE Frameworks 5 plotting library
Group: System/Libraries

%description -n %{libname}
KPlotting offers graph drawing functions.

KPlotting can be used to draw beautiful graphs on top of QWidgets. It
takes care of transformation of data coordinates to screen coordinates,
among other things.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KPlotting offers graph drawing functions.

KPlotting can be used to draw beautiful graphs on top of QWidgets. It
takes care of transformation of data coordinates to screen coordinates,
among other things.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Plotting

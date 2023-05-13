%define major 5
%define libname %mklibname KF5Plotting %{major}
%define devname %mklibname KF5Plotting -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kplotting
Version:	5.106.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 plotting library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(Qt5UiPlugin)
# For QCH docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Plotting
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

%files designer
%{_libdir}/qt5/plugins/designer/kplotting5widgets.so

Name: libksane
Summary:  A library for dealing with scanners 
Version: 4.7.95
Release: 1
Epoch: 2
Group: System/Libraries
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libsane-devel
BuildRequires: automoc4
Conflicts: kdegraphics4-core < 2:4.6.90

%description
LibKSane is a KDE interface for SANE library to control flat scanner.

%files
%_kde_iconsdir/hicolor/*/actions/black-white.png
%_kde_iconsdir/hicolor/*/actions/color.png
%_kde_iconsdir/hicolor/*/actions/gray-scale.png

#------------------------------------------------

%define ksane_major 0
%define libksane %mklibname ksane %ksane_major

%package -n %libksane
Summary: A library for dealing with scanners 
Group: System/Libraries

%description -n %libksane
LibKSane is a KDE interface for SANE library to control flat scanners.

%files -n %libksane
%_kde_libdir/libksane.so.%{ksane_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: libsane-devel
Requires: %libksane = %epoch:%version-%release
Conflicts: kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%_kde_includedir/%{name}
%_kde_libdir/cmake/KSane/KSaneConfig.cmake
%_kde_libdir/libksane.so
%_kde_libdir/pkgconfig/libksane.pc

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A library for dealing with scanners
Name:		libksane
Version:	15.08.2
Release:	1
Epoch:		2
Group:		System/Libraries
License:	GPLv2
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	sane-devel
BuildRequires:	automoc4
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
LibKSane is a KDE interface for SANE library to control flat scanner.

%files
%{_kde_iconsdir}/hicolor/*/actions/black-white.png
%{_kde_iconsdir}/hicolor/*/actions/color.png
%{_kde_iconsdir}/hicolor/*/actions/gray-scale.png

#------------------------------------------------

%define ksane_major 0
%define libksane %mklibname ksane %{ksane_major}

%package -n %{libksane}
Summary:	A library for dealing with scanners
Group:		System/Libraries

%description -n %{libksane}
LibKSane is a KDE interface for SANE library to control flat scanners.

%files -n %{libksane}
%{_kde_libdir}/libksane.so.%{ksane_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	sane-devel
Requires:	%{libksane} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_includedir}/%{name}
%{_kde_libdir}/cmake/KSane/KSaneConfig.cmake
%{_kde_libdir}/libksane.so
%{_kde_libdir}/pkgconfig/libksane.pc

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

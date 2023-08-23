%define major 5
%define libname %mklibname KF5Sane %{major}
%define devname %mklibname KF5Sane -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A library for dealing with scanners
Name:		libksane
Version:	23.08.0
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	sane-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KSaneCore)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)

%description
LibKSane is a KDE interface for SANE library to control flat scanner.

%files -f libksane.lang
%{_datadir}/icons/*/*/*/*

#------------------------------------------------

%package -n %{libname}
Summary:	A library for dealing with scanners
Group:		System/Libraries
Provides:	ksane = %{EVRD}
Requires:	%{name} = %{EVRD}

%description -n %{libname}
LibKSane is a KDE interface for SANE library to control flat scanners.

%files -n %{libname}
%{_libdir}/libKF5Sane.so.%{major}*
%{_libdir}/libKF5Sane.so.%(echo %{version} |cut -d. -f1)*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	sane-devel
Requires:	%{libname} = %{EVRD}

%description  -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files  -n %{devname}
%{_includedir}/KF5/KSane
%{_libdir}/cmake/KF5Sane
%{_libdir}/*.so

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libksane

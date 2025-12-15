#define git 20240217
%define gitbranch release/24.12
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define oldlibname %mklibname KF5Sane 5
%define lib5name %mklibname KF5Sane
%define dev5name %mklibname KF5Sane -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KSaneWidgets6
%define devname %mklibname KSaneWidgets6 -d

Summary:	A library for dealing with scanners
Name:		libksane
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	GPLv2
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/libksane/-/archive/%{gitbranch}/libksane-%{gitbranchd}.tar.bz2#/libksane-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	sane-devel
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KSaneCore6)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
%rename plasma6-libksane

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
Obsoletes:	%{lib5name} < %{EVRD}

%description -n %{libname}
LibKSane is a KDE interface for SANE library to control flat scanners.

%files -n %{libname}
%{_libdir}/libKSaneWidgets6.so.*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	sane-devel
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{dev5name} < %{EVRD}

%description  -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files  -n %{devname}
%{_includedir}/KSaneWidgets6
%{_libdir}/cmake/KSaneWidgets6
%{_libdir}/libKSaneWidgets6.so

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n libksane-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=6 \
        -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libksane

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdegraphics-mobipocket
Version  : 19.04.0
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.0/src/kdegraphics-mobipocket-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/kdegraphics-mobipocket-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/kdegraphics-mobipocket-19.04.0.tar.xz.sig
Summary  : A collection of plugins to handle mobipocket files
Group    : Development/Tools
License  : GPL-2.0
Requires: kdegraphics-mobipocket-data = %{version}-%{release}
Requires: kdegraphics-mobipocket-lib = %{version}-%{release}
Requires: kdegraphics-mobipocket-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the kdegraphics-mobipocket package.
Group: Data

%description data
data components for the kdegraphics-mobipocket package.


%package dev
Summary: dev components for the kdegraphics-mobipocket package.
Group: Development
Requires: kdegraphics-mobipocket-lib = %{version}-%{release}
Requires: kdegraphics-mobipocket-data = %{version}-%{release}
Provides: kdegraphics-mobipocket-devel = %{version}-%{release}
Requires: kdegraphics-mobipocket = %{version}-%{release}

%description dev
dev components for the kdegraphics-mobipocket package.


%package lib
Summary: lib components for the kdegraphics-mobipocket package.
Group: Libraries
Requires: kdegraphics-mobipocket-data = %{version}-%{release}
Requires: kdegraphics-mobipocket-license = %{version}-%{release}

%description lib
lib components for the kdegraphics-mobipocket package.


%package license
Summary: license components for the kdegraphics-mobipocket package.
Group: Default

%description license
license components for the kdegraphics-mobipocket package.


%prep
%setup -q -n kdegraphics-mobipocket-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557007559
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557007559
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdegraphics-mobipocket
cp COPYING %{buildroot}/usr/share/package-licenses/kdegraphics-mobipocket/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/mobithumbnail.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/qmobipocket/mobipocket.h
/usr/include/qmobipocket/qfilestream.h
/usr/include/qmobipocket/qmobipocket_export.h
/usr/lib64/cmake/QMobipocket/QMobipocketConfig.cmake
/usr/lib64/cmake/QMobipocket/QMobipocketConfigVersion.cmake
/usr/lib64/cmake/QMobipocket/QMobipocketTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QMobipocket/QMobipocketTargets.cmake
/usr/lib64/libqmobipocket.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqmobipocket.so.2
/usr/lib64/libqmobipocket.so.2.0.0
/usr/lib64/qt5/plugins/mobithumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdegraphics-mobipocket/COPYING

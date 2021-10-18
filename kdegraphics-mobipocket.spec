#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdegraphics-mobipocket
Version  : 21.08.2
Release  : 33
URL      : https://download.kde.org/stable/release-service/21.08.2/src/kdegraphics-mobipocket-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/kdegraphics-mobipocket-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/kdegraphics-mobipocket-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdegraphics-mobipocket-data = %{version}-%{release}
Requires: kdegraphics-mobipocket-lib = %{version}-%{release}
Requires: kdegraphics-mobipocket-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
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
%setup -q -n kdegraphics-mobipocket-21.08.2
cd %{_builddir}/kdegraphics-mobipocket-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634403603
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634403603
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdegraphics-mobipocket
cp %{_builddir}/kdegraphics-mobipocket-21.08.2/COPYING %{buildroot}/usr/share/package-licenses/kdegraphics-mobipocket/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/mobithumbnail.desktop
/usr/share/metainfo/org.kde.kdegraphics-mobipocket.metainfo.xml

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
/usr/share/package-licenses/kdegraphics-mobipocket/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

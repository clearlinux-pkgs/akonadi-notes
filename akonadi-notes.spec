#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-notes
Version  : 20.08.0
Release  : 23
URL      : https://download.kde.org/stable/release-service/20.08.0/src/akonadi-notes-20.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.0/src/akonadi-notes-20.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.0/src/akonadi-notes-20.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: akonadi-notes-lib = %{version}-%{release}
Requires: akonadi-notes-license = %{version}-%{release}
Requires: akonadi-notes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kmime-dev
BuildRequires : qtbase-dev

%description
# Akonadi Notes #
Akonadi Notes is a library that effectively bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package dev
Summary: dev components for the akonadi-notes package.
Group: Development
Requires: akonadi-notes-lib = %{version}-%{release}
Provides: akonadi-notes-devel = %{version}-%{release}
Requires: akonadi-notes = %{version}-%{release}

%description dev
dev components for the akonadi-notes package.


%package lib
Summary: lib components for the akonadi-notes package.
Group: Libraries
Requires: akonadi-notes-license = %{version}-%{release}

%description lib
lib components for the akonadi-notes package.


%package license
Summary: license components for the akonadi-notes package.
Group: Default

%description license
license components for the akonadi-notes package.


%package locales
Summary: locales components for the akonadi-notes package.
Group: Default

%description locales
locales components for the akonadi-notes package.


%prep
%setup -q -n akonadi-notes-20.08.0
cd %{_builddir}/akonadi-notes-20.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597767005
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597767005
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-notes
cp %{_builddir}/akonadi-notes-20.08.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-notes/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang akonadinotes5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Akonadi/Notes/NoteUtils
/usr/include/KF5/akonadi-notes_version.h
/usr/include/KF5/akonadi/notes/NoteUtils
/usr/include/KF5/akonadi/notes/akonadi-notes_export.h
/usr/include/KF5/akonadi/notes/noteutils.h
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfig.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets.cmake
/usr/lib64/libKF5AkonadiNotes.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiNotes.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiNotes.so.5
/usr/lib64/libKF5AkonadiNotes.so.5.15.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-notes/20079e8f79713dce80ab09774505773c926afa2a

%files locales -f akonadinotes5.lang
%defattr(-,root,root,-)


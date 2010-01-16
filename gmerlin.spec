Name: gmerlin
Summary: A multimedia architecture for linux
Version: 0.4.1
Release: %mkrel 3
Url: http://gmerlin.sourceforge.net/
License: LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://downloads.sourceforge.net/gmerlin/%name-%version.tar.gz
BuildRequires: gavl-devel >= 1.1.0
BuildRequires: libmjpegtools-devel
BuildRequires: quicktime-devel
BuildRequires: pulseaudio-devel
BuildRequires: libalsa-devel
BuildRequires: jpeg-devel
BuildRequires: png-devel
BuildRequires: texinfo
BuildRequires: doxygen
BuildRequires: libxml2-devel >= 2.4.0
BuildRequires: fontconfig-devel >= 2.2.3
BuildRequires: freetype2-devel
BuildRequires: gtk2-devel >= 2.8.0
BuildRequires: X11-devel
BuildRequires: libcdio-devel
BuildRequires: libvisual-devel
BuildRequires: tiff-devel
BuildRequires: libcddb-devel

%description
The gmerlin application framework consists of a toolkit indepentent
gmerlin library, which contains the player core, the transcoder core
and other utilities. It can be used to build custom multimedia
applications.

%files -f %name.lang
%defattr(-,root,root)
%doc %_datadir/doc/%name
%_bindir/*
%dir %_prefix/lib/%name
%_prefix/lib/%name/plugins
%_datadir/%name
%_datadir/applications/*.desktop
%_mandir/man1/*
%_infodir/*

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname %name %major

%package -n %libname
Group: System/Libraries
Summary: Libraries for %name

%description -n %libname
This package contains shared libraries for %name.

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %name

%package -n %develname
Group: Development/Other
Summary: Development files for %name
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %develname
This package contains development files for %name.

%files -n %develname
%defattr(-,root,root)
%_includedir/%name
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

# drop la files
rm -fr %buildroot%_prefix/lib/%_prefix/lib/%name/plugins/*.la

%find_lang %name

%clean
rm -rf %buildroot

%define major 0
%define libname %mklibname %{name} %{major}
%define libgtk %mklibname %{name}_gtk %{major}
%define devname %mklibname -d %{name}

Summary:	A multimedia architecture for linux
Name:		gmerlin
Version:	1.2.0
Release:	2
License:	GPLv3+
Group:		Video
Url:		https://gmerlin.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
Patch0:		gmerlin-1.0.0-link.patch
Patch1:		gmerlin-1.2.0-icons.patch
Patch2:		gmerlin-1.2.0-desktop.patch
BuildRequires:	doxygen
BuildRequires:	texinfo
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gavl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libquicktime)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xv)

%description
The gmerlin application framework consists of a toolkit indepentent
gmerlin library, which contains the player core, the transcoder core
and other utilities. It can be used to build custom multimedia
applications.

%files -f %{name}.lang
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*
%{_infodir}/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgtk}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gmerlin0 < 1.2.0

%description -n %{libgtk}
This package contains shared library for %{name}.

%files -n %{libgtk}
%{_libdir}/lib%{name}_gtk.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{libgtk} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

%find_lang %{name}


# TODO
# - use system fonts
#
%define	_alpha	alpha
Summary:	3D chess game for X-Window
Summary(pl.UTF-8):	Trójwymiarowe szachy dla X-Window
Name:		brutalchess
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/brutalchess/%{name}-%{_alpha}-%{version}-src.tar.gz
# Source0-md5:	370476b63091b8d82a9ea57c604dcbab
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-GLvoid.patch
URL:		http://brutalchess.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brutal Chess features full 3D graphics, an advanced engine, and
several different levels of intelligent AI.

%description -l pl.UTF-8
Brutal Chess cechuje pełna trójwymiarowa grafika, zaawansowany silnik
i kilka różnych poziomów sztucznej inteligencji.

%prep
%setup -q
%patch0 -p0
%{__sed} -i 's@../art@%{_datadir}/brutalchess/art@' src/{basicset.cpp,gamecore.cpp,granitetheme.cpp}
%{__sed} -i 's@../fonts@%{_datadir}/brutalchess/fonts@' src/gamecore.cpp
%{__sed} -i 's@../models@%{_datadir}/brutalchess/models@' src/{basicset.cpp,gamecore.cpp}
rm -f models/.cvsignore

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install	%{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -r art  $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r fonts $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r models $RPM_BUILD_ROOT%{_datadir}/%{name}

# remove these files to avoid confusion with installed but unpacked files
rm -rf $RPM_BUILD_ROOT%{_docdir}/brutalchess/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/md3view
%attr(755,root,root) %{_libdir}/objview
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm

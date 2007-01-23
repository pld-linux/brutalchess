# TODO
# - use system fonts
#
%define	_alpha	alpha
Summary:	3D chess game for X-Window
Summary(pl):	Trójwymiarowe szachy dla X-Window
Name:		brutalchess
Version:	0.5.2
Release:	0.%{_alpha}.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/brutalchess/%{name}-%{_alpha}-%{version}-src.tar.gz
# Source0-md5:	370476b63091b8d82a9ea57c604dcbab
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://brutalchess.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brutal Chess features full 3D graphics, an advanced engine, and
several different levels of intelligent AI.

%description -l pl
Brutal Chess cechuje pe³na trójwymiarowa grafika, zaawansowany silnik
i kilka ró¿nych poziomów sztucznej inteligencji.

%prep
%setup -q
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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install	%{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm

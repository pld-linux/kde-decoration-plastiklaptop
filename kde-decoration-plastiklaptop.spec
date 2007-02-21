%define		_decoration plastiklaptop
Summary:	Kwin decoration - %{_decoration}
Summary(pl.UTF-8):Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.6.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/CONTENT/content-files/34616-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	686365e0dfbea44a15d6dd865613cb3c
URL:		http://www.kde-look.org/content/show.php?content=34616
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_decoration} is a modification to the Plastik kwin window decoration
adding the ability to make the most used titlebar buttons rectangular.

%description -l pl.UTF-8
%{_decoration} jest modyfikacją dekoracji kwin Plastik pozwalającą
korzystać z prostokątnych przycisków paska tytułowego.

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
#%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

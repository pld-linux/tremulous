#
# Conditional build:
%bcond_with	altivec		# use altivec, no runtime detection
%bcond_without	openal		# don't use OpenAL

Summary:	Tremulous for Linux
Summary(pl):	Tremulous dla Linuksa
Name:		tremulous
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	%{name}-%{version}-src.tar.gz
# Source0-md5:	13382bfd1c17677ff97109a457f4c488
Source2:	tremded.init
Source3:	tremded.sysconfig
Source4:	%{name}.desktop
Source5:	%{name}-smp.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-LIBDIR.patch
Patch2:		%{name}-alpha.patch
URL:		http://www.tremulous.net/
%if %{with openal}
BuildRequires:	OpenAL-devel
%endif
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{name}-common = %{version}-%{release}
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-ffast-math -funroll-loops -fomit-frame-pointer -fno-strict-aliasing
%define		specflags_ia32	-falign-loops=2 -falign-jumps=2 -falign-functions=2
%if %{with altivec}
%define		specflags_ppc	-maltivec -mabi=altivec
%endif
%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Tremulous for Linux.

%description -l pl
Tremulous dla Linuksa.

%package server
Summary:	Tremulous server
Summary(pl):	Serwer Tremulous
Group:		Applications/Games
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(triggerpostun):	/usr/sbin/usermod
Requires:	%{name}-common = %{version}-%{release}
Requires:	psmisc
Requires:	rc-scripts
Requires:	screen
Provides:	group(tremulous)
Provides:	user(tremulous)

%description server
Tremulous server.

%description server -l pl
Serwer Tremulous.

%package smp
Summary:	Tremulous for SMP
Summary(pl):	Tremulous dla SMP
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description smp
Tremulous for multi processor machine.

%description smp -l pl
Tremulous dla maszyny wieloprocesorowej.

%package common
Summary:	Common files for Tremulous
Summary(pl):	Pliki wspólne dla Tremulous
Group:		Applications/Games
Requires(triggerpostun):	/usr/sbin/groupdel
Requires(triggerpostun):	/usr/sbin/userdel
Requires:	%{name}-data = %{version}

%description common
Common files for Tremulous server and player game.

%description common -l pl
Pliki wspólne Tremulous dla serwera i trybu gracza.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
cat << EOF > Makefile.local
BUILD_CLIENT	= 1
BUILD_CLIENT_SMP= 1
BUILD_SERVER	= 1
BUILD_GAME_SO	= 1
BUILD_GAME_QVM	= 0
%if %{without openal}
USE_OPENAL	= 0
%endif
EOF

%build
CFLAGS="%{rpmcflags}"
CFLAGS="$CFLAGS -DDEFAULT_BASEDIR=\\\"%{_datadir}/games/%{name}\\\""
CFLAGS="$CFLAGS -DLIBDIR=\\\"%{_libdir}/%{name}\\\""
CFLAGS="$CFLAGS -Wall -Wimplicit -Wstrict-prototypes"
CFLAGS="$CFLAGS -DUSE_SDL_VIDEO=1 -DUSE_SDL_SOUND=1 $(sdl-config --cflags)"
%if %{with openal}
CFLAGS="$CFLAGS -DUSE_OPENAL=1"
%endif
CFLAGS="$CFLAGS -DNDEBUG -MMD"
%ifnarch %{ix86} %{x8664}
CFLAGS="$CFLAGS -DNO_VM_COMPILED"
%endif

%{__make} makedirs tools targets \
	B="release-%{_target}"	\
	CC="%{__cc}"		\
	CFLAGS="$CFLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}/base} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_libdir}/%{name}/base} \
	$RPM_BUILD_ROOT/var/games/tremulous

install release-%{_target}/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
install release-%{_target}/%{name}-smp.* $RPM_BUILD_ROOT%{_bindir}/%{name}-smp
install release-%{_target}/tremded.* $RPM_BUILD_ROOT%{_bindir}/tremded
install release-%{_target}/base/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/base

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/tremded
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/tremded
install misc/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/%{name}-smp.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
%groupadd -P %{name}-server -g 38 tremulous
%useradd -P %{name}-server -u 124 -d /var/games/tremulous -s /bin/sh -c "Tremulous" -g tremulous tremulous

%post server
/sbin/chkconfig --add tremded
%service tremded restart "Tremulous server"

%preun server
if [ "$1" = "0" ]; then
	%service tremded stop
	/sbin/chkconfig --del tremded
fi

%postun server
if [ "$1" = "0" ]; then
	%userremove tremulous
	%groupremove tremulous
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop

%files common
%defattr(644,root,root,755)
%doc ChangeLog COPYING
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/base
%{_pixmapsdir}/%{name}.xpm
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/base
%attr(755,root,root) %{_libdir}/%{name}/base/*.so

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/tremded
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/tremded
%attr(755,root,root) %{_bindir}/tremded
%attr(750,tremulous,tremulous) /var/games/tremulous

%files smp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-smp
%{_desktopdir}/%{name}-smp.desktop

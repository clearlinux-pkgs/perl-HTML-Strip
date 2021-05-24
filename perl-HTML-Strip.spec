#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Strip
Version  : 2.10
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/K/KI/KILINRAX/HTML-Strip-2.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KI/KILINRAX/HTML-Strip-2.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-strip-perl/libhtml-strip-perl_2.10-1.debian.tar.xz
Summary  : 'Perl extension for stripping HTML markup from text.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Strip-license = %{version}-%{release}
Requires: perl-HTML-Strip-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
HTML::Strip
===========
This module strips HTML-like markup from text.
It is written in XS, and thus about five times quicker than using
regular expressions for the same task.

%package dev
Summary: dev components for the perl-HTML-Strip package.
Group: Development
Provides: perl-HTML-Strip-devel = %{version}-%{release}
Requires: perl-HTML-Strip = %{version}-%{release}

%description dev
dev components for the perl-HTML-Strip package.


%package license
Summary: license components for the perl-HTML-Strip package.
Group: Default

%description license
license components for the perl-HTML-Strip package.


%package perl
Summary: perl components for the perl-HTML-Strip package.
Group: Default
Requires: perl-HTML-Strip = %{version}-%{release}

%description perl
perl components for the perl-HTML-Strip package.


%prep
%setup -q -n HTML-Strip-2.10
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-strip-perl_2.10-1.debian.tar.xz
cd %{_builddir}/HTML-Strip-2.10
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-Strip-2.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Strip
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-Strip/48acdc4e0745947404025d9f5225d158126143b6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Strip.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Strip/48acdc4e0745947404025d9f5225d158126143b6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/HTML/Strip.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/HTML/Strip/Strip.so

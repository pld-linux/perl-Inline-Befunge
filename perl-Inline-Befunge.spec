#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	Befunge
Summary:	Inline::Befunge Perl module
Summary(cs):	Modul Inline::Befunge pro Perl
Summary(da):	Perlmodul Inline::Befunge
Summary(de):	Inline::Befunge Perl Modul
Summary(es):	Módulo de Perl Inline::Befunge
Summary(fr):	Module Perl Inline::Befunge
Summary(it):	Modulo di Perl Inline::Befunge
Summary(ja):	Inline::Befunge Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Befunge ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Inline::Befunge
Summary(pl):	Modu³ Perla Inline::Befunge
Summary(pt):	Módulo de Perl Inline::Befunge
Summary(pt_BR):	Módulo Perl Inline::Befunge
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Befunge
Summary(sv):	Inline::Befunge Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Befunge
Summary(zh_CN):	Inline::Befunge Perl Ä£¿é
Name:		perl-Inline-Befunge
Version:	0.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55f6720ea86102a1f987105fcbff183d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Befunge >= 0.36
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Befunge - write Perl subs in Befunge.

%description -l pl
Modu³ Inline::Befunge - pozwalaj±cy na pisanie procedur Perla w jêzyku
Befunge.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/Befunge.pm
%{_mandir}/man3/*

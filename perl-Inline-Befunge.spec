#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	Befunge
Summary:	Inline::Befunge Perl module
Summary(cs.UTF-8):	Modul Inline::Befunge pro Perl
Summary(da.UTF-8):	Perlmodul Inline::Befunge
Summary(de.UTF-8):	Inline::Befunge Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::Befunge
Summary(fr.UTF-8):	Module Perl Inline::Befunge
Summary(it.UTF-8):	Modulo di Perl Inline::Befunge
Summary(ja.UTF-8):	Inline::Befunge Perl モジュール
Summary(ko.UTF-8):	Inline::Befunge 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::Befunge
Summary(pl.UTF-8):	Moduł Perla Inline::Befunge
Summary(pt.UTF-8):	Módulo de Perl Inline::Befunge
Summary(pt_BR.UTF-8):	Módulo Perl Inline::Befunge
Summary(ru.UTF-8):	Модуль для Perl Inline::Befunge
Summary(sv.UTF-8):	Inline::Befunge Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::Befunge
Summary(zh_CN.UTF-8):	Inline::Befunge Perl 模块
Name:		perl-Inline-Befunge
Version:	0.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55f6720ea86102a1f987105fcbff183d
URL:		http://search.cpan.org/dist/Inline-Befunge/
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Befunge >= 0.36
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Befunge - write Perl subs in Befunge.

%description -l pl.UTF-8
Moduł Inline::Befunge - pozwalający na pisanie procedur Perla w języku
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

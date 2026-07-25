%define upstream_name    Test-Sys-Info
%define upstream_version 0.23

%define debug_package %{nil}

Summary:	Centralized test suite for Sys::Info
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
License:    GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/burak/CPAN-Test-Sys-Info
Source0:	https://cpan.metacpan.org/authors/id/B/BU/BURAK/Test-Sys-Info-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl-Sys-Info-Base

%description
Perl centralized test suite for Sys::Info.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

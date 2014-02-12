%define upstream_name    Test-Sys-Info
%define upstream_version 0.20

%define debug_package %{nil}

Summary:	Centralized test suite for Sys::Info
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:    GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz
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

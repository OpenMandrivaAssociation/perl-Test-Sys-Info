%define upstream_name    Test-Sys-Info
%define upstream_version 0.17

Summary:	Centralized test suite for Sys::Info
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:        GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
Requires:	perl-Sys-Info-Base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

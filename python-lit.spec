Name: python-lit
Version: 0.5.0
Release: 0%{?dist}
BuildArch: noarch

License: NCSA
Group: Development/Languages
Summary: Tool for executing llvm test suites
URL: https://pypi.python.org/pypi/lit
Source0: https://pypi.python.org/packages/5b/a0/dbed2c8dfb220eb9a5a893257223cd0ff791c0fbc34ce2f1a957fa4b6c6f/lit-0.5.0.tar.gz

BuildRequires: python2-devel
BuildRequires: python2-setuptools

%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif # if with_python3

%description
lit is a tool used by the LLVM project for executing its test suites.

%if 0%{?with_python3}
%package -n python3-lit
Summary: lit test runner for Python 3
Group: Development/Languages

%description -n python3-lit
lit is a tool used by the LLVM project for executing its test suites.

%endif # with_python3

%prep
%autosetup -n lit-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
rm -rf %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
mv %{buildroot}/%{_bindir}/lit %{buildroot}/%{_bindir}/python3-lit
popd
%endif # with_python3

%{__python} setup.py install --skip-build --root %{buildroot}

%check
python2 setup.py test

# FIXME: Tests fail with python3
#%if 0%{?with_python3}
#pushd %{py3dir}
#python3 setup.py test
#popd
#%endif

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/lit
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-lit
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/python3-lit
%{python3_sitelib}/*
%endif

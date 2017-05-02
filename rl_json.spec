%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          rl_json
Summary:       Extends Tcl with a json value type and a command to manipulate json values directly
Version:       0.9.7
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        rl_json-0.9.7.tar.gz
URL:           https://github.com/RubyLane/rl_json
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
This package adds a command json to the interpreter, and defines a new
Tcl_Obj type to store the parsed JSON document. The json command directly
manipulates values whose string representation is valid JSON, in a similar
way to how the dict command directly manipulates values whose string
representation is a valid dictionary. It is similar to dict in performance.

%prep
%setup -q -n %{name}-%{version}

%build
%{__autoconf}
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc LICENSE README.md
%defattr(-,root,root)
%{directory}/%{_lib}/tcl


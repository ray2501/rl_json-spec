%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          rl_json
Summary:       Extends Tcl with a json value type and a command to manipulate json values directly
Version:       0.9.14
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        rl_json-0.9.14.tar.gz
Patch0:        noman.patch
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


%package devel
Summary:        Development package for rl_json
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
This package contains development files for rl_json.

%prep
%setup -q -n %{name}-%{version}
%patch0

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
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc LICENSE README.md
%defattr(-,root,root)
%{tcl_archdir}

%files devel
%defattr(-,root,root)
%{directory}/include/rl_jsonDecls.h


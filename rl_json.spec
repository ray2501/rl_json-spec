%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          rl_json
Summary:       Extends Tcl with a json value type to manipulate json objects
Version:       0.15.1
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        rl_json-%{version}.tar.gz
Patch0:        noman.patch
URL:           https://github.com/RubyLane/rl_json
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
This package adds a command json to the interpreter, and defines a new
Tcl_Obj type to store the parsed JSON document. The json command
directly manipulates values whose string representation is valid JSON,
in a similar way to how the dict command directly manipulates values
whose string representation is a valid dictionary. It is similar to
dictin performance.


%prep
%setup -q -n %{name}-%{version}
%patch 0

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf --force
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

# Build failed because openSUSE Tumbleweed LTO request (add flag but no help)
# Add a workaround: remove static library and header files
# Since I remove static library, then also remove header files
find %{buildroot}%{tcl_archdir}/%{name}%{version} -type f -name "*.a" -delete -print
find %{buildroot}%{directory}/include -type f -name "*.h" -delete -print

%files
%doc LICENSE README.md
%defattr(-,root,root)
%{tcl_archdir}/%{name}%{version}

%changelog


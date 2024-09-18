#!/usr/bin/tclsh

set arch "x86_64"
set base "rl_json-0.15.2"

set var [list git clone --recurse-submodules https://github.com/RubyLane/rl_json.git $base]
exec >@stdout 2>@stderr {*}$var

cd $base

set var2 [list git checkout eb5aa3bb211e528df21258aa7e983a38cd197ff5]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var [list tar czvf $base.tar.gz $base]
exec >@stdout 2>@stderr {*}$var
file delete -force $base

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force noman.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb rl_json.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz

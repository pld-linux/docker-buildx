Summary:	Docker CLI plugin for extended build capabilities
Name:		docker-buildx
Version:	0.25.0
Release:	1
License:	Apache v2.0
Group:		Applications/System
Source0:	https://github.com/docker/buildx/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	14797b2df82559a06bcf0a7c38235912
URL:		https://github.com/docker/buildx
BuildRequires:	golang >= 1.23.0
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	docker-ce-cli
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
buildx is a Docker CLI plugin for extended build capabilities with
BuildKit.

Key features:
- Familiar UI from docker build
- Full BuildKit capabilities with container driver
- Multiple builder instance support
- Multi-node builds for cross-platform images
- Compose build support
- High-level build constructs (bake)
- In-container driver support (both Docker and Kubernetes)

%prep
%setup -q -n buildx-%{version}

%build
%{__make} build \
	BUILDX_BIN=/bin/false \
	VERSION="%{version}" \
	REVISION="%{release}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libexecdir}/docker/cli-plugins

cp -p bin/build/docker-buildx $RPM_BUILD_ROOT%{_libexecdir}/docker/cli-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS PROJECT.md README.md
%attr(755,root,root) %{_libexecdir}/docker/cli-plugins/docker-buildx

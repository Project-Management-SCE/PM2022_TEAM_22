import apt
import sys


packages = ["libpq-dev", "python3-dev", "build-essential"]

for pkg_name in packages:
    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print("{pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        pkg.mark_install()
        try:
            cache.commit()
        except (BaseException):
            print("Unable to install")

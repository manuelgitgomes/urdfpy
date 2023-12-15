try:
    import roslib
    ros_available = True
except ImportError:
    ros_available = False


def resolve_ros_path(package_name):
    try:
        package_path = roslib.packages.get_pkg_dir(package_name)
    except roslib.packages.InvalidROSPkgException:
        package_path = None
    return package_path

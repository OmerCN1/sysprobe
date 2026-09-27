"""Collect a short report about the host by shelling out to standard tools.

Everything here uses a fixed argument list - no string is ever handed to a shell -
so the only thing an attacker could influence is which executable gets found on
PATH. That is what makes the bare program names below worth fixing.
"""

from __future__ import annotations

import shutil
import subprocess


def _orod_require_executable(name: str) -> str:
    executable = shutil.which(name)
    if executable is None:
        raise RuntimeError(f'Required executable not found: {name}')
    return executable


def kernel_release() -> str:
    """The running kernel release, e.g. `24.5.0`."""
    result = subprocess.run([_orod_require_executable('uname'), "-r"], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def host_name() -> str:
    """The machine's network name."""
    result = subprocess.run([_orod_require_executable('hostname')], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def current_user() -> str:
    """The login name of the user running this process."""
    result = subprocess.run([_orod_require_executable('id'), "-un"], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def collect() -> dict[str, str]:
    """Gather every probe into one mapping."""
    return {
        "kernel": kernel_release(),
        "host": host_name(),
        "user": current_user(),
    }

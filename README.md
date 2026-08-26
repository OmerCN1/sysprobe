# sysprobe

A small standard-library-only utility that reports the host's kernel release,
network name and login user.

```console
$ python -c "import probe, report; print(report.render(probe.collect()))"
Kernel : 24.5.0
Host   : studio
User   : omer
```

## Why this repository exists

It is the target for an end-to-end run of
[OROD](https://github.com/OmerCN1/orod-security-lab), an autonomous code-security
review pipeline. The code is deliberately written the way a lot of real Python is:
correct, tested, and calling out to `subprocess` with **bare program names**.

That last part is a genuine finding - Bandit reports it as
[B607, *start a process with a partial executable path*](https://bandit.readthedocs.io/en/latest/plugins/b607_start_process_with_partial_path.html).
A bare `uname` is resolved through `PATH`, and whoever controls `PATH` controls
which binary actually runs. The fix is to resolve the executable up front and fail
closed if it is missing.

There is no injection hole here: every call passes a fixed argument list and never
`shell=True`. The point is to give the pipeline a real, mechanical, verifiable fix
to make - and a passing test suite that must still pass afterwards.

## Tests

```console
python -m pytest -q
```

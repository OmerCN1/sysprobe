from probe import collect, current_user, host_name, kernel_release


def test_each_probe_returns_a_non_empty_line() -> None:
    for probe in (kernel_release, host_name, current_user):
        value = probe()
        assert value, f"{probe.__name__} returned nothing"
        assert "\n" not in value, f"{probe.__name__} returned more than one line"


def test_collect_reports_every_probe() -> None:
    values = collect()
    assert set(values) == {"kernel", "host", "user"}
    assert all(values.values())

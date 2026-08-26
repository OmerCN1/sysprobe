from report import render


def test_renders_known_keys_in_declared_order() -> None:
    out = render({"user": "omer", "kernel": "24.5.0", "host": "studio"})
    assert [line.split(" : ")[1] for line in out.splitlines()] == ["24.5.0", "studio", "omer"]


def test_aligns_the_labels() -> None:
    out = render({"kernel": "24.5.0", "host": "studio"})
    assert out.splitlines() == ["Kernel : 24.5.0", "Host   : studio"]


def test_unknown_keys_are_appended_alphabetically() -> None:
    out = render({"host": "studio", "zone": "utc", "arch": "arm64"})
    assert [line.split(" : ")[0].strip() for line in out.splitlines()] == ["Host", "arch", "zone"]


def test_empty_input_says_so() -> None:
    assert render({}) == "no data collected"

from functools import reduce


def top_n(scores, n):
    """The n highest (name, score) pairs, best first; ties by name."""
    return sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))[:n]


def compose(*functions):
    """compose(f, g, h)(x) == f(g(h(x)))"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def http_status(code):
    match code:
        case 200 | 201 | 204:
            return "success"
        case 301 | 302:
            return "redirect"
        case 404:
            return "not found"
        case _ if 400 <= code < 500:
            return "client error"
        case _ if 500 <= code < 600:
            return "server error"
        case _:
            return "unknown"


if __name__ == "__main__":
    print(top_n({"ana": 82, "ben": 95, "cy": 82, "dee": 70}, 3))
    shout = compose(lambda s: s + "!", str.upper, str.strip)
    print(shout("  hello "))
    for code in (200, 302, 404, 418, 503, 99):
        print(code, http_status(code))

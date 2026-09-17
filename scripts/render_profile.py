"""Render small, dependency-free profile cards from GitHub's GraphQL response."""

import json
import sys
from datetime import date
from pathlib import Path


def svg(height, title, description, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{height}" viewBox="0 0 720 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<style>
  .bg {{ fill: #f6f8fa; }}
  .text {{ fill: #24292f; }}
  .muted {{ fill: #57606a; }}
  .grid {{ stroke: #d0d7de; }}
  .line {{ stroke: #57606a; }}
  text {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill: #0d1117; }}
    .text {{ fill: #e6edf3; }}
    .muted {{ fill: #9198a1; }}
    .grid {{ stroke: #212830; }}
    .line {{ stroke: #b1bac4; }}
  }}
</style>
<rect class="bg" width="720" height="{height}" rx="8"/>
{content}
</svg>
'''


def render(payload, destination):
    if payload.get("errors"):
        raise ValueError("GitHub returned GraphQL errors; keeping the previous cards")
    user = payload["data"]["user"]
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    days = [day for week in weeks for day in week["contributionDays"]]
    if not days:
        raise ValueError("No contribution dates returned; keeping the previous cards")
    start, end = (date.fromisoformat(days[i]["date"]) for i in (0, -1))
    period = f"{start:%b %d, %Y} – {end:%b %d, %Y}"
    metrics = [
        (calendar["totalContributions"], "Contributions"),
        (sum(day["contributionCount"] > 0 for day in days), "Active days"),
        (user["repositories"]["totalCount"], "Public repos · non-forks"),
    ]
    stats = []
    for x, (value, label) in zip((120, 360, 600), metrics):
        stats.append(f'<text class="text" x="{x}" y="48" text-anchor="middle" font-size="28" font-weight="600">{value}</text>')
        stats.append(f'<text class="muted" x="{x}" y="73" text-anchor="middle" font-size="13">{label}</text>')
    stats.append(f'<text class="muted" x="360" y="104" text-anchor="middle" font-size="11">{period}</text>')

    totals = [sum(day["contributionCount"] for day in week["contributionDays"]) for week in weeks]
    maximum = max(1, max(totals))
    left, right, top, bottom = 42, 698, 38, 154
    graph = ['<text class="muted" x="22" y="22" font-size="12">Contributions per week</text>']
    for value in sorted({0, maximum // 2, maximum}):
        y = bottom - (bottom - top) * value / maximum
        graph.append(f'<path class="grid" d="M {left} {y:.1f} H {right}" fill="none"/>')
        graph.append(f'<text class="muted" x="30" y="{y + 4:.1f}" text-anchor="end" font-size="11">{value}</text>')
    points = []
    for index, count in enumerate(totals):
        x = left + (right - left) * index / max(1, len(totals) - 1)
        y = bottom - (bottom - top) * count / maximum
        points.append(f"{x:.1f},{y:.1f}")
    graph.append(f'<polyline class="line" points="{" ".join(points)}" fill="none" stroke-width="2" stroke-linejoin="round"/>')
    graph.append(f'<text class="muted" x="{left}" y="179" font-size="11">{start:%b %Y}</text>')
    graph.append(f'<text class="muted" x="{right}" y="179" text-anchor="end" font-size="11">{end:%b %Y}</text>')

    stats_svg = svg(120, "GitHub statistics", f"{period}. " + "; ".join(f"{value} {label}" for value, label in metrics), "\n".join(stats))
    graph_svg = svg(196, "GitHub activity", f"Weekly contributions, {period}. First and last weeks may be partial.", "\n".join(graph))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "github-stats.svg").write_text(stats_svg, encoding="utf-8")
    (destination / "github-activity.svg").write_text(graph_svg, encoding="utf-8")


if __name__ == "__main__":
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    render(payload, Path(__file__).resolve().parents[1] / "assets")

import re
import collections
import math

ORE, CLAY, OBSIDIAN, GEODE = 1, 2, 3, 4
MATERIALS = [ORE, CLAY, OBSIDIAN, GEODE]


def parse_blueprint(s):
    q = list(map(int, re.findall("\d+", s)))
    return {
        ORE: {ORE: q[1]},
        CLAY: {ORE: q[2]},
        OBSIDIAN: {ORE: q[3], CLAY: q[4]},
        GEODE: {ORE: q[5], OBSIDIAN: q[6]}
    }


def get_max_robots(bp):
    max_robots = {m: 0 for m in MATERIALS}
    max_robots[GEODE] = 100
    for _, needs in bp.items():
        for robot, qty in needs.items():
            max_robots[robot] = max(max_robots[robot], qty)
    return max_robots


def get_build_options(bp, resources):
    options = {0}
    for robot, needs in bp.items():
        if all(qty <= resources[need] for need, qty in needs.items()):
            options.add(robot)
    if GEODE in options:
        return {GEODE}
    return options


def build_robot(bp, robots, resources, to_build):
    robots[to_build] += 1
    for resource, qty in bp[to_build].items():
        resources[resource] -= qty
        assert resources[resource] >= 0
    return (robots, resources)


def harvest(robots, resources):
    for k, v in robots.items():
        resources[k] += v
    return resources


def largest_for_bp(bp, end_time):
    init_robots = {m: 0 for m in MATERIALS}
    init_robots[ORE] = 1
    stack = [(0, init_robots, {m: 0 for m in MATERIALS}, set())]
    best_at_time = collections.defaultdict(int)
    max_robots = get_max_robots(bp)
    while stack:
        t, robots, resources, skipped_last_iteration = stack.pop(0)
        best_at_time[t] = max(best_at_time[t], resources[GEODE])
        if t <= end_time and best_at_time[t] == resources[GEODE]:
            options = get_build_options(bp, resources)
            for to_build in options:
                if not to_build:
                    resources1 = harvest(robots, resources.copy())
                    stack.append((t + 1, robots, resources1, options))
                elif to_build in skipped_last_iteration:
                    continue
                elif robots[to_build] + 1 > max_robots[to_build]:
                    continue
                else:
                    robots1, resources1 = build_robot(
                        bp, robots.copy(), resources.copy(), to_build)
                    resources1 = harvest(robots, resources1.copy())
                    stack.insert(0, (t + 1, robots1, resources1, set()))
    print(best_at_time[end_time])
    return best_at_time[end_time]


bps = list(map(parse_blueprint, open('day19input.txt').read().split('\n')))
print(sum((i + 1) * largest_for_bp(bp, 24) for i, bp in enumerate(bps)))
print(math.prod(largest_for_bp(bp, 32) for bp in bps[:3]))

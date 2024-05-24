def min_total_time(n, m, l, ants):
    total_time = 0
    while ants:
        group_mass = 0
        group_time = 0
        while ants and group_mass + ants[0][0] <= m:
            ant_mass, ant_velocity = ants.pop(0)
            group_mass += ant_mass
            group_time = max(group_time, l / ant_velocity)
        total_time += group_time
    return total_time

def read_input(filename):
    with open(filename, 'r') as f:
        n, m, l = map(int, f.readline().split())
        ants = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, m, l, ants

def write_output(filename, total_time):
    with open(filename, 'w') as f:
        f.write("{:.2f}".format(total_time))

if __name__ == "__main__":
    n, m, l, ants = read_input("GROUANTS.INP")
    total_time = min_total_time(n, m, l, ants)
    write_output("GROUANTS.OUT", total_time)
